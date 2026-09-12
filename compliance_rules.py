"""
LPG Packed Truck Compliance Rules and Specifications
Based on: Guidelines and Specifications for LPG Packed Truck Panels and Stickers
(Bharat Petroleum / Bharatgas LPG Packed Trucks - 306 & 450 Cylinders)
"""

from typing import Dict, List, Any

# Standard Dimensions and Specifications
PANEL_SPECS = {
    "acm_sheet": "3 mm thick, coated both sides with 0.25 mm Aluminium skin (Make: Viva / Alucobond / Mitsubishi)",
    "ms_stiffener": "35 mm x 35 mm x 3 mm MS angle",
    "ms_slotted_angle": "40 mm x 40 mm x 3 mm pre-painted ONE SIDE slotted angle",
    "ms_u_clamp": "M10 U clamp, 120 mm length, M10 locknut + 1 mm washer",
    "vinyl_grade": "Superior grade opaque/clear cast vinyl for gasoline resistance, 5-year guarantee",
    "side_panel_dimensions": "4200 mm x 900 mm",
    "eip_dimensions": "800 mm x 600 mm",
    "goods_carrier_dimensions": "310 mm x 1490 mm",
    "bp_logo_front_dimensions": "160 mm x 1300 mm",
    "class_label_front_dimensions": "250 mm x 250 mm",
    "cabin_bharatgas_dimensions": "200 mm x 600 mm"
}

# Quantity Audit Targets
REQUIRED_QUANTITIES = {
    "side_panels": {
        "count": 2,
        "description": "2 nos. Side Panels: Left Side in English ('Bharat Petroleum'), Right Side in Hindi ('भारत पेट्रोलियम')"
    },
    "eip_panels": {
        "count": 3,
        "description": "3 nos. Emergency Information Panels (EIP): Left Side, Right Side, and Rear / Back"
    },
    "cabin_stickers": {
        "count": 2,
        "description": "2 nos. 'Bharatgas' Logo Stickers (1 on Left cabin door, 1 on Right cabin door)"
    },
    "front_branding": {
        "count": 3,
        "description": "'GOODS CARRIER' crown, 'Bharat Petroleum' front sticker, Class 2 Hazard Label diamond"
    }
}

# Detailed Checklists per Angle
COMPLIANCE_CHECKLIST: Dict[str, List[Dict[str, Any]]] = {
    "front": [
        {
            "id": "F1_GOODS_CARRIER",
            "name": "'GOODS CARRIER' Sunshade Sticker",
            "spec": "Size 310 mm x 1490 mm, royal blue background, bold white lettering 'GOODS CARRIER' with Class 2 Flammable Gas red diamond in center.",
            "critical": True,
            "keywords": ["GOODS CARRIER", "2"],
            "element": "Sunshade / Top Crown Sticker"
        },
        {
            "id": "F2_BP_FRONT_LOGO",
            "name": "'Bharat Petroleum' Front Logo",
            "spec": "Size 160 mm x 1300 mm, blue 'Bharat Petroleum' lettering with standard BPCL circular emblem, placed below windshield / upper cabin grill.",
            "critical": True,
            "keywords": ["Bharat Petroleum"],
            "element": "Front Cabin Face Logo"
        },
        {
            "id": "F3_FRONT_CLASS_LABEL",
            "name": "Front Class 2 Flammable Gas Hazard Diamond",
            "spec": "Size 250 mm x 250 mm, red diamond sticker with white flame symbol and numeral '2' at bottom, affixed on front grill/bumper area.",
            "critical": True,
            "keywords": ["2"],
            "element": "Class 2 Hazard Diamond"
        },
        {
            "id": "F4_CABIN_LIVERY",
            "name": "Cabin Color Scheme & Livery",
            "spec": "Standard blue and white cabin finish matching BPCL standards, in clean and undamaged condition.",
            "critical": False,
            "keywords": ["Blue", "White"],
            "element": "Cabin Livery"
        },
        {
            "id": "F5_FRONT_NUMBER_PLATE",
            "name": "Registration Number Plate (Front)",
            "spec": "Official high security / legible vehicle registration number plate mounted securely on front bumper.",
            "critical": True,
            "keywords": [],
            "element": "Front License Plate"
        }
    ],
    "left": [
        {
            "id": "L1_BHARATGAS_CABIN",
            "name": "'Bharatgas' Helper Cabin Door Sticker",
            "spec": "Size 200 mm x 600 mm printed vinyl sticker with Bharatgas logo and 'COOK FOOD. SERVE LOVE.' tagline on helper side cabin door.",
            "critical": True,
            "keywords": ["Bharatgas"],
            "element": "Helper Cabin Door Sticker"
        },
        {
            "id": "L2_SIDE_PANEL_ENGLISH",
            "name": "Side Main Panel in English ('Bharat Petroleum')",
            "spec": "Size 4200 mm x 900 mm ACM board cladded with staggered pop rivets. Features BPCL roundel on left, blue English text 'Bharat Petroleum', and top/bottom yellow-blue wave ribbons (Option 2B).",
            "critical": True,
            "keywords": ["Bharat Petroleum"],
            "element": "Left Side ACM Panel (English)"
        },
        {
            "id": "L3_LEFT_EIP_PANEL",
            "name": "Emergency Information Panel (EIP) - Left Side",
            "spec": "Size 800 mm x 600 mm metal board mounted on rear lower section of left body. MUST display: 'CORRECT TECHNICAL NAME: LIQUIFIED PETROLEUM GAS', 'UN No. 1075', 'HAZCHEM 2WE', Emergency dial (POLICE: 100, FIRE: 101, AMBULANCE: 102), Specialist Advice ('USE DRY CHEMICAL POWDER TYPE FIRE EXTINGUISHER'), and Class 2 Flammable Gas red diamond.",
            "critical": True,
            "keywords": ["LIQUIFIED PETROLEUM GAS", "1075", "2WE", "100", "101", "102", "DRY CHEMICAL POWDER", "2"],
            "element": "Left Side EIP Board"
        },
        {
            "id": "L4_LEFT_CAGE_STRUCTURE",
            "name": "Cylinder Cage & Locking Integrity",
            "spec": "Standard blue/white horizontal slotted cage frame for cylinder containment, clamped securely with M10 U-clamps.",
            "critical": False,
            "keywords": [],
            "element": "Cage Frame and Clamps"
        }
    ],
    "right": [
        {
            "id": "R1_BHARATGAS_CABIN",
            "name": "'Bharatgas' Driver Cabin Door Sticker",
            "spec": "Size 200 mm x 600 mm printed vinyl sticker with Bharatgas Hindi logo 'भारतगैस' and 'बनाईये खाना. परोसिये प्यार.' on driver cabin door.",
            "critical": True,
            "keywords": ["भारतगैस", "Bharatgas"],
            "element": "Driver Cabin Door Sticker"
        },
        {
            "id": "R2_SIDE_PANEL_HINDI",
            "name": "Side Main Panel in Hindi ('भारत पेट्रोलियम')",
            "spec": "Size 4200 mm x 900 mm ACM board cladded with staggered pop rivets. Features Devanagari Hindi text 'भारत पेट्रोलियम' in blue with BPCL emblem, and top/bottom yellow-blue wave ribbons (Option 2B).",
            "critical": True,
            "keywords": ["भारत पेट्रोलियम"],
            "element": "Right Side ACM Panel (Hindi)"
        },
        {
            "id": "R3_RIGHT_EIP_PANEL",
            "name": "Emergency Information Panel (EIP) - Right Side",
            "spec": "Size 800 mm x 600 mm metal board mounted on right side. Mandatory: UN 1075, HAZCHEM 2WE, 'LIQUIFIED PETROLEUM GAS', Emergency dial numbers (100, 101, 102), Specialist Advice, and Class 2 red diamond.",
            "critical": True,
            "keywords": ["LIQUIFIED PETROLEUM GAS", "1075", "2WE", "100", "101", "102", "2"],
            "element": "Right Side EIP Board"
        },
        {
            "id": "R4_RIGHT_CAGE_STRUCTURE",
            "name": "Right Cylinder Cage Frame",
            "spec": "Properly painted and maintained cylinder containment cage bars without physical structural damage.",
            "critical": False,
            "keywords": [],
            "element": "Cage Frame"
        }
    ],
    "back": [
        {
            "id": "B1_REAR_EIP_PANEL",
            "name": "Rear Emergency Information Panel (EIP)",
            "spec": "Size 800 mm x 600 mm board cladded onto rear mesh gate. Must contain: 'CORRECT TECHNICAL NAME: LIQUIFIED PETROLEUM GAS', 'UN No. 1075', 'HAZCHEM 2WE', 'IN EMERGENCY DIAL: POLICE : 100 FIRE : 101 AMBULANCE : 102', 'SPECIALIST ADVICE: USE DRY CHEMICAL POWDER TYPE FIRE EXTINGUISHER', and Class 2 Flammable Gas red diamond.",
            "critical": True,
            "keywords": ["LIQUIFIED PETROLEUM GAS", "1075", "2WE", "100", "101", "102", "DRY CHEMICAL POWDER", "2"],
            "element": "Rear Gate EIP Board"
        },
        {
            "id": "B2_REAR_CLASS_LABEL_REFLECTORS",
            "name": "Rear Class 2 Diamond & Safety Reflective Striping",
            "spec": "Class 2 Flammable Gas diamond (integrated or separate 250x250mm) and high-visibility reflective red/white warning tape on rear under-run protection / bumper.",
            "critical": True,
            "keywords": ["2"],
            "element": "Rear Safety Diamond & Reflectors"
        },
        {
            "id": "B3_REAR_NUMBER_PLATE",
            "name": "Rear Vehicle Registration Plate",
            "spec": "Clearly legible registration plate affixed on rear bumper with functioning illumination lamp.",
            "critical": True,
            "keywords": [],
            "element": "Rear License Plate"
        },
        {
            "id": "B4_REAR_GATE_LOCKING",
            "name": "Rear Gate Mesh & Locking Latches",
            "spec": "Sturdy mesh frame with functional locking mechanism to ensure cylinder load cannot be displaced or opened in transit.",
            "critical": True,
            "keywords": [],
            "element": "Rear Mesh Gate"
        }
    ]
}

# Quick lookup mapping by rule ID for instant specification retrieval
RULE_SPECS: Dict[str, Dict[str, Any]] = {
    rule["id"]: rule
    for rules in COMPLIANCE_CHECKLIST.values()
    for rule in rules
}
