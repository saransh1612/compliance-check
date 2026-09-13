"""
LPG Packed Truck Compliance Check Application
Streamlit Web Application for Bharat Petroleum / Bharatgas LPG Packed Truck Inspection
Supports: English, Hindi (हिंदी), and Bengali (বাংলা)
"""

import os
import streamlit as st
from PIL import Image, ImageOps
from datetime import datetime

def load_and_fix_orientation(file_obj):
    """Opens image and automatically corrects orientation using EXIF data (e.g., from phones)."""
    img = Image.open(file_obj)
    try:
        img = ImageOps.exif_transpose(img)
    except Exception:
        pass
    return img

# Set page config
st.set_page_config(
    page_title="BPCL LPG Truck Compliance Audit",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

from compliance_rules import COMPLIANCE_CHECKLIST, REQUIRED_QUANTITIES, PANEL_SPECS, RULE_SPECS
from vision_checker import run_gemini_vision_audit, generate_simulated_audit, build_manual_audit, GENAI_AVAILABLE
from report_generator import generate_html_report
from translations import UI_TEXT, SIDE_METADATA, RULE_TRANSLATIONS, get_ui_text, localize_item

# Language Selector in Sidebar
st.sidebar.markdown("### 🌐 भाषा / Language / ভাষা")
lang_options = ["हिंदी (Hindi)", "English", "বাংলা (Bengali)"]
selected_lang_str = st.sidebar.selectbox(
    "Choose Language / भाषा चुनें",
    options=lang_options,
    index=0,
    label_visibility="collapsed"
)
lang = "hi" if "हिंदी" in selected_lang_str else ("bn" if "বাংলা" in selected_lang_str else "en")
st.session_state.lang = lang

# Custom CSS for BPCL professional styling
st.markdown("""
<style>
    :root {
        --bpcl-blue: #003399;
        --bpcl-yellow: #FFCC00;
        --bpcl-dark: #0f172a;
    }
    .main-header {
        background: linear-gradient(135deg, #003399 0%, #001f5c 100%);
        padding: 22px 28px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
        border-bottom: 5px solid #FFCC00;
        box-shadow: 0 4px 12px rgba(0, 51, 153, 0.15);
    }
    .main-header h1 {
        color: white !important;
        margin: 0;
        font-size: 26px;
        font-weight: 800;
        letter-spacing: -0.3px;
    }
    .main-header p {
        color: #e2e8f0 !important;
        margin: 6px 0 0 0;
        font-size: 14px;
    }
    .metric-card {
        background: white;
        padding: 14px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        text-align: center;
    }
    .metric-card .num {
        font-size: 26px;
        font-weight: 800;
    }
    .metric-card .lbl {
        font-size: 12px;
        color: #64748b;
        text-transform: uppercase;
        font-weight: 600;
        margin-top: 2px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 6px 6px 0 0;
        padding: 10px 18px;
        font-weight: 700;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown(f"""
<div class="main-header">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
        <div>
            <h1>🚛 {get_ui_text('app_title', lang)}</h1>
            <p>{get_ui_text('app_subtitle', lang)}</p>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 8px 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.3); text-align: right;">
            <div style="font-size: 11px; text-transform: uppercase; color: #FFCC00; font-weight: bold;">BPCL Standard</div>
            <div style="font-size: 13px; font-weight: 600;">EIP & ACM Panels v2.0</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.markdown(f"### 📋 {get_ui_text('quick_audit', lang)}")
truck_no = st.sidebar.text_input(get_ui_text("truck_no", lang), value="MH 12 BP 1075")
truck_capacity = st.sidebar.selectbox(get_ui_text("truck_cap", lang), ["306 Cylinders", "450 Cylinders"])
plant_name = st.sidebar.text_input(get_ui_text("plant_name", lang), value="BPCL Uran LPG Plant")
transporter_name = st.sidebar.text_input(get_ui_text("transporter", lang), value="Mahalaxmi Transport Corp")
auditor_name = st.sidebar.text_input(get_ui_text("auditor", lang), value="Inspector R. K. Sharma")

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ Inspection Engine")

engine_mode = st.sidebar.radio(
    "Inspection Mode",
    [
        "🤖 Gemini Multimodal Vision AI",
        "🧪 Demo / Simulated Test Case",
        "✍️ Manual Auditor Checklist"
    ],
    index=1 if not os.environ.get("GEMINI_API_KEY") else 0
)

api_key = ""
if engine_mode == "🤖 Gemini Multimodal Vision AI":
    default_key = os.environ.get("GEMINI_API_KEY", "")
    api_key = st.sidebar.text_input(
        "Google Gemini API Key",
        value=default_key,
        type="password",
        help="Get a 100% free API key from Google AI Studio (https://aistudio.google.com)"
    )
    model_choice = st.sidebar.selectbox("Gemini Model", ["gemini-3.6-flash", "gemini-3.7-flash", "gemini-3.5-flash-lite"], index=0)
    
    st.sidebar.markdown("""
    <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:12px; border-radius:8px; font-size:12px; margin-top:8px;">
        <strong style="color:#1d4ed8;">🔑 Get a 100% Free Gemini API Key:</strong>
        <ol style="padding-left:18px; margin:6px 0 0 0;">
            <li>Visit <a href="https://aistudio.google.com" target="_blank" style="font-weight:bold; color:#1d4ed8;">aistudio.google.com</a></li>
            <li>Sign in with your Google account</li>
            <li>Click <strong>"Get API key"</strong> ➔ <strong>"Create API key"</strong></li>
            <li>Paste it above (no credit card required!)</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

demo_scenario = "compliant"
if engine_mode == "🧪 Demo / Simulated Test Case":
    demo_scenario = st.sidebar.selectbox(
        "Select Demo Scenario",
        [
            ("compliant", "✅ 100% Compliant Truck (All Panels & Stickers OK)"),
            ("missing_eip_and_hindi", "❌ Defective Truck (Missing Rear EIP & Hindi Panel)"),
        ],
        format_func=lambda x: x[1]
    )[0]

# Quick Reference Sidebar Accordion
with st.sidebar.expander("📖 View BPCL Specification Summary"):
    st.markdown(f"""
    **Standard Dimensions:**
    - **Side Panels**: {PANEL_SPECS['side_panel_dimensions']} (ACM sheet)
    - **EIP Panels**: {PANEL_SPECS['eip_dimensions']} (3 nos. total)
    - **GOODS CARRIER**: {PANEL_SPECS['goods_carrier_dimensions']}
    - **Bharatgas Cabin**: {PANEL_SPECS['cabin_bharatgas_dimensions']}
    - **Class 2 Diamond**: {PANEL_SPECS['class_label_front_dimensions']}
    """)

# Session State Initialization
for key in ["front_img", "left_img", "right_img", "back_img",
            "front_file_id", "left_file_id", "right_file_id", "back_file_id"]:
    if key not in st.session_state:
        st.session_state[key] = None

if "audit_results" not in st.session_state:
    st.session_state.audit_results = None

# Sample Photos and Clear Buttons Row
samples_dir = os.path.join(os.path.dirname(__file__), "samples")
col_load1, col_load2 = st.columns([3, 7])
with col_load1:
    if st.button(get_ui_text("load_sample_btn", lang), use_container_width=True, type="secondary"):
        try:
            st.session_state.front_img = Image.open(os.path.join(samples_dir, "sample_front.jpg"))
            st.session_state.left_img = Image.open(os.path.join(samples_dir, "sample_left.jpg"))
            st.session_state.right_img = Image.open(os.path.join(samples_dir, "sample_right.jpg"))
            st.session_state.back_img = Image.open(os.path.join(samples_dir, "sample_back.jpg"))
            st.session_state.front_file_id = "sample_front"
            st.session_state.left_file_id = "sample_left"
            st.session_state.right_file_id = "sample_right"
            st.session_state.back_file_id = "sample_back"
            st.success("Loaded all 4 sample test photos!")
            st.rerun()
        except Exception as e:
            st.error(f"Could not load samples: {e}")

with col_load2:
    if st.button(get_ui_text("clear_photos_btn", lang), type="secondary"):
        st.session_state.front_img = None
        st.session_state.left_img = None
        st.session_state.right_img = None
        st.session_state.back_img = None
        st.session_state.front_file_id = None
        st.session_state.left_file_id = None
        st.session_state.right_file_id = None
        st.session_state.back_file_id = None
        st.session_state.audit_results = None
        st.rerun()

st.markdown(f"### 📸 {get_ui_text('photo_upload_title', lang)}")
col1, col2, col3, col4 = st.columns(4)

# 1. Front View
with col1:
    st.markdown(f"**1. {get_ui_text('photo_front', lang)}**")
    st.caption(get_ui_text("photo_front_sub", lang))
    front_file = st.file_uploader("Front Photo", type=["jpg", "jpeg", "png", "webp"], key="upload_front", label_visibility="collapsed")
    if front_file:
        fid = f"{front_file.name}_{front_file.size}"
        if st.session_state.front_file_id != fid:
            st.session_state.front_file_id = fid
            st.session_state.front_img = load_and_fix_orientation(front_file)
            
    if st.session_state.front_img:
        st.image(st.session_state.front_img, caption="Front View Loaded", use_container_width=True)
        rc1, rc2 = st.columns(2)
        with rc1:
            if st.button(get_ui_text("rotate_left", lang), key="rot_l_front", use_container_width=True):
                st.session_state.front_img = st.session_state.front_img.rotate(90, expand=True)
                st.rerun()
        with rc2:
            if st.button(get_ui_text("rotate_right", lang), key="rot_r_front", use_container_width=True):
                st.session_state.front_img = st.session_state.front_img.rotate(-90, expand=True)
                st.rerun()

# 2. Left View
with col2:
    st.markdown(f"**2. {get_ui_text('photo_left', lang)}**")
    st.caption(get_ui_text("photo_left_sub", lang))
    left_file = st.file_uploader("Left Photo", type=["jpg", "jpeg", "png", "webp"], key="upload_left", label_visibility="collapsed")
    if left_file:
        fid = f"{left_file.name}_{left_file.size}"
        if st.session_state.left_file_id != fid:
            st.session_state.left_file_id = fid
            st.session_state.left_img = load_and_fix_orientation(left_file)
            
    if st.session_state.left_img:
        st.image(st.session_state.left_img, caption="Left Side Loaded", use_container_width=True)
        rc1, rc2 = st.columns(2)
        with rc1:
            if st.button(get_ui_text("rotate_left", lang), key="rot_l_left", use_container_width=True):
                st.session_state.left_img = st.session_state.left_img.rotate(90, expand=True)
                st.rerun()
        with rc2:
            if st.button(get_ui_text("rotate_right", lang), key="rot_r_left", use_container_width=True):
                st.session_state.left_img = st.session_state.left_img.rotate(-90, expand=True)
                st.rerun()

# 3. Right View
with col3:
    st.markdown(f"**3. {get_ui_text('photo_right', lang)}**")
    st.caption(get_ui_text("photo_right_sub", lang))
    right_file = st.file_uploader("Right Photo", type=["jpg", "jpeg", "png", "webp"], key="upload_right", label_visibility="collapsed")
    if right_file:
        fid = f"{right_file.name}_{right_file.size}"
        if st.session_state.right_file_id != fid:
            st.session_state.right_file_id = fid
            st.session_state.right_img = load_and_fix_orientation(right_file)
            
    if st.session_state.right_img:
        st.image(st.session_state.right_img, caption="Right Side Loaded", use_container_width=True)
        rc1, rc2 = st.columns(2)
        with rc1:
            if st.button(get_ui_text("rotate_left", lang), key="rot_l_right", use_container_width=True):
                st.session_state.right_img = st.session_state.right_img.rotate(90, expand=True)
                st.rerun()
        with rc2:
            if st.button(get_ui_text("rotate_right", lang), key="rot_r_right", use_container_width=True):
                st.session_state.right_img = st.session_state.right_img.rotate(-90, expand=True)
                st.rerun()

# 4. Back View
with col4:
    st.markdown(f"**4. {get_ui_text('photo_back', lang)}**")
    st.caption(get_ui_text("photo_back_sub", lang))
    back_file = st.file_uploader("Back Photo", type=["jpg", "jpeg", "png", "webp"], key="upload_back", label_visibility="collapsed")
    if back_file:
        fid = f"{back_file.name}_{back_file.size}"
        if st.session_state.back_file_id != fid:
            st.session_state.back_file_id = fid
            st.session_state.back_img = load_and_fix_orientation(back_file)
            
    if st.session_state.back_img:
        st.image(st.session_state.back_img, caption="Rear Gate Loaded", use_container_width=True)
        rc1, rc2 = st.columns(2)
        with rc1:
            if st.button(get_ui_text("rotate_left", lang), key="rot_l_back", use_container_width=True):
                st.session_state.back_img = st.session_state.back_img.rotate(90, expand=True)
                st.rerun()
        with rc2:
            if st.button(get_ui_text("rotate_right", lang), key="rot_r_back", use_container_width=True):
                st.session_state.back_img = st.session_state.back_img.rotate(-90, expand=True)
                st.rerun()

# Manual Checklist Mode handling
checklist_responses = {}
if engine_mode == "✍️ Manual Auditor Checklist":
    with st.expander("📝 Guided Auditor Inspection Checklist", expanded=True):
        st.caption("Inspect the 4 photos loaded above and confirm status per BPCL specifications:")
        t1, t2, t3, t4 = st.tabs([
            SIDE_METADATA["front"]["names"].get(lang, "Front"),
            SIDE_METADATA["left"]["names"].get(lang, "Left"),
            SIDE_METADATA["right"]["names"].get(lang, "Right"),
            SIDE_METADATA["back"]["names"].get(lang, "Back")
        ])
        
        for tab_obj, sec_key in [(t1, "front"), (t2, "left"), (t3, "right"), (t4, "back")]:
            with tab_obj:
                for rule in COMPLIANCE_CHECKLIST[sec_key]:
                    loc_r = localize_item(rule, lang=lang)
                    c1, c2 = st.columns([7, 3])
                    with c1:
                        st.write(f"**{loc_r['name']}**")
                        st.caption(loc_r['what_is_correct'])
                    with c2:
                        st_val = st.radio(
                            f"Status for {rule['id']}",
                            ["PASS", "FAIL", "WARNING"],
                            key=f"manual_{rule['id']}",
                            horizontal=True,
                            label_visibility="collapsed"
                        )
                        checklist_responses[rule['id']] = {
                            "status": st_val,
                            "observation": "Complies with BPCL specification" if st_val == "PASS" else loc_r['what_is_wrong'],
                            "action": "None required" if st_val == "PASS" else loc_r['action']
                        }

st.markdown("<br>", unsafe_allow_html=True)

# Run Compliance Check Button
col_btn, col_help = st.columns([3, 7])
with col_btn:
    run_check = st.button(f"🔍 {get_ui_text('run_audit_btn', lang)}", type="primary", use_container_width=True)

all_photos_uploaded = (
    st.session_state.front_img is not None and
    st.session_state.left_img is not None and
    st.session_state.right_img is not None and
    st.session_state.back_img is not None
)

if run_check:
    if not all_photos_uploaded:
        st.error("⚠️ Please provide all 4 photos (Front, Left, Right, and Back) before initiating compliance audit.")
    else:
        with st.spinner("Analyzing all 4 angles against Bharat Petroleum specifications..."):
            try:
                if engine_mode == "🤖 Gemini Multimodal Vision AI":
                    if not api_key:
                        st.error("Please enter a valid Google Gemini API key or switch to Demo mode.")
                    else:
                        results = run_gemini_vision_audit(
                            front_img=st.session_state.front_img,
                            back_img=st.session_state.back_img,
                            left_img=st.session_state.left_img,
                            right_img=st.session_state.right_img,
                            api_key=api_key,
                            model_name=model_choice
                        )
                        st.session_state.audit_results = results
                elif engine_mode == "🧪 Demo / Simulated Test Case":
                    results = generate_simulated_audit(scenario=demo_scenario)
                    st.session_state.audit_results = results
                else:  # Manual Auditor Mode
                    results = build_manual_audit(checklist_responses)
                    st.session_state.audit_results = results
                
                st.success("✅ Audit analysis completed successfully!")
            except Exception as e:
                st.error(f"Audit failed: {str(e)}")


def render_html_clean(html_content: str):
    """Renders HTML directly without markdown code-block artifacts."""
    if hasattr(st, "html"):
        st.html(html_content)
    else:
        unindented = "\n".join(line.lstrip() for line in html_content.splitlines())
        st.markdown(unindented, unsafe_allow_html=True)


def render_checklist_html_table(items: list, current_lang: str, show_side: bool = True) -> str:
    """
    Renders the direct visual checklist table with:
    - Truck Side badge with icon
    - Inspection Item (clean typography, no code blocks)
    - Clear green tick mark ✅ (PASS) or red cross ❌ (FAIL)
    - Column: ✅ What is Correct (Required Standard)
    - Column: ❌ What is Wrong (Observed Defect & Remediation)
    """
    if not items:
        no_items_msg = get_ui_text("no_items_filter", current_lang)
        return f'<div style="text-align:center; padding:24px; color:#64748b; background:#f8fafc; border-radius:8px; border:1px dashed #cbd5e1;">{no_items_msg}</div>'

    col_side = get_ui_text("col_side", current_lang)
    col_item = get_ui_text("col_item", current_lang)
    col_status = get_ui_text("col_status", current_lang)
    col_correct = get_ui_text("col_correct", current_lang)
    col_wrong = get_ui_text("col_wrong", current_lang)

    side_th = f'<th style="width:13%; padding:14px; text-align:left; border-right:1px solid #1e3a8a;">{col_side}</th>' if show_side else ''

    lines = [
        '<div style="overflow-x:auto; width:100%; margin-top:12px; margin-bottom:20px;">',
        '<table style="width:100%; border-collapse:collapse; font-family:-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif; background:#ffffff; border:1px solid #cbd5e1; border-radius:10px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.06);">',
        '<thead>',
        '<tr style="background:#003399; color:#ffffff; font-size:13px; text-transform:uppercase; letter-spacing:0.5px;">',
        side_th,
        f'<th style="width:{"21%" if show_side else "25%"}; padding:14px; text-align:left; border-right:1px solid #1e3a8a;">{col_item}</th>',
        f'<th style="width:{"13%" if show_side else "14%"}; padding:14px; text-align:center; border-right:1px solid #1e3a8a;">{col_status}</th>',
        f'<th style="width:{"26%" if show_side else "30%"}; padding:14px; text-align:left; background:#002673; border-right:1px solid #1e3a8a;">{col_correct}</th>',
        f'<th style="width:{"27%" if show_side else "31%"}; padding:14px; text-align:left; background:#001a4e;">{col_wrong}</th>',
        '</tr>',
        '</thead>',
        '<tbody>'
    ]

    for item in items:
        loc = localize_item(item, lang=current_lang)
        status = loc["status"]
        row_bg = "#fff9f9" if status == "FAIL" else ("#fffdf7" if status == "WARNING" else "#ffffff")

        side_td = ""
        if show_side:
            side_td = f'<td style="padding:14px; vertical-align:top; border-right:1px solid #f1f5f9; border-bottom:1px solid #e2e8f0;"><span style="background:{loc["side_badge_bg"]}; color:{loc["side_badge_fg"]}; padding:5px 10px; border-radius:6px; font-weight:700; font-size:12px; display:inline-block; white-space:nowrap;">{loc["side_icon"]} {loc["side_short"]}</span></td>'

        if status == "PASS":
            wrong_content = f'<div style="color:#166534; font-size:13px; font-weight:600; line-height:1.45;">{loc["what_is_wrong"]}</div>'
            wrong_bg = "#f0fdf4"
            wrong_border = "#bbf7d0"
        elif status == "WARNING":
            wrong_content = f'<div style="color:#92400e; font-size:13px; font-weight:700; line-height:1.45;">⚠️ {loc["what_is_wrong"]}</div><div style="margin-top:6px; font-size:12px; color:#1e40af; background:#e0f2fe; padding:5px 8px; border-radius:4px; border-left:3px solid #0284c7;"><strong>🔧 {get_ui_text("remediation_label", current_lang)}</strong> {loc["action"]}</div>'
            wrong_bg = "#fffbeb"
            wrong_border = "#fde68a"
        else:
            wrong_content = f'<div style="color:#991b1b; font-size:13px; font-weight:700; line-height:1.45;">❌ {loc["what_is_wrong"]}</div><div style="margin-top:6px; font-size:12px; color:#b91c1c; background:#fee2e2; padding:6px 10px; border-radius:4px; border-left:3px solid #ef4444;"><strong>🔧 {get_ui_text("remediation_label", current_lang)}</strong> {loc["action"]}</div>'
            wrong_bg = "#fef2f2"
            wrong_border = "#fecaca"

        lines.extend([
            f'<tr style="background:{row_bg}; border-bottom:1px solid #e2e8f0;">',
            side_td,
            f'<td style="padding:14px; vertical-align:top; border-right:1px solid #f1f5f9; border-bottom:1px solid #e2e8f0;"><div style="font-weight:700; color:#0f172a; font-size:14px; line-height:1.35;">{loc["name"]}</div></td>',
            f'<td style="padding:14px; vertical-align:top; text-align:center; border-right:1px solid #f1f5f9; border-bottom:1px solid #e2e8f0;">{loc["status_badge_html"]}</td>',
            f'<td style="padding:14px; vertical-align:top; background:#f0fdf4; border-right:1px solid #bbf7d0; border-left:3px solid #10b981; border-bottom:1px solid #e2e8f0; font-size:13px; color:#14532d; line-height:1.45;">{loc["what_is_correct"]}</td>',
            f'<td style="padding:14px; vertical-align:top; background:{wrong_bg}; border-left:3px solid {wrong_border}; border-bottom:1px solid #e2e8f0;">{wrong_content}</td>',
            '</tr>'
        ])

    lines.extend([
        '</tbody>',
        '</table>',
        '</div>'
    ])
    return "\n".join(lines)


def render_rear_text_table(rear_texts: list, lang: str) -> str:
    """Renders a dedicated table displaying all text detected on the rear view."""
    if not rear_texts:
        return ""
    
    title = "🔍 पीछे लिखी सभी लिखावट एवं चिन्हों की सूची (Rear View Written Text Readout)" if lang == "hi" else (
        "🔍 পেছনের সম্পূর্ণ লেখা ও চিহ্নের তালিকা (Rear View Text Readout)" if lang == "bn" else
        "🔍 Rear View Full Text & Signage Detection Inventory"
    )

    lines = [
        '<div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:16px; margin-top:20px; margin-bottom:20px;">',
        f'<h4 style="margin-top:0; margin-bottom:12px; color:#003399; font-size:15px; font-weight:800;">{title}</h4>',
        '<div style="overflow-x:auto;">',
        '<table style="width:100%; border-collapse:collapse; background:#ffffff; border:1px solid #e2e8f0; font-size:13px;">',
        '<thead>',
        '<tr style="background:#0284c7; color:#ffffff; font-size:12px; text-transform:uppercase;">',
        '<th style="padding:10px; width:8%; text-align:center;">#</th>',
        '<th style="padding:10px; width:52%; text-align:left;">' + ("पहचानी गई लिखावट / चिन्ह (Detected Text)" if lang == "hi" else ("সনাক্তকৃত লেখা বা প্রতীক" if lang == "bn" else "Detected Text / Sign")) + '</th>',
        '<th style="padding:10px; width:40%; text-align:left;">' + ("बीपीसीएल मानक स्थिति (Compliance Classification)" if lang == "hi" else ("বিপিসিএল মান্যতা শ্রেণীবিভাগ" if lang == "bn" else "Compliance Classification")) + '</th>',
        '</tr>',
        '</thead>',
        '<tbody>'
    ]

    for idx, txt in enumerate(rear_texts, 1):
        is_statutory = any(k in txt.upper() for k in ["EIP", "UN", "1075", "HAZCHEM", "2WE", "POLICE", "100", "FIRE", "101", "AMBULANCE", "102", "DRY CHEMICAL", "PLATE"])
        is_unauth = any(k in txt.upper() for k in ["HORN", "PLEASE", "BURI NAZAR", "DIPPER", "UNAUTHORIZED", "CONTACT", "MOBILE", "PHONE"])

        if is_unauth:
            badge = '<span style="background:#fee2e2; color:#991b1b; padding:4px 8px; border-radius:4px; font-weight:bold; font-size:11px;">❌ गैर-मानक / अनधिकृत (Non-BPCL)</span>' if lang == "hi" else (
                '<span style="background:#fee2e2; color:#991b1b; padding:4px 8px; border-radius:4px; font-weight:bold; font-size:11px;">❌ অননুমোদিত লেখা (Non-BPCL)</span>' if lang == "bn" else
                '<span style="background:#fee2e2; color:#991b1b; padding:4px 8px; border-radius:4px; font-weight:bold; font-size:11px;">❌ Unauthorized / Non-BPCL</span>'
            )
            row_bg = "#fff5f5"
        elif is_statutory:
            badge = '<span style="background:#dcfce7; color:#166534; padding:4px 8px; border-radius:4px; font-weight:bold; font-size:11px;">✅ वैधानिक मानक (Statutory BPCL)</span>' if lang == "hi" else (
                '<span style="background:#dcfce7; color:#166534; padding:4px 8px; border-radius:4px; font-weight:bold; font-size:11px;">✅ সংবিধিবদ্ধ তথ্য (Statutory BPCL)</span>' if lang == "bn" else
                '<span style="background:#dcfce7; color:#166534; padding:4px 8px; border-radius:4px; font-weight:bold; font-size:11px;">✅ Mandatory Statutory BPCL</span>'
            )
            row_bg = "#ffffff"
        else:
            badge = '<span style="background:#f1f5f9; color:#475569; padding:4px 8px; border-radius:4px; font-weight:bold; font-size:11px;">ℹ️ अन्य लिखावट (Other Text)</span>'
            row_bg = "#ffffff"

        lines.extend([
            f'<tr style="background:{row_bg}; border-bottom:1px solid #e2e8f0;">',
            f'<td style="padding:10px; text-align:center; font-weight:bold; color:#64748b;">{idx}</td>',
            f'<td style="padding:10px; font-weight:600; color:#0f172a;">{txt}</td>',
            f'<td style="padding:10px;">{badge}</td>',
            '</tr>'
        ])

    lines.extend([
        '</tbody>',
        '</table>',
        '</div>',
        '</div>'
    ])
    return "\n".join(lines)


def render_unauthorized_markings_table(markings: list, lang: str) -> str:
    """Renders a dedicated warning table for unauthorized/extraneous symbols, signs, or slogans."""
    if not markings:
        return ""
    
    title = "⚠️ गाड़ी पर पाए गए गैर-मानक चिन्ह, नारे व स्टीकर (Unauthorized Markings Detected)" if lang == "hi" else (
        "⚠️ গাড়িতে সনাক্ত অননুমোদিত চিহ্ন, স্লোগান ও স্টিকার (Unauthorized Markings Detected)" if lang == "bn" else
        "⚠️ Extraneous / Unauthorized Markings & Slogans Detected on Vehicle"
    )

    lines = [
        '<div style="background:#fef2f2; border:2px solid #ef4444; border-radius:10px; padding:16px; margin-top:20px; margin-bottom:20px;">',
        f'<h4 style="margin-top:0; margin-bottom:12px; color:#991b1b; font-size:15px; font-weight:800;">{title}</h4>',
        '<div style="overflow-x:auto;">',
        '<table style="width:100%; border-collapse:collapse; background:#ffffff; border:1px solid #fecaca; font-size:13px;">',
        '<thead>',
        '<tr style="background:#dc2626; color:#ffffff; font-size:12px; text-transform:uppercase;">',
        '<th style="padding:10px; width:8%; text-align:center;">#</th>',
        '<th style="padding:10px; width:46%; text-align:left;">' + ("पहचाना गया गैर-मानक चिन्ह / लिखावट" if lang == "hi" else ("সনাক্তকৃত অননুমোদিত চিহ্ন বা লেখা" if lang == "bn" else "Detected Non-Compliant Marking")) + '</th>',
        '<th style="padding:10px; width:46%; text-align:left;">' + ("बीपीसीएल नियम एवं आवश्यक सुधार" if lang == "hi" else ("বিপিসিএল নিয়ম ও প্রতিকার" if lang == "bn" else "BPCL Rule & Remediation Action")) + '</th>',
        '</tr>',
        '</thead>',
        '<tbody>'
    ]

    for idx, mark in enumerate(markings, 1):
        rule_desc = (
            "बीपीसीएल नियमों अनुसार किसी भी प्रकार के धार्मिक चिन्ह, निजी नारे ('Horn OK Please' आदि), या फोन नंबर वर्जित हैं। इन्हें तुरंत खुरचकर या पेंट कर हटाएं।" if lang == "hi" else (
                "বিপিসিএল নিয়ম অনুযায়ী কোনো ধর্মীয় প্রতীক, ব্যক্তিগত স্লোগান ('Horn OK Please' ইত্যাদি) বা ফোন নম্বর লেখা সম্পূর্ণ নিষিদ্ধ। অবিলম্বে মুছে ফেলুন।" if lang == "bn" else
                "BPCL fleet standards strictly prohibit unauthorized slogans ('Horn OK Please' etc.), religious symbols, or private adverts. Scrub or repaint surface immediately."
            )
        )
        lines.extend([
            '<tr style="border-bottom:1px solid #fecaca; background:#fff9f9;">',
            f'<td style="padding:10px; text-align:center; font-weight:bold; color:#dc2626;">{idx}</td>',
            f'<td style="padding:10px; font-weight:700; color:#991b1b;">❌ {mark}</td>',
            f'<td style="padding:10px; color:#475569; line-height:1.4;">{rule_desc}</td>',
            '</tr>'
        ])

    lines.extend([
        '</tbody>',
        '</table>',
        '</div>',
        '</div>'
    ])
    return "\n".join(lines)


# Display Results Section
if st.session_state.audit_results:
    data = st.session_state.audit_results
    is_pass = data.get("overall_status") == "PASS"
    score = data.get("compliance_score", 0)
    violations = data.get("critical_violations", [])
    quantities = data.get("quantities", {})
    rear_texts = data.get("rear_text_detected", [])
    unauth_marks = data.get("unauthorized_markings_found", [])

    st.markdown("---")
    st.markdown(f"## 📊 {get_ui_text('audit_results_title', lang)}")

    # Overall Status Banner
    if is_pass:
        render_html_clean(f"""
        <div style="background:#dcfce7; border:2px solid #16a34a; border-radius:10px; padding:18px 24px; text-align:center; color:#14532d; margin-bottom:16px;">
            <div style="font-size:22px; font-weight:800; letter-spacing:0.3px;">✅ {get_ui_text('status_pass', lang)}</div>
            <div style="font-size:14px; margin-top:4px; color:#166534;">{get_ui_text('status_pass_desc', lang)} | {get_ui_text('score_label', lang)}: <strong>{score}%</strong></div>
        </div>
        """)
    else:
        render_html_clean(f"""
        <div style="background:#fee2e2; border:2px solid #dc2626; border-radius:10px; padding:18px 24px; text-align:center; color:#7f1d1d; margin-bottom:16px;">
            <div style="font-size:22px; font-weight:800; letter-spacing:0.3px;">❌ {get_ui_text('status_fail', lang)}</div>
            <div style="font-size:14px; margin-top:4px; color:#991b1b;">{get_ui_text('status_fail_desc', lang)} | {get_ui_text('score_label', lang)}: <strong>{score}%</strong></div>
        </div>
        """)

    # All items consolidated
    all_checks = []
    for sec in ["front_checks", "left_checks", "right_checks", "back_checks"]:
        all_checks.extend(data.get(sec, []))

    total_count = len(all_checks)
    pass_count = sum(1 for c in all_checks if c.get("status") == "PASS")
    defect_count = sum(1 for c in all_checks if c.get("status") in ["FAIL", "WARNING"])

    # Key Metrics Row
    m1, m2, m3, m4, m5 = st.columns(5)
    with m1:
        render_html_clean(f"""
        <div class="metric-card">
            <div class="num" style="color: {'#10b981' if score>=85 else '#ef4444'};">{score}%</div>
            <div class="lbl">{get_ui_text('score_label', lang)}</div>
        </div>
        """)
    with m2:
        render_html_clean(f"""
        <div class="metric-card">
            <div class="num" style="color: #0284c7;">{total_count}</div>
            <div class="lbl">{get_ui_text('total_items', lang)}</div>
        </div>
        """)
    with m3:
        render_html_clean(f"""
        <div class="metric-card">
            <div class="num" style="color: #10b981;">{pass_count}</div>
            <div class="lbl">{get_ui_text('passed_items', lang)}</div>
        </div>
        """)
    with m4:
        render_html_clean(f"""
        <div class="metric-card">
            <div class="num" style="color: {'#ef4444' if defect_count > 0 else '#10b981'};">{defect_count}</div>
            <div class="lbl">{get_ui_text('failed_items', lang)}</div>
        </div>
        """)
    with m5:
        side_p = quantities.get("side_panels_detected", 2)
        render_html_clean(f"""
        <div class="metric-card">
            <div class="num" style="color: {'#10b981' if side_p==2 else '#ef4444'};">{side_p} / 2</div>
            <div class="lbl">ACM Panels</div>
        </div>
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    # Navigation Tabs
    tab_master, tab_front, tab_left, tab_right, tab_back, tab_report = st.tabs([
        get_ui_text("nav_table_tab", lang),
        get_ui_text("nav_front_tab", lang),
        get_ui_text("nav_left_tab", lang),
        get_ui_text("nav_right_tab", lang),
        get_ui_text("nav_back_tab", lang),
        get_ui_text("nav_cert_tab", lang)
    ])

    # Tab 1: Master Checklist Table (With Side & Status Navigation)
    with tab_master:
        st.markdown(f"### 📋 {get_ui_text('audit_results_title', lang)}")
        
        col_nav1, col_nav2 = st.columns([6, 4])
        with col_nav1:
            side_options = [
                ("all", f"🌐 {get_ui_text('all_sides', lang)}"),
                ("front", f"🚛 {get_ui_text('front_side', lang)}"),
                ("left", f"◀️ {get_ui_text('left_side', lang)}"),
                ("right", f"▶️ {get_ui_text('right_side', lang)}"),
                ("back", f"🔙 {get_ui_text('back_side', lang)}")
            ]
            selected_side_key = st.radio(
                "गाड़ी की दिशा (Truck Side):",
                options=[s[0] for s in side_options],
                format_func=lambda k: next(s[1] for s in side_options if s[0] == k),
                horizontal=True,
                key="filter_side_master"
            )
        with col_nav2:
            status_options = [
                ("all", get_ui_text("filter_all", lang)),
                ("defects", get_ui_text("filter_defects_only", lang)),
                ("correct", get_ui_text("filter_correct_only", lang))
            ]
            selected_status_filter = st.radio(
                "फिल्टर (Filter):",
                options=[s[0] for s in status_options],
                format_func=lambda k: next(s[1] for s in status_options if s[0] == k),
                horizontal=True,
                key="filter_status_master"
            )

        # Apply Filters
        filtered_items = all_checks
        if selected_side_key != "all":
            filtered_items = [item for item in filtered_items if item.get("side") == selected_side_key]

        if selected_status_filter == "defects":
            filtered_items = [item for item in filtered_items if item.get("status") in ["FAIL", "WARNING"]]
        elif selected_status_filter == "correct":
            filtered_items = [item for item in filtered_items if item.get("status") == "PASS"]

        # Render the Master Table (Clean Table Format - No Code Boxes)
        table_html = render_checklist_html_table(filtered_items, current_lang=lang, show_side=(selected_side_key == "all"))
        render_html_clean(table_html)

        # Show Unauthorized Markings Table if detected
        if unauth_marks:
            unauth_html = render_unauthorized_markings_table(unauth_marks, lang)
            render_html_clean(unauth_html)

        # Show Rear View Complete Text Readout
        if rear_texts:
            rear_tbl_html = render_rear_text_table(rear_texts, lang)
            render_html_clean(rear_tbl_html)

    # Tab 2: Front View
    with tab_front:
        st.markdown(f"### 🚛 {SIDE_METADATA['front']['names'].get(lang, 'Front View')}")
        col_img, col_tbl = st.columns([3, 7])
        with col_img:
            if st.session_state.front_img:
                st.image(st.session_state.front_img, caption="Front Photo", use_container_width=True)
            else:
                st.info("No front photo uploaded")
        with col_tbl:
            tbl_front = render_checklist_html_table(data.get("front_checks", []), current_lang=lang, show_side=False)
            render_html_clean(tbl_front)

    # Tab 3: Left Side
    with tab_left:
        st.markdown(f"### ◀️ {SIDE_METADATA['left']['names'].get(lang, 'Left Side')}")
        col_img, col_tbl = st.columns([3, 7])
        with col_img:
            if st.session_state.left_img:
                st.image(st.session_state.left_img, caption="Left (Helper) Photo", use_container_width=True)
            else:
                st.info("No left photo uploaded")
        with col_tbl:
            tbl_left = render_checklist_html_table(data.get("left_checks", []), current_lang=lang, show_side=False)
            render_html_clean(tbl_left)

    # Tab 4: Right Side
    with tab_right:
        st.markdown(f"### ▶️ {SIDE_METADATA['right']['names'].get(lang, 'Right Side')}")
        col_img, col_tbl = st.columns([3, 7])
        with col_img:
            if st.session_state.right_img:
                st.image(st.session_state.right_img, caption="Right (Driver) Photo", use_container_width=True)
            else:
                st.info("No right photo uploaded")
        with col_tbl:
            tbl_right = render_checklist_html_table(data.get("right_checks", []), current_lang=lang, show_side=False)
            render_html_clean(tbl_right)

    # Tab 5: Rear Gate
    with tab_back:
        st.markdown(f"### 🔙 {SIDE_METADATA['back']['names'].get(lang, 'Rear Gate')}")
        col_img, col_tbl = st.columns([3, 7])
        with col_img:
            if st.session_state.back_img:
                st.image(st.session_state.back_img, caption="Rear Gate Photo", use_container_width=True)
            else:
                st.info("No back photo uploaded")
        with col_tbl:
            tbl_back = render_checklist_html_table(data.get("back_checks", []), current_lang=lang, show_side=False)
            render_html_clean(tbl_back)
            if rear_texts:
                rear_tbl_html = render_rear_text_table(rear_texts, lang)
                render_html_clean(rear_tbl_html)

    # Tab 6: Official Certificate & Print
    with tab_report:
        st.markdown(f"### 📄 {get_ui_text('nav_cert_tab', lang)}")
        metadata_dict = {
            "truck_no": truck_no,
            "plant": plant_name,
            "transporter": transporter_name,
            "auditor": auditor_name,
            "capacity": truck_capacity,
            "timestamp": datetime.now().strftime("%d-%b-%Y %I:%M %p")
        }
        
        report_html = generate_html_report(
            inspection_data=data,
            metadata=metadata_dict,
            front_img=st.session_state.front_img,
            back_img=st.session_state.back_img,
            left_img=st.session_state.left_img,
            right_img=st.session_state.right_img,
            lang=lang
        )

        col_dl1, col_dl2 = st.columns([3, 7])
        with col_dl1:
            st.download_button(
                label=get_ui_text("download_cert", lang),
                data=report_html,
                file_name=f"BPCL_Compliance_{truck_no.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.html",
                mime="text/html",
                type="primary",
                use_container_width=True
            )
        
        st.components.v1.html(report_html, height=800, scrolling=True)

else:
    render_html_clean("""
    <div style="text-align: center; padding: 40px; color: #64748b; background: #f8fafc; border-radius: 10px; border: 1px dashed #cbd5e1;">
        <div style="font-size: 40px; margin-bottom: 10px;">🚛</div>
        <div style="font-size: 16px; font-weight: 600;">No active inspection running</div>
        <div style="font-size: 13px;">Upload 4 photos above or click <strong>'Load All 4 Sample Photos'</strong> to start.</div>
    </div>
    """)
