"""
Compliance Report Generator
Generates self-contained, printable HTML and PDF-ready audit certificates
for LPG Packed Truck Compliance Inspections.
"""

import base64
import io
from datetime import datetime
from typing import Dict, Any, Optional
from PIL import Image


def image_to_base64(img: Image.Image) -> str:
    """Converts a PIL Image to a base64 data URI string."""
    buffered = io.BytesIO()
    # Convert RGBA to RGB if needed for JPEG or save as PNG
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(buffered, format="JPEG", quality=85)
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{img_str}"


from translations import localize_item, get_ui_text

def generate_html_report(
    inspection_data: Dict[str, Any],
    metadata: Dict[str, str],
    front_img: Optional[Image.Image] = None,
    back_img: Optional[Image.Image] = None,
    left_img: Optional[Image.Image] = None,
    right_img: Optional[Image.Image] = None,
    lang: str = "en"
) -> str:
    """
    Generates a complete standalone HTML compliance audit certificate.
    Supports English (en), Hindi (hi), and Bengali (bn).
    """
    is_pass = inspection_data.get("overall_status") == "PASS"
    score = inspection_data.get("compliance_score", 0)
    summary = inspection_data.get("summary", "")
    critical_violations = inspection_data.get("critical_violations", [])
    
    timestamp = metadata.get("timestamp", datetime.now().strftime("%d-%b-%Y %I:%M %p"))
    truck_no = metadata.get("truck_no", "XX 00 XX 0000").upper()
    transporter = metadata.get("transporter", "Authorized LPG Transporter")
    plant = metadata.get("plant", "LPG Bottling Plant")
    auditor = metadata.get("auditor", "Safety Inspector")
    capacity = metadata.get("capacity", "306 Cylinders")

    # Encode images if provided
    front_b64 = image_to_base64(front_img) if front_img else ""
    back_b64 = image_to_base64(back_img) if back_img else ""
    left_b64 = image_to_base64(left_img) if left_img else ""
    right_b64 = image_to_base64(right_img) if right_img else ""

    # Build table rows
    def render_rows(checks: list) -> str:
        rows_html = ""
        for c in checks:
            loc = localize_item(c, lang=lang)
            status = loc["status"]
            if status == "PASS":
                badge = f'<span class="badge badge-pass">✅ {loc["status_label"]}</span>'
                wrong_html = f'<div style="color:#059669; font-weight:600;">{loc["what_is_wrong"]}</div>'
            elif status == "WARNING":
                badge = f'<span class="badge badge-warn">⚠️ {loc["status_label"]}</span>'
                wrong_html = f'<div style="color:#b45309; font-weight:700;">⚠️ {loc["what_is_wrong"]}</div>'
            else:
                badge = f'<span class="badge badge-fail">❌ {loc["status_label"]}</span>'
                wrong_html = f'<div style="color:#b91c1c; font-weight:700; background:#fef2f2; padding:6px 8px; border-radius:4px; border-left:3px solid #ef4444;">❌ {loc["what_is_wrong"]}</div>'
            
            action_html = ""
            if status != "PASS" and loc["action"] and loc["action"].lower() not in ["none", "none required", "कोई सुधार आवश्यक नहीं", "কোনো সংশোধনের প্রয়োজন নেই"]:
                action_html = f'<div style="color:#1e40af; font-size:11px; margin-top:4px; background:#eff6ff; padding:4px 6px; border-radius:4px;"><strong>🔧 {get_ui_text("remediation_label", lang)}</strong> {loc["action"]}</div>'
            
            rows_html += f"""
            <tr>
                <td style="font-weight:700; color:#0f172a;">
                    {loc['name']}
                </td>
                <td style="text-align:center; vertical-align:middle;">{badge}</td>
                <td style="color:#14532d; background:#f0fdf4; font-size:12px; line-height:1.45; border-left:2px solid #10b981;">
                    {loc['what_is_correct']}
                </td>
                <td style="font-size:12px; line-height:1.45;">
                    {wrong_html}
                    {action_html}
                </td>
            </tr>
            """
        return rows_html

    front_rows = render_rows(inspection_data.get("front_checks", []))
    back_rows = render_rows(inspection_data.get("back_checks", []))
    left_rows = render_rows(inspection_data.get("left_checks", []))
    right_rows = render_rows(inspection_data.get("right_checks", []))

    quantities = inspection_data.get("quantities", {})
    side_panels = quantities.get("side_panels_detected", 2)
    eip_panels = quantities.get("eip_panels_detected", 3)
    cabin_stickers = quantities.get("cabin_stickers_detected", 2)

    status_theme_color = "#10b981" if is_pass else "#ef4444"
    status_title = "VEHICLE COMPLIANT — APPROVED FOR DISPATCH" if is_pass else "VEHICLE NON-COMPLIANT — DISPATCH PROHIBITED"

    violations_html = ""
    if critical_violations:
        violations_html = """
        <div class="violations-box">
            <h3>⚠️ Critical Defects Preventing Dispatch:</h3>
            <ul>
        """
        for v in critical_violations:
            violations_html += f"<li><strong>{v}</strong></li>"
        violations_html += "</ul></div>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BPCL LPG Packed Truck Compliance Certificate - {truck_no}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #f8fafc;
            color: #1e293b;
            margin: 0;
            padding: 24px;
        }}
        .certificate-container {{
            max-width: 960px;
            margin: 0 auto;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            padding: 32px;
        }}
        .header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 3px solid #003399;
            padding-bottom: 20px;
            margin-bottom: 24px;
        }}
        .header-title h1 {{
            margin: 0;
            color: #003399;
            font-size: 22px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .header-title h2 {{
            margin: 4px 0 0 0;
            color: #475569;
            font-size: 14px;
            font-weight: 500;
        }}
        .stamp-box {{
            border: 3px solid {status_theme_color};
            color: {status_theme_color};
            font-weight: 800;
            text-align: center;
            padding: 10px 18px;
            border-radius: 8px;
            font-size: 16px;
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
        .meta-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            background: #f1f5f9;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 24px;
        }}
        .meta-item label {{
            display: block;
            font-size: 11px;
            color: #64748b;
            text-transform: uppercase;
            font-weight: 600;
        }}
        .meta-item value {{
            display: block;
            font-size: 14px;
            color: #0f172a;
            font-weight: 700;
            margin-top: 2px;
        }}
        .photos-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 24px;
        }}
        .photo-card {{
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            overflow: hidden;
            background: #fafafa;
            text-align: center;
        }}
        .photo-card img {{
            width: 100%;
            height: 140px;
            object-fit: cover;
            display: block;
        }}
        .photo-card .label {{
            padding: 6px;
            font-size: 11px;
            font-weight: bold;
            background: #003399;
            color: #fff;
        }}
        .summary-box {{
            background: #f8fafc;
            border-left: 4px solid {status_theme_color};
            padding: 14px 18px;
            border-radius: 4px;
            margin-bottom: 24px;
        }}
        .summary-box p {{
            margin: 0;
            font-size: 14px;
            line-height: 1.5;
        }}
        .violations-box {{
            background: #fef2f2;
            border: 1px solid #fecaca;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 24px;
            color: #991b1b;
        }}
        .violations-box h3 {{
            margin-top: 0;
            font-size: 15px;
        }}
        .violations-box ul {{
            margin-bottom: 0;
            padding-left: 20px;
        }}
        .section-title {{
            font-size: 15px;
            font-weight: bold;
            color: #003399;
            margin: 20px 0 10px 0;
            display: flex;
            align-items: center;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 6px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
            margin-bottom: 16px;
        }}
        th {{
            background: #f1f5f9;
            color: #334155;
            font-weight: 600;
            text-align: left;
            padding: 8px 10px;
            border: 1px solid #e2e8f0;
        }}
        td {{
            padding: 8px 10px;
            border: 1px solid #e2e8f0;
            vertical-align: top;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            font-size: 11px;
            font-weight: bold;
            border-radius: 4px;
        }}
        .badge-pass {{
            background: #d1fae5;
            color: #065f46;
        }}
        .badge-fail {{
            background: #fee2e2;
            color: #991b1b;
        }}
        .badge-warn {{
            background: #fef3c7;
            color: #92400e;
        }}
        .quantity-card {{
            display: flex;
            gap: 20px;
            background: #eef2ff;
            padding: 12px 18px;
            border-radius: 8px;
            margin-bottom: 24px;
            font-size: 13px;
        }}
        .quantity-item {{
            flex: 1;
        }}
        .quantity-item strong {{
            color: #1e3a8a;
        }}
        .footer-signatures {{
            display: flex;
            justify-content: space-between;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px dashed #cbd5e1;
            font-size: 12px;
            gap: 16px;
        }}
        .sig-block {{
            text-align: center;
            flex: 1;
        }}
        .sig-line {{
            border-bottom: 1px solid #475569;
            margin-bottom: 6px;
            height: 40px;
        }}
        @media print {{
            body {{ padding: 0; background: #fff; }}
            .certificate-container {{ border: none; box-shadow: none; padding: 0; }}
            .no-print {{ display: none; }}
        }}
    </style>
</head>
<body>
    <div class="certificate-container">
        <div class="no-print" style="margin-bottom: 16px; text-align: right;">
            <button onclick="window.print()" style="background:#003399; color:white; border:none; padding:8px 18px; border-radius:6px; cursor:pointer; font-weight:bold;">🖨️ Print / Save as PDF</button>
        </div>

        <div class="header">
            <div class="header-title">
                <h1>Bharat Petroleum Corporation Limited</h1>
                <h2>LPG Packed Truck Compliance & Safety Inspection Certificate</h2>
            </div>
            <div class="stamp-box">
                {status_title.split('—')[0].strip()}<br>
                <span style="font-size:24px;">{score}%</span>
            </div>
        </div>

        <div class="meta-grid">
            <div class="meta-item">
                <label>Vehicle Reg. Number</label>
                <value>{truck_no}</value>
            </div>
            <div class="meta-item">
                <label>LPG Bottling Plant</label>
                <value>{plant}</value>
            </div>
            <div class="meta-item">
                <label>Capacity Variant</label>
                <value>{capacity}</value>
            </div>
            <div class="meta-item">
                <label>Inspection Date & Time</label>
                <value>{timestamp}</value>
            </div>
            <div class="meta-item">
                <label>Transporter Name</label>
                <value>{transporter}</value>
            </div>
            <div class="meta-item">
                <label>Inspecting Officer</label>
                <value>{auditor}</value>
            </div>
            <div class="meta-item">
                <label>Compliance Status</label>
                <value style="color:{status_theme_color}; font-weight:800;">{inspection_data.get('overall_status', 'FAIL')}</value>
            </div>
            <div class="meta-item">
                <label>Score</label>
                <value>{score} / 100</value>
            </div>
        </div>

        {violations_html}

        <div class="summary-box">
            <p><strong>Executive Audit Summary:</strong> {summary}</p>
        </div>

        <div class="photos-grid">
            <div class="photo-card">
                <div class="label">1. FRONT VIEW</div>
                <img src="{front_b64 if front_b64 else 'https://via.placeholder.com/300x200?text=Front+View'}" alt="Front View">
            </div>
            <div class="photo-card">
                <div class="label">2. LEFT (HELPER)</div>
                <img src="{left_b64 if left_b64 else 'https://via.placeholder.com/300x200?text=Left+View'}" alt="Left View">
            </div>
            <div class="photo-card">
                <div class="label">3. RIGHT (DRIVER)</div>
                <img src="{right_b64 if right_b64 else 'https://via.placeholder.com/300x200?text=Right+View'}" alt="Right View">
            </div>
            <div class="photo-card">
                <div class="label">4. REAR / BACK</div>
                <img src="{back_b64 if back_b64 else 'https://via.placeholder.com/300x200?text=Back+View'}" alt="Back View">
            </div>
        </div>

        <div class="quantity-card">
            <div class="quantity-item">
                <strong>Side Panels (4200x900mm):</strong> {side_panels} / 2 (1 English, 1 Hindi)
            </div>
            <div class="quantity-item">
                <strong>EIP Panels (800x600mm):</strong> {eip_panels} / 3 (Left, Right, Rear)
            </div>
            <div class="quantity-item">
                <strong>Bharatgas Stickers (200x600mm):</strong> {cabin_stickers} / 2 (Left & Right Doors)
            </div>
        </div>

        <div class="section-title">1. Front Cabin & Face Inspection (आगे का भाग / সামনের দৃশ্য)</div>
        <table>
            <thead>
                <tr>
                    <th style="width:22%;">Specification Item</th>
                    <th style="width:14%; text-align:center;">Status</th>
                    <th style="width:32%;">✅ Required Standard (What is Correct)</th>
                    <th style="width:32%;">❌ Observed Defect (What is Wrong)</th>
                </tr>
            </thead>
            <tbody>
                {front_rows}
            </tbody>
        </table>

        <div class="section-title">2. Left Side (Helper Side) Inspection — English Panel (बायां भाग / বাম পাশ)</div>
        <table>
            <thead>
                <tr>
                    <th style="width:22%;">Specification Item</th>
                    <th style="width:14%; text-align:center;">Status</th>
                    <th style="width:32%;">✅ Required Standard (What is Correct)</th>
                    <th style="width:32%;">❌ Observed Defect (What is Wrong)</th>
                </tr>
            </thead>
            <tbody>
                {left_rows}
            </tbody>
        </table>

        <div class="section-title">3. Right Side (Driver Side) Inspection — Hindi Panel (दायां भाग / ডান পাশ)</div>
        <table>
            <thead>
                <tr>
                    <th style="width:22%;">Specification Item</th>
                    <th style="width:14%; text-align:center;">Status</th>
                    <th style="width:32%;">✅ Required Standard (What is Correct)</th>
                    <th style="width:32%;">❌ Observed Defect (What is Wrong)</th>
                </tr>
            </thead>
            <tbody>
                {right_rows}
            </tbody>
        </table>

        <div class="section-title">4. Rear / Back Gate Inspection (पीछे का गेट / পেছনের গেট)</div>
        <table>
            <thead>
                <tr>
                    <th style="width:22%;">Specification Item</th>
                    <th style="width:14%; text-align:center;">Status</th>
                    <th style="width:32%;">✅ Required Standard (What is Correct)</th>
                    <th style="width:32%;">❌ Observed Defect (What is Wrong)</th>
                </tr>
            </thead>
            <tbody>
                {back_rows}
            </tbody>
        </table>

        <div class="footer-signatures">
            <div class="sig-block">
                <div class="sig-line"></div>
                <strong style="font-size:14px; color:#0f172a;">Driver</strong><br>
                <span style="color:#64748b; font-size:11px;">(गाड़ी चालक / চালক)</span>
            </div>
            <div class="sig-block">
                <div class="sig-line"></div>
                <strong style="font-size:14px; color:#0f172a;">Inspector</strong><br>
                <span style="color:#64748b; font-size:11px;">(निरीक्षक / পরিদর্শক)</span>
            </div>
            <div class="sig-block">
                <div class="sig-line"></div>
                <strong style="font-size:14px; color:#0f172a;">Officer</strong><br>
                <span style="color:#64748b; font-size:11px;">(अधिकारी / কর্মকর্তা)</span>
            </div>
            <div class="sig-block">
                <div class="sig-line"></div>
                <strong style="font-size:14px; color:#0f172a;">Munshi</strong><br>
                <span style="color:#64748b; font-size:11px;">(मुंशी / মুন্সী)</span>
            </div>
        </div>
    </div>
</body>
</html>
"""
    return html
