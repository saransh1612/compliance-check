"""
Creates synthetic visual test cards for demo inspection.
Generates front, back, left, and right test visuals for both Compliant and Non-Compliant scenarios.
"""

import os
from PIL import Image, ImageDraw, ImageFont

SAMPLES_DIR = os.path.join(os.path.dirname(__file__), "samples")
os.makedirs(SAMPLES_DIR, exist_ok=True)

def create_card(title: str, subtitle: str, color: tuple, details: list, filename: str):
    width, height = 800, 500
    img = Image.new("RGB", (width, height), color=(240, 244, 248))
    draw = ImageDraw.Draw(img)

    # Top banner
    draw.rectangle([(0, 0), (width, 80)], fill=color)
    
    # Try default font or basic drawing
    draw.text((25, 20), title, fill=(255, 255, 255))
    draw.text((25, 48), subtitle, fill=(230, 230, 230))

    # Truck illustration outline
    draw.rectangle([(50, 120), (750, 440)], outline=(100, 116, 139), width=3, fill=(255, 255, 255))
    
    # Draw sample visual items
    y_pos = 140
    for d in details:
        draw.rectangle([(80, y_pos), (720, y_pos + 45)], fill=(224, 231, 255), outline=(99, 102, 241), width=1)
        draw.text((100, y_pos + 12), d, fill=(30, 41, 59))
        y_pos += 60

    img.save(os.path.join(SAMPLES_DIR, filename), "JPEG")

def generate_all_samples():
    # 1. Front Compliant
    create_card(
        "LPG PACKED TRUCK - FRONT VIEW (COMPLIANT)",
        "Standard Bharat Petroleum 306/450 Cylinder Livery",
        (0, 51, 153),
        [
            "[OK] Top Crown: 'GOODS CARRIER' (310x1490mm) with Class 2 Diamond",
            "[OK] Cabin Face: 'Bharat Petroleum' Logo (160x1300mm)",
            "[OK] Bumper/Grill: Class 2 Flammable Gas Diamond (250x250mm)",
            "[OK] License Plate: MH 12 BP 1075 & Blue/White Cab Livery"
        ],
        "sample_front.jpg"
    )

    # 2. Left Compliant (Helper side - English)
    create_card(
        "LPG PACKED TRUCK - LEFT VIEW (HELPER SIDE)",
        "English Side Panel & EIP Compliance",
        (0, 51, 153),
        [
            "[OK] Cabin Door: 'Bharatgas' Logo Sticker (200x600mm)",
            "[OK] Side Main Panel: 'Bharat Petroleum' English + Wave Ribbons (4200x900mm)",
            "[OK] Rear Lower Side: EIP Board (UN 1075, HAZCHEM 2WE, 800x600mm)",
            "[OK] Slotted Cage Frame Clamped with M10 U-Clamps"
        ],
        "sample_left.jpg"
    )

    # 3. Right Compliant (Driver side - Hindi)
    create_card(
        "LPG PACKED TRUCK - RIGHT VIEW (DRIVER SIDE)",
        "Hindi Side Panel & EIP Compliance",
        (0, 51, 153),
        [
            "[OK] Cabin Door: 'भारतगैस' Hindi Logo Sticker (200x600mm)",
            "[OK] Side Main Panel: 'भारत पेट्रोलियम' Hindi Devanagari (4200x900mm)",
            "[OK] Right Side: EIP Board (UN 1075, HAZCHEM 2WE, 800x600mm)",
            "[OK] Driver Cabin Livery & Locking Hardware"
        ],
        "sample_right.jpg"
    )

    # 4. Back Compliant
    create_card(
        "LPG PACKED TRUCK - BACK / REAR VIEW (COMPLIANT)",
        "Rear Gate Mesh & 3rd EIP Panel",
        (0, 51, 153),
        [
            "[OK] Rear Gate: 3rd EIP Board (UN 1075, HAZCHEM 2WE, Emergency 100/101/102)",
            "[OK] Rear Hazard: Class 2 Flammable Gas Diamond Sticker",
            "[OK] Safety: Red/White Reflective Tape Across Rear Under-run Bumper",
            "[OK] Rear License Plate & Gate Locking Latches Intact"
        ],
        "sample_back.jpg"
    )

if __name__ == "__main__":
    generate_all_samples()
    print("Generated all sample test images in samples/ directory.")
