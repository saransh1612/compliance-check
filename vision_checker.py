"""
Vision Compliance Inspection Engine
Analyzes 4 truck photos (Front, Back, Left, Right) against Bharat Petroleum compliance specifications.
Supports:
1. Automated Gemini Multimodal Vision API (gemini-2.5-flash / gemini-1.5-flash)
2. Interactive Auditor Mode (Local verification & override)
3. Simulated Test Scenarios (Compliant, Non-compliant, Missing Panels)
"""

import json
import os
import io
from typing import Dict, Any, List, Optional
from PIL import Image
from compliance_rules import COMPLIANCE_CHECKLIST, REQUIRED_QUANTITIES, RULE_SPECS

def build_manual_audit(checklist_responses: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Builds a full compliance result object from human auditor checklist inputs.
    No API key needed!
    """
    total_checks = 0
    passed_checks = 0
    critical_violations = []
    
    sections = {
        "front": [],
        "left": [],
        "right": [],
        "back": []
    }
    
    for section_key, rules in COMPLIANCE_CHECKLIST.items():
        for rule in rules:
            rule_id = rule["id"]
            resp = checklist_responses.get(rule_id, {"status": "PASS", "observation": "Verified per BPCL standards", "action": "None"})
            status = resp.get("status", "PASS")
            obs = resp.get("observation", "Verified per BPCL standards")
            action = resp.get("action", "None required")
            defect_desc = "Compliant with specification" if status == "PASS" else obs
            
            total_checks += 1
            if status == "PASS":
                passed_checks += 1
            elif rule.get("critical", False) and status == "FAIL":
                critical_violations.append(f"{rule['name']}: {obs}")
            
            sections[section_key].append({
                "id": rule_id,
                "name": rule["name"],
                "status": status,
                "confidence": 1.0,
                "required_compliance": rule["spec"],
                "observation": obs,
                "defect_reason": defect_desc,
                "corrective_action": action,
                "side": section_key
            })
            
    score = int((passed_checks / total_checks) * 100) if total_checks > 0 else 0
    overall_status = "PASS" if len(critical_violations) == 0 and score >= 85 else "FAIL"
    
    # Quantities
    side_panels = 2 if (sections["left"][1]["status"] == "PASS" and sections["right"][1]["status"] == "PASS") else 1
    eip_panels = 3
    if sections["left"][2]["status"] != "PASS":
        eip_panels -= 1
    if sections["right"][2]["status"] != "PASS":
        eip_panels -= 1
    if sections["back"][0]["status"] != "PASS":
        eip_panels -= 1
        
    cabin_stickers = 0
    if sections["left"][0]["status"] == "PASS":
        cabin_stickers += 1
    if sections["right"][0]["status"] == "PASS":
        cabin_stickers += 1
        
    summary = "Vehicle passed all mandatory safety & branding specifications." if overall_status == "PASS" else f"Vehicle failed inspection. Rectify {len(critical_violations)} critical defect(s) before release."
    
    rear_text = [
        "EIP Board: LIQUIFIED PETROLEUM GAS, UN 1075, HAZCHEM 2WE",
        "Statutory Dial: POLICE 100, FIRE 101, AMBULANCE 102",
        "Extinguisher Advice: USE DRY CHEMICAL POWDER TYPE FIRE EXTINGUISHER"
    ]
    unauth = []
    for sec_list in sections.values():
        for chk in sec_list:
            if "UNAUTHORIZED" in chk["id"] and chk["status"] != "PASS":
                unauth.append(f"{chk['name']}: {chk['observation']}")
    
    return {
        "overall_status": overall_status,
        "compliance_score": score,
        "summary": summary,
        "critical_violations": critical_violations,
        "rear_text_detected": rear_text,
        "unauthorized_markings_found": unauth,
        "quantities": {
            "side_panels_detected": side_panels,
            "eip_panels_detected": eip_panels,
            "cabin_stickers_detected": cabin_stickers
        },
        "front_checks": sections["front"],
        "left_checks": sections["left"],
        "right_checks": sections["right"],
        "back_checks": sections["back"]
    }

# Try importing google-genai
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


def pil_to_part(img: Image.Image) -> Any:
    """Converts a PIL image to a google.genai types.Part object."""
    buf = io.BytesIO()
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(buf, format="JPEG", quality=90)
    return types.Part.from_bytes(data=buf.getvalue(), mime_type="image/jpeg")


def _enrich_checks_with_specs(audit_result: Dict[str, Any]) -> Dict[str, Any]:
    """Ensures every checklist item has side, required_compliance, and defect_reason for easy comparison."""
    for sec in ["front_checks", "left_checks", "right_checks", "back_checks"]:
        side_key = sec.replace("_checks", "")
        for item in audit_result.get(sec, []):
            item["side"] = side_key
            rule_id = item.get("id")
            if rule_id in RULE_SPECS:
                if not item.get("required_compliance"):
                    item["required_compliance"] = RULE_SPECS[rule_id]["spec"]
            if not item.get("defect_reason"):
                if item.get("status") == "PASS":
                    item["defect_reason"] = "Compliant with specification"
                else:
                    item["defect_reason"] = item.get("observation", "Non-compliant with specification")
    return audit_result


def run_gemini_vision_audit(
    front_img: Image.Image,
    back_img: Image.Image,
    left_img: Image.Image,
    right_img: Image.Image,
    api_key: str,
    model_name: str = "gemini-3.6-flash"
) -> Dict[str, Any]:
    """
    Executes an automated vision audit across all 4 angles using Gemini Multimodal AI.
    Uses modern Gemini 3.x Flash models with automatic fallback.
    """
    if not GENAI_AVAILABLE:
        raise RuntimeError("google-genai library is not installed. Please run: pip install google-genai")

    client = genai.Client(api_key=api_key)

    checklist_summary = json.dumps(COMPLIANCE_CHECKLIST, indent=2, ensure_ascii=False)

    prompt = f"""
You are a Senior Fleet Quality & Safety Compliance Auditor for Bharat Petroleum Corporation Limited (BPCL).
Your task is to inspect 4 photos of an LPG Packed Cylinder Truck (306 or 450 cylinders) STRICTLY against the official BPCL Guidelines and Specifications for LPG Packed Truck Panels and Stickers.

The 4 uploaded photos are:
1. Photo 1: Front View of Truck
2. Photo 2: Left Side (Helper Side) of Truck
3. Photo 3: Right Side (Driver Side) of Truck
4. Photo 4: Rear / Back View of Truck

CHECKLIST RULES FROM BPCL SPECIFICATION DOCUMENT:
{checklist_summary}

CRITICAL INSPECTION & DETECTION REQUIREMENTS:
1. STRICT DOCUMENT COMPLIANCE FOR ALL 4 SIDES:
   - Front View:
     * F1: "GOODS CARRIER" (310x1490mm) on royal blue background, bold white lettering, Class 2 flammable gas diamond in center.
     * F2: "Bharat Petroleum" front logo below windshield (160x1300mm).
     * F3: Class 2 Flammable Gas red diamond (250x250mm) on front bumper/grill.
     * F4: Standard BPCL blue & white cabin finish in good repair.
     * F5: Legible front registration number plate.
     * F6_UNAUTHORIZED_MARKINGS: Check for ANY unauthorized text, religious symbols (e.g. Om, Swastika, Cross), private slogans, mobile numbers, or unapproved decals on windshield or front cabin.
   - Left Side (Helper Side):
     * L1: "Bharatgas" sticker on helper cabin door (200x600mm) with tagline "COOK FOOD. SERVE LOVE.".
     * L2: Side Main Panel MUST BE IN ENGLISH: "Bharat Petroleum" (4200x900mm ACM sheet) with BPCL logo on left (text length 2700mm) and yellow/blue wave ribbons (Option 2B).
     * L3: Emergency Information Panel (EIP, 800x600mm) on left rear lower body with: "CORRECT TECHNICAL NAME: LIQUIFIED PETROLEUM GAS", "UN No. 1075", "HAZCHEM 2WE", Emergency dial (Police 100, Fire 101, Ambulance 102), Specialist Advice ("USE DRY CHEMICAL POWDER TYPE FIRE EXTINGUISHER"), Class 2 red diamond.
     * L4: Cylinder cage frame and clamps.
     * L5_UNAUTHORIZED_MARKINGS: Check for ANY extraneous paintings, commercial ads, private transporter slogans, or decals.
   - Right Side (Driver Side):
     * R1: "Bharatgas" sticker on driver cabin door (200x600mm) with Hindi "भारतगैस" and "बनाईये खाना. परोसिये प्यार.".
     * R2: Side Main Panel MUST BE IN HINDI: "भारत पेट्रोलियम" (4200x900mm ACM sheet) in Devanagari script (text length 2450mm) with BPCL logo and wave ribbons (Option 2B). AN ENGLISH PANEL ON THE RIGHT SIDE IS A CRITICAL VIOLATION.
     * R3: Emergency Information Panel (EIP, 800x600mm) with identical statutory hazmat text.
     * R4: Right cage frame.
     * R5_UNAUTHORIZED_MARKINGS: Check for ANY unauthorized text, religious symbols, private slogans or unapproved decals.
   - Rear / Back View (STRICT FULL DETECTION & OCR):
     * B1: 3rd Emergency Information Panel (EIP, 800x600mm) cladded onto rear mesh gate with exact statutory text.
     * B2: Class 2 Flammable Gas diamond (250x250mm) and red/white reflective tape across rear under-run protection bumper.
     * B3: Rear registration plate with functioning lamp.
     * B4: Rear gate mesh and locking latch.
     * B5_REAR_ALL_TEXT_AUDIT: Perform complete OCR and list EVERYTHING written, painted, or mounted on the rear view. Transcribe all words, numbers, and signs.
     * B6_UNAUTHORIZED_MARKINGS: Actively check for any non-BPCL slogans (e.g. "Horn OK Please", "Buri Nazar...", "Keep Distance", "Use Dipper At Night"), religious symbols, private phone numbers, or unapproved decals on rear gate or bumper. If present, flag as non-compliant!

2. DETECTION OF UNAUTHORIZED / EXTRA MARKINGS ACROSS ALL SIDES:
   In F6, L5, R5, and B6, state clearly what extraneous text, slogans, or symbols (if any) were seen, or confirm surface is clean and compliant.

Return your response strictly as valid JSON matching this schema:
{{
  "overall_status": "PASS" | "FAIL",
  "compliance_score": <int 0-100>,
  "summary": "<clear executive summary without any code formatting>",
  "critical_violations": ["<list of any critical violations preventing dispatch>"],
  "rear_text_detected": ["<list of every text item, slogan, or sign detected on the rear view>"],
  "unauthorized_markings_found": ["<list of any extraneous symbols, slogans, or unauthorized text found on any side>"],
  "quantities": {{
    "side_panels_detected": <int>,
    "eip_panels_detected": <int>,
    "cabin_stickers_detected": <int>
  }},
  "front_checks": [
    {{
      "id": "<rule id: F1_GOODS_CARRIER, F2_BP_FRONT_LOGO, F3_FRONT_CLASS_LABEL, F4_CABIN_LIVERY, F5_FRONT_NUMBER_PLATE, F6_UNAUTHORIZED_MARKINGS>",
      "name": "<rule name>",
      "status": "PASS" | "FAIL" | "WARNING",
      "confidence": <float 0.0 to 1.0>,
      "observation": "<detailed observation of what is visible on vehicle>",
      "corrective_action": "<none or specific remediation required>"
    }}
  ],
  "left_checks": [...],
  "right_checks": [...],
  "back_checks": [...]
}}
Do NOT output any markdown backticks (```json) around the JSON, return ONLY raw valid JSON.
"""

    contents = [
        "Photo 1 - Front View of Truck:", pil_to_part(front_img),
        "Photo 2 - Left Side (Helper Side) of Truck:", pil_to_part(left_img),
        "Photo 3 - Right Side (Driver Side) of Truck:", pil_to_part(right_img),
        "Photo 4 - Back / Rear View of Truck:", pil_to_part(back_img),
        prompt
    ]

    # Candidate models in priority order
    candidate_models = [model_name]
    for m in ["gemini-3.6-flash", "gemini-3.7-flash", "gemini-3.5-flash-lite"]:
        if m not in candidate_models:
            candidate_models.append(m)

    response = None
    last_err = None
    for candidate in candidate_models:
        try:
            response = client.models.generate_content(
                model=candidate,
                contents=contents,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.1
                )
            )
            if response and response.text:
                break
        except Exception as e:
            last_err = e
            err_msg = str(e).lower()
            if "not_found" in err_msg or "404" in err_msg or "no longer available" in err_msg:
                continue
            raise e

    if response is None or not response.text:
        raise RuntimeError(f"Gemini Vision API error: {str(last_err)}")

    try:
        text_content = response.text.strip()
        # Clean up any potential markdown formatting
        if text_content.startswith("```json"):
            text_content = text_content[7:]
        if text_content.startswith("```"):
            text_content = text_content[3:]
        if text_content.endswith("```"):
            text_content = text_content[:-3]
        
        result = json.loads(text_content.strip())
        return _enrich_checks_with_specs(result)
    except Exception as e:
        raise RuntimeError(f"Failed to parse Gemini Vision API response: {str(e)}\nRaw Response: {response.text[:200]}")


def generate_simulated_audit(scenario: str = "compliant") -> Dict[str, Any]:
    """
    Generates realistic simulated inspection data for demo and quick-testing purposes.
    scenarios: 'compliant', 'missing_eip_and_hindi', 'poor_condition'
    """
    if scenario == "compliant":
        res = {
            "overall_status": "PASS",
            "compliance_score": 96,
            "summary": "The vehicle fully complies with BPCL specifications. All 2 side panels (English on Left, Hindi on Right), 3 Emergency Information Panels (Left, Right, Rear), and cabin stickers are present, correctly oriented, and in excellent condition.",
            "critical_violations": [],
            "quantities": {
                "side_panels_detected": 2,
                "eip_panels_detected": 3,
                "cabin_stickers_detected": 2
            },
            "front_checks": [
                {
                    "id": "F1_GOODS_CARRIER",
                    "name": "'GOODS CARRIER' Sunshade Sticker",
                    "status": "PASS",
                    "confidence": 0.98,
                    "observation": "Crown sticker present with blue background, white lettering, and Class 2 red diamond in center.",
                    "corrective_action": "None required"
                },
                {
                    "id": "F2_BP_FRONT_LOGO",
                    "name": "'Bharat Petroleum' Front Logo",
                    "status": "PASS",
                    "confidence": 0.97,
                    "observation": "Standard BPCL emblem and 'Bharat Petroleum' lettering clearly visible below windshield.",
                    "corrective_action": "None required"
                },
                {
                    "id": "F3_FRONT_CLASS_LABEL",
                    "name": "Front Class 2 Flammable Gas Hazard Diamond",
                    "status": "PASS",
                    "confidence": 0.95,
                    "observation": "250mm x 250mm red flammable gas diamond present on front grille.",
                    "corrective_action": "None required"
                },
                {
                    "id": "F4_CABIN_LIVERY",
                    "name": "Cabin Color Scheme & Livery",
                    "status": "PASS",
                    "confidence": 0.94,
                    "observation": "Blue and white cabin color livery well maintained.",
                    "corrective_action": "None required"
                },
                {
                    "id": "F5_FRONT_NUMBER_PLATE",
                    "name": "Registration Number Plate (Front)",
                    "status": "PASS",
                    "confidence": 0.99,
                    "observation": "Front registration number plate clearly legible and secure.",
                    "corrective_action": "None required"
                },
                {
                    "id": "F6_UNAUTHORIZED_MARKINGS",
                    "name": "Extraneous / Unauthorized Signs, Symbols & Markings (Front)",
                    "status": "PASS",
                    "confidence": 0.97,
                    "observation": "Surface clean and compliant. No unauthorized stickers, religious symbols, or private slogans detected on windshield or cabin.",
                    "corrective_action": "None required"
                }
            ],
            "left_checks": [
                {
                    "id": "L1_BHARATGAS_CABIN",
                    "name": "'Bharatgas' Helper Cabin Door Sticker",
                    "status": "PASS",
                    "confidence": 0.96,
                    "observation": "Bharatgas logo sticker present on helper cabin door.",
                    "corrective_action": "None required"
                },
                {
                    "id": "L2_SIDE_PANEL_ENGLISH",
                    "name": "Side Main Panel in English ('Bharat Petroleum')",
                    "status": "PASS",
                    "confidence": 0.98,
                    "observation": "ACM panel 4200x900mm present with English text 'Bharat Petroleum', BPCL roundel, and wave borders.",
                    "corrective_action": "None required"
                },
                {
                    "id": "L3_LEFT_EIP_PANEL",
                    "name": "Emergency Information Panel (EIP) - Left Side",
                    "status": "PASS",
                    "confidence": 0.97,
                    "observation": "800x600mm EIP panel clearly displays UN 1075, HAZCHEM 2WE, and emergency contact numbers.",
                    "corrective_action": "None required"
                },
                {
                    "id": "L4_LEFT_CAGE_STRUCTURE",
                    "name": "Cylinder Cage & Locking Integrity",
                    "status": "PASS",
                    "confidence": 0.93,
                    "observation": "Cage framing undamaged and securely clamped.",
                    "corrective_action": "None required"
                },
                {
                    "id": "L5_UNAUTHORIZED_MARKINGS",
                    "name": "Extraneous / Unauthorized Signs, Symbols & Markings (Left Side)",
                    "status": "PASS",
                    "confidence": 0.96,
                    "observation": "No unauthorized commercial paintings, private slogans, or extraneous stickers on left body.",
                    "corrective_action": "None required"
                }
            ],
            "right_checks": [
                {
                    "id": "R1_BHARATGAS_CABIN",
                    "name": "'Bharatgas' Driver Cabin Door Sticker",
                    "status": "PASS",
                    "confidence": 0.95,
                    "observation": "Bharatgas Hindi logo sticker present on driver cabin door.",
                    "corrective_action": "None required"
                },
                {
                    "id": "R2_SIDE_PANEL_HINDI",
                    "name": "Side Main Panel in Hindi ('भारत पेट्रोलियम')",
                    "status": "PASS",
                    "confidence": 0.98,
                    "observation": "ACM panel present with Devanagari Hindi text 'भारत पेट्रोलियम' and wave design.",
                    "corrective_action": "None required"
                },
                {
                    "id": "R3_RIGHT_EIP_PANEL",
                    "name": "Emergency Information Panel (EIP) - Right Side",
                    "status": "PASS",
                    "confidence": 0.96,
                    "observation": "Right side EIP board present with UN 1075, HAZCHEM 2WE, and Class 2 label.",
                    "corrective_action": "None required"
                },
                {
                    "id": "R4_RIGHT_CAGE_STRUCTURE",
                    "name": "Right Cylinder Cage Frame",
                    "status": "PASS",
                    "confidence": 0.94,
                    "observation": "Right cage structure intact.",
                    "corrective_action": "None required"
                },
                {
                    "id": "R5_UNAUTHORIZED_MARKINGS",
                    "name": "Extraneous / Unauthorized Signs, Symbols & Markings (Right Side)",
                    "status": "PASS",
                    "confidence": 0.96,
                    "observation": "No unauthorized markings on right side or driver door.",
                    "corrective_action": "None required"
                }
            ],
            "back_checks": [
                {
                    "id": "B1_REAR_EIP_PANEL",
                    "name": "Rear Emergency Information Panel (EIP)",
                    "status": "PASS",
                    "confidence": 0.98,
                    "observation": "3rd EIP board mounted on rear mesh gate, all emergency contact details legible.",
                    "corrective_action": "None required"
                },
                {
                    "id": "B2_REAR_CLASS_LABEL_REFLECTORS",
                    "name": "Rear Class 2 Diamond & Safety Reflective Striping",
                    "status": "PASS",
                    "confidence": 0.95,
                    "observation": "Red/white reflective tape across rear under-run protection and Class 2 label intact.",
                    "corrective_action": "None required"
                },
                {
                    "id": "B3_REAR_NUMBER_PLATE",
                    "name": "Rear Vehicle Registration Plate",
                    "status": "PASS",
                    "confidence": 0.98,
                    "observation": "Rear license plate legible and properly mounted.",
                    "corrective_action": "None required"
                },
                {
                    "id": "B4_REAR_GATE_LOCKING",
                    "name": "Rear Gate Mesh & Locking Latches",
                    "status": "PASS",
                    "confidence": 0.94,
                    "observation": "Mesh gate securely locked and latch functional.",
                    "corrective_action": "None required"
                },
                {
                    "id": "B5_REAR_ALL_TEXT_AUDIT",
                    "name": "Rear View Full Text & Signage Detection",
                    "status": "PASS",
                    "confidence": 0.98,
                    "observation": "Detected statutory text: 'CORRECT TECHNICAL NAME: LIQUIFIED PETROLEUM GAS', 'UN No. 1075', 'HAZCHEM 2WE', emergency dial 100/101/102, 'SPECIALIST ADVICE: USE DRY CHEMICAL POWDER TYPE FIRE EXTINGUISHER', and registration plate. All text strictly adheres to BPCL document.",
                    "corrective_action": "None required"
                },
                {
                    "id": "B6_UNAUTHORIZED_MARKINGS",
                    "name": "Extraneous / Unauthorized Signs, Symbols & Markings (Rear Gate)",
                    "status": "PASS",
                    "confidence": 0.98,
                    "observation": "No unauthorized slogans ('Horn OK Please' etc.), private phone numbers, or religious decals detected on rear gate or bumper.",
                    "corrective_action": "None required"
                }
            ],
            "rear_text_detected": [
                "EIP Board: LIQUIFIED PETROLEUM GAS",
                "EIP Board: UN No. 1075 | HAZCHEM 2WE",
                "EIP Board: IN EMERGENCY DIAL: POLICE 100, FIRE 101, AMBULANCE 102",
                "EIP Board: SPECIALIST ADVICE: USE DRY CHEMICAL POWDER TYPE FIRE EXTINGUISHER",
                "Number Plate: MH 12 BP 1075"
            ],
            "unauthorized_markings_found": []
        }
    else:  # non-compliant / violations
        res = {
            "overall_status": "FAIL",
            "compliance_score": 52,
            "summary": "Vehicle FAILED compliance audit. Critical deficiencies: Rear Emergency Information Panel (EIP) is MISSING, Right side panel is in English instead of mandatory Hindi, unauthorized painted slogan 'Horn OK Please' and private contact numbers detected on rear, and front Class 2 diamond is damaged.",
            "critical_violations": [
                "Right Side Panel: Hindi text ('भारत पेट्रोलियम') is missing. Incorrect panel language used.",
                "Rear EIP Board Missing: Vehicle only has 2 of 3 required Emergency Information Panels.",
                "Rear Unauthorized Markings: 'Horn OK Please' painted slogan and private contact numbers detected on rear gate and bumper.",
                "Front Hazard Label: Peeling/damaged Class 2 Flammable Gas diamond."
            ],
            "quantities": {
                "side_panels_detected": 2,
                "eip_panels_detected": 2,
                "cabin_stickers_detected": 2
            },
            "front_checks": [
                {
                    "id": "F1_GOODS_CARRIER",
                    "name": "'GOODS CARRIER' Sunshade Sticker",
                    "status": "PASS",
                    "confidence": 0.95,
                    "observation": "Crown sticker present with blue background.",
                    "corrective_action": "None"
                },
                {
                    "id": "F2_BP_FRONT_LOGO",
                    "name": "'Bharat Petroleum' Front Logo",
                    "status": "PASS",
                    "confidence": 0.94,
                    "observation": "Logo present below windshield.",
                    "corrective_action": "None"
                },
                {
                    "id": "F3_FRONT_CLASS_LABEL",
                    "name": "Front Class 2 Flammable Gas Hazard Diamond",
                    "status": "FAIL",
                    "confidence": 0.92,
                    "observation": "Hazard diamond is torn/peeling off front grill.",
                    "corrective_action": "Replace with new 250x250mm Class 2 Flammable Gas sticker."
                },
                {
                    "id": "F4_CABIN_LIVERY",
                    "name": "Cabin Color Scheme & Livery",
                    "status": "PASS",
                    "confidence": 0.90,
                    "observation": "Standard blue/white paint visible.",
                    "corrective_action": "None"
                },
                {
                    "id": "F5_FRONT_NUMBER_PLATE",
                    "name": "Registration Number Plate (Front)",
                    "status": "PASS",
                    "confidence": 0.96,
                    "observation": "Front plate legible.",
                    "corrective_action": "None"
                },
                {
                    "id": "F6_UNAUTHORIZED_MARKINGS",
                    "name": "Extraneous / Unauthorized Signs, Symbols & Markings (Front)",
                    "status": "WARNING",
                    "confidence": 0.89,
                    "observation": "Detected unauthorized religious sticker on top-right corner of front windshield.",
                    "corrective_action": "Remove unauthorized sticker from windshield."
                }
            ],
            "left_checks": [
                {
                    "id": "L1_BHARATGAS_CABIN",
                    "name": "'Bharatgas' Helper Cabin Door Sticker",
                    "status": "PASS",
                    "confidence": 0.94,
                    "observation": "Cabin sticker present.",
                    "corrective_action": "None"
                },
                {
                    "id": "L2_SIDE_PANEL_ENGLISH",
                    "name": "Side Main Panel in English ('Bharat Petroleum')",
                    "status": "PASS",
                    "confidence": 0.97,
                    "observation": "English side panel correctly installed on helper side.",
                    "corrective_action": "None"
                },
                {
                    "id": "L3_LEFT_EIP_PANEL",
                    "name": "Emergency Information Panel (EIP) - Left Side",
                    "status": "PASS",
                    "confidence": 0.96,
                    "observation": "EIP panel present with UN 1075 and HAZCHEM 2WE.",
                    "corrective_action": "None"
                },
                {
                    "id": "L4_LEFT_CAGE_STRUCTURE",
                    "name": "Cylinder Cage & Locking Integrity",
                    "status": "PASS",
                    "confidence": 0.91,
                    "observation": "Cage bars secure.",
                    "corrective_action": "None"
                },
                {
                    "id": "L5_UNAUTHORIZED_MARKINGS",
                    "name": "Extraneous / Unauthorized Signs, Symbols & Markings (Left Side)",
                    "status": "PASS",
                    "confidence": 0.94,
                    "observation": "No extraneous markings on left side body.",
                    "corrective_action": "None"
                }
            ],
            "right_checks": [
                {
                    "id": "R1_BHARATGAS_CABIN",
                    "name": "'Bharatgas' Driver Cabin Door Sticker",
                    "status": "PASS",
                    "confidence": 0.93,
                    "observation": "Driver cabin sticker present.",
                    "corrective_action": "None"
                },
                {
                    "id": "R2_SIDE_PANEL_HINDI",
                    "name": "Side Main Panel in Hindi ('भारत पेट्रोलियम')",
                    "status": "FAIL",
                    "confidence": 0.98,
                    "observation": "CRITICAL VIOLATION: Right side panel has English text instead of mandatory Hindi ('भारत पेट्रोलियम') text.",
                    "corrective_action": "Replace right panel with Hindi vinyl cladded ACM sheet per specification."
                },
                {
                    "id": "R3_RIGHT_EIP_PANEL",
                    "name": "Emergency Information Panel (EIP) - Right Side",
                    "status": "PASS",
                    "confidence": 0.95,
                    "observation": "Right EIP panel present.",
                    "corrective_action": "None"
                },
                {
                    "id": "R4_RIGHT_CAGE_STRUCTURE",
                    "name": "Right Cylinder Cage Frame",
                    "status": "PASS",
                    "confidence": 0.92,
                    "observation": "Structure acceptable.",
                    "corrective_action": "None"
                },
                {
                    "id": "R5_UNAUTHORIZED_MARKINGS",
                    "name": "Extraneous / Unauthorized Signs, Symbols & Markings (Right Side)",
                    "status": "PASS",
                    "confidence": 0.93,
                    "observation": "No unauthorized text on right side.",
                    "corrective_action": "None"
                }
            ],
            "back_checks": [
                {
                    "id": "B1_REAR_EIP_PANEL",
                    "name": "Rear Emergency Information Panel (EIP)",
                    "status": "FAIL",
                    "confidence": 0.99,
                    "observation": "CRITICAL VIOLATION: Rear EIP board (800x600mm) is completely MISSING from rear mesh gate.",
                    "corrective_action": "Fabricate and rivet 800x600mm EIP panel (UN 1075, HAZCHEM 2WE, dial numbers) to rear gate before release."
                },
                {
                    "id": "B2_REAR_CLASS_LABEL_REFLECTORS",
                    "name": "Rear Class 2 Diamond & Safety Reflective Striping",
                    "status": "WARNING",
                    "confidence": 0.88,
                    "observation": "Reflective warning tape on rear bumper is partially faded and missing on right corner.",
                    "corrective_action": "Affix new high-intensity reflective tape."
                },
                {
                    "id": "B3_REAR_NUMBER_PLATE",
                    "name": "Rear Vehicle Registration Plate",
                    "status": "PASS",
                    "confidence": 0.96,
                    "observation": "Rear number plate visible.",
                    "corrective_action": "None"
                },
                {
                    "id": "B4_REAR_GATE_LOCKING",
                    "name": "Rear Gate Mesh & Locking Latches",
                    "status": "PASS",
                    "confidence": 0.93,
                    "observation": "Mesh latch secured.",
                    "corrective_action": "None"
                },
                {
                    "id": "B5_REAR_ALL_TEXT_AUDIT",
                    "name": "Rear View Full Text & Signage Detection",
                    "status": "FAIL",
                    "confidence": 0.97,
                    "observation": "Detected text: 'MH 12 BP 1075' on number plate, hand-painted slogan 'Horn OK Please' on bumper, and private mobile number '98XXXXXXXX' on rear gate frame. MANDATORY STATUTORY EIP BOARD TEXT IS MISSING.",
                    "corrective_action": "Install statutory EIP board with mandatory hazmat text and remove non-statutory words."
                },
                {
                    "id": "B6_UNAUTHORIZED_MARKINGS",
                    "name": "Extraneous / Unauthorized Signs, Symbols & Markings (Rear Gate)",
                    "status": "FAIL",
                    "confidence": 0.98,
                    "observation": "DEFECT: Detected unauthorized painted slogan 'Horn OK Please' across rear bumper and handwritten private phone number on rear mesh gate frame.",
                    "corrective_action": "Scrub and repaint bumper to remove 'Horn OK Please' slogan and remove private contact number."
                }
            ],
            "rear_text_detected": [
                "Registration Plate: MH 12 BP 1075",
                "Painted Slogan on Bumper: 'Horn OK Please' (UNAUTHORIZED)",
                "Handwritten Gate Marking: 'Transporter Contact: 98XXXXXXXX' (UNAUTHORIZED)",
                "NOTE: Statutory EIP Hazmat Board text is completely MISSING"
            ],
            "unauthorized_markings_found": [
                "Rear Bumper: Unauthorized painted slogan 'Horn OK Please'",
                "Rear Gate: Private contact number painting",
                "Front Windshield: Non-statutory religious decal"
            ]
        }
    return _enrich_checks_with_specs(res)
