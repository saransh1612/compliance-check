# Bharat Petroleum LPG Packed Truck Compliance Inspector 🚛

A dedicated compliance verification web application for **LPG Packed Cylinder Trucks (306 & 450 Cylinders)** based on official **Bharat Petroleum Corporation Limited (BPCL)** Guidelines and Specifications for Panels and Stickers.

---

## 📌 Features

- **4-Angle Dedicated Inspection**:
  - **Front View**: Validates "GOODS CARRIER" crown (310x1490mm) with Class 2 diamond, "Bharat Petroleum" front logo (160x1300mm), Class 2 hazard label (250x250mm), and registration plate.
  - **Left View (Helper Side)**: Validates helper cabin "Bharatgas" sticker, English "Bharat Petroleum" ACM panel (4200x900mm) with wave pattern, and Left Emergency Information Panel (EIP, 800x600mm with UN 1075, HAZCHEM 2WE).
  - **Right View (Driver Side)**: Validates driver cabin "भारतगैस" sticker, Hindi "भारत पेट्रोलियम" ACM panel (4200x900mm), and Right EIP board.
  - **Back / Rear View**: Validates the mandatory 3rd EIP board mounted on rear mesh gate, Class 2 flammable diamond, safety reflective striping across rear bumper, and rear license plate.
- **Quantity Validation**:
  - Automatically verifies that all 7 primary panels/stickers are accounted for:
    - 2 Side Panels (1 English, 1 Hindi)
    - 3 EIP Boards (Left, Right, Rear)
    - 2 Cabin Stickers (Left, Right)
- **Inspection Modes**:
  - **Gemini Multimodal Vision AI**: Automated computer vision inspection using Google Gemini (`gemini-2.5-flash`).
  - **Demo & Simulated Test Mode**: Test compliant and non-compliant scenarios instantly without needing real trucks or API keys.
  - **Auditor Mode**: Manual checklist inspection for on-site plant safety officers.
- **Export & Reporting**:
  - Standalone, self-contained HTML compliance certificate with embedded image thumbnails.
  - One-click print / save to PDF for audit logging and dispatch clearance.

---

## 🚀 How to Run

### Option 1: Double-Click Launcher
Simply double-click `run_app.bat` in this folder.

### Option 2: Command Line
Open PowerShell or Command Prompt in this folder and run:
```bash
py -3 -m streamlit run app.py
```

The web application will automatically open in your browser at:
`http://localhost:8501`

---

## 🛠️ Required Dependencies

All dependencies are already installed on your system:
- Python 3.13
- `streamlit`
- `pillow`
- `google-genai`
- `pydantic`
- `requests`

---

## 🔑 Using Gemini Vision AI Mode

1. Get a free API key from [Google AI Studio](https://aistudio.google.com).
2. Enter your key in the app sidebar, or set it in your environment:
   ```powershell
   $env:GEMINI_API_KEY="your_api_key_here"
   ```
3. Upload 4 photos and click **"Run Full Compliance Audit"**.
