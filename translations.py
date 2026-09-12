"""
Translations and Multilingual Support for LPG Packed Truck Compliance Application
Supports: English (en), Hindi (hi), Bengali (bn)
"""

from typing import Dict, Any

# UI Text Dictionary
UI_TEXT: Dict[str, Dict[str, str]] = {
    "en": {
        "app_title": "BPCL LPG Packed Truck Compliance Checker",
        "app_subtitle": "Bharat Petroleum / Bharatgas 306 & 450 Cylinders Truck Inspection Portal",
        "select_lang": "Language",
        "quick_audit": "Quick Inspection Setup",
        "truck_no": "Truck Registration No.",
        "plant_name": "BPCL Bottling Plant",
        "transporter": "Transporter Name",
        "auditor": "Safety Inspector Name",
        "truck_cap": "Cylinder Capacity",
        "photo_upload_title": "Upload 4 Inspection Photos",
        "photo_front": "Front View",
        "photo_front_sub": "Windshield, crown, logo & hazard label",
        "photo_left": "Left Side (Helper Side)",
        "photo_left_sub": "English panel & Left EIP board",
        "photo_right": "Right Side (Driver Side)",
        "photo_right_sub": "Hindi panel & Right EIP board",
        "photo_back": "Rear View (Mesh Gate)",
        "photo_back_sub": "Rear EIP board, reflectors & latch",
        "rotate_left": "⟲ 90° Left",
        "rotate_right": "⟳ 90° Right",
        "run_audit_btn": "🔍 Run Compliance Audit",
        "load_sample_btn": "📂 Load All 4 Sample Photos",
        "clear_photos_btn": "🗑️ Clear Photos",
        "audit_results_title": "Vehicle Compliance Checklist",
        "status_pass": "VEHICLE COMPLIANT — APPROVED FOR DISPATCH",
        "status_pass_desc": "All safety markings, panels, and stickers strictly satisfy BPCL guidelines.",
        "status_fail": "VEHICLE NON-COMPLIANT — DISPATCH PROHIBITED",
        "status_fail_desc": "Critical safety or branding defects detected. Vehicle must be rectified before dispatch.",
        "score_label": "Audit Score",
        "total_items": "Total Items Checked",
        "passed_items": "Correct Items",
        "failed_items": "Defects Found",
        "all_sides": "All Sides (Complete Truck)",
        "front_side": "Front View (Cabin)",
        "left_side": "Left Side (Helper)",
        "right_side": "Right Side (Driver)",
        "back_side": "Rear Gate (Back)",
        "filter_all": "All Items",
        "filter_defects_only": "❌ Only Defects (Non-Compliant)",
        "filter_correct_only": "✅ Only Correct (Compliant)",
        "col_side": "Truck Side",
        "col_item": "Inspection Item",
        "col_status": "Status",
        "col_correct": "✅ What is Correct (Required Standard)",
        "col_wrong": "❌ What is Wrong (Vehicle Condition)",
        "col_action": "Remediation Action",
        "status_compliant": "COMPLIANT",
        "status_non_compliant": "DEFECT / FAIL",
        "status_warning": "WARNING",
        "no_defect_found": "✅ No defect. Fully conforms to BPCL specification.",
        "action_none": "No action needed",
        "nav_table_tab": "📋 Checklist Table (All Sides)",
        "nav_front_tab": "1️⃣ Front View",
        "nav_left_tab": "2️⃣ Left Side (English)",
        "nav_right_tab": "3️⃣ Right Side (Hindi)",
        "nav_back_tab": "4️⃣ Rear Gate",
        "nav_cert_tab": "📄 Official Certificate",
        "download_cert": "📥 Download HTML Audit Certificate",
        "no_items_filter": "No items match the selected filter.",
        "remediation_label": "Fix Action:"
    },
    "hi": {
        "app_title": "बीपीसीएल एलपीजी पैक्ड ट्रक अनुपालन जांच (Compliance Checker)",
        "app_subtitle": "भारत पेट्रोलियम / भारतगैस 306 एवं 450 सिलेंडर ट्रक निरीक्षण पोर्टल",
        "select_lang": "भाषा चुनें",
        "quick_audit": "निरीक्षण विवरण भरें",
        "truck_no": "ट्रक रजिस्ट्रेशन नंबर",
        "plant_name": "बीपीसीएल एलपीजी बॉटलिंग प्लांट",
        "transporter": "ट्रांसपोर्टर का नाम",
        "auditor": "सुरक्षा निरीक्षक का नाम",
        "truck_cap": "सिलेंडर क्षमता",
        "photo_upload_title": "ट्रक के चारों तरफ के 4 फोटो डालें",
        "photo_front": "आगे का फोटो (Front)",
        "photo_front_sub": "विंडशील्ड, क्राउन, लोगो और लाल खतरा डायमंड",
        "photo_left": "बायां भाग (खलासी/हेल्पर तरफ)",
        "photo_left_sub": "अंग्रेजी पैनल और बायां EIP आपातकालीन बोर्ड",
        "photo_right": "दायां भाग (ड्राइवर तरफ)",
        "photo_right_sub": "हिन्दी पैनल और दायां EIP आपातकालीन बोर्ड",
        "photo_back": "पीछे का फोटो (जालीदार गेट)",
        "photo_back_sub": "पीछे का EIP बोर्ड, रिफ्लेक्टर और गेट लॉक",
        "rotate_left": "⟲ 90° बाएँ घुमाएं",
        "rotate_right": "⟳ 90° दाएँ घुमाएं",
        "run_audit_btn": "🔍 ट्रक जांच शुरू करें (Run Audit)",
        "load_sample_btn": "📂 4 सैंपल फोटो लोड करें",
        "clear_photos_btn": "🗑️ फोटो हटाएं",
        "audit_results_title": "ट्रक अनुपालन चेकलिस्ट तालिका",
        "status_pass": "गाड़ी पूरी तरह पास है — रवानगी की अनुमति है (APPROVED)",
        "status_pass_desc": "सभी बोर्ड, स्टीकर, रंग और सुरक्षा मानक बीपीसीएल नियम अनुसार बिल्कुल सही हैं।",
        "status_fail": "गाड़ी में कमियां हैं — रवानगी पर रोक (DISPATCH PROHIBITED)",
        "status_fail_desc": "गंभीर सुरक्षा या बोर्ड संबंधी कमियां पाई गईं। गाड़ी ठीक कराने के बाद ही रवाना करें।",
        "score_label": "जांच स्कोर",
        "total_items": "कुल जांच बिंदु",
        "passed_items": "सही बिंदु (Pass)",
        "failed_items": "खराबियां (Defects)",
        "all_sides": "पूरी गाड़ी (सभी दिशाएं)",
        "front_side": "आगे का भाग (केबिन)",
        "left_side": "बायां भाग (खलासी तरफ)",
        "right_side": "दायां भाग (ड्राइवर तरफ)",
        "back_side": "पीछे का भाग (गेट)",
        "filter_all": "सभी जांच दिखाएं",
        "filter_defects_only": "❌ केवल गलतियां / कमियां दिखाएं",
        "filter_correct_only": "✅ केवल सही बिंदु दिखाएं",
        "col_side": "गाड़ी का भाग / दिशा",
        "col_item": "जांच का विषय",
        "col_status": "स्थिति",
        "col_correct": "✅ सही क्या होना चाहिए (नियम/मानक)",
        "col_wrong": "❌ क्या गलत है (गाड़ी की हालत)",
        "col_action": "सुधार का तरीका",
        "status_compliant": "सही (PASS)",
        "status_non_compliant": "गलत (FAIL)",
        "status_warning": "चेतावनी",
        "no_defect_found": "✅ कोई खराबी नहीं। मानक के अनुसार बिल्कुल सही है।",
        "action_none": "कोई सुधार आवश्यक नहीं",
        "nav_table_tab": "📋 मुख्य चेकलिस्ट तालिका (सभी दिशाएं)",
        "nav_front_tab": "1️⃣ आगे का भाग",
        "nav_left_tab": "2️⃣ बायां भाग (अंग्रेजी)",
        "nav_right_tab": "3️⃣ दायां भाग (हिन्दी)",
        "nav_back_tab": "4️⃣ पीछे का गेट",
        "nav_cert_tab": "📄 आधिकारिक प्रमाणपत्र",
        "download_cert": "📥 प्रमाणपत्र डाउनलोड करें (HTML)",
        "no_items_filter": "इस फिल्टर के लिए कोई बिंदु नहीं मिला।",
        "remediation_label": "ठीक करने का उपाय:"
    },
    "bn": {
        "app_title": "বিপিসিএল এলপিজি প্যাকড ট্রাক সম্মতি যাচাই (Compliance Checker)",
        "app_subtitle": "ভারত পেট্রোলিয়াম / ভারতগ্যাস ৩০৬ ও ৪৫০ সিলিন্ডার ট্রাক পরিদর্শন পোর্টাল",
        "select_lang": "ভাষা নির্বাচন করুন",
        "quick_audit": "পরিদর্শন বিবরণ দিন",
        "truck_no": "ট্রাক রেজিস্ট্রেশন নম্বর",
        "plant_name": "বিপিসিএল বটলিং প্ল্যান্ট",
        "transporter": "ট্রান্সপোর্টারের নাম",
        "auditor": "সুরক্ষা পরিদর্শকের নাম",
        "truck_cap": "সিলিন্ডার ধারণক্ষমতা",
        "photo_upload_title": "ট্রাকের চারপাশের ৪টি ছবি দিন",
        "photo_front": "সামনের ছবি (Front)",
        "photo_front_sub": "উইন্ডশিল্ড, ক্রাউন, লোগো এবং লাল বিপদ ডায়মন্ড",
        "photo_left": "বাম পাশ (সহকারী/খালাসী পাশ)",
        "photo_left_sub": "ইংরেজি প্যানেল এবং বাম EIP জরুরী বোর্ড",
        "photo_right": "ডান পাশ (ড্রাইভার পাশ)",
        "photo_right_sub": "হিন্দি প্যানেল এবং ডান EIP জরুরী বোর্ড",
        "photo_back": "পেছনের ছবি (জালের গেট)",
        "photo_back_sub": "পেছনের EIP বোর্ড, প্রতিফলক ও গেটের লক",
        "rotate_left": "⟲ ৯০° বামে ঘোরান",
        "rotate_right": "⟳ ৯০° ডানে ঘোরান",
        "run_audit_btn": "🔍 ট্রাক পরীক্ষা শুরু করুন (Run Audit)",
        "load_sample_btn": "📂 ৪টি নমুনা ছবি লোড করুন",
        "clear_photos_btn": "🗑️ ছবি মুছুন",
        "audit_results_title": "ট্রাক সম্মতি চেকলিস্ট টেবিল",
        "status_pass": "গাড়ি সম্পূর্ণ নিয়ম মেনেছে — ছাড়পত্র মঞ্জুর (APPROVED)",
        "status_pass_desc": "সমস্ত বোর্ড, স্টিকার, রঙ এবং নিরাপত্তা নিয়মাবলী সঠিকভাবে পূরণ হয়েছে।",
        "status_fail": "গাড়িতে ত্রুটি রয়েছে — গাড়ি ছাড়া নিষিদ্ধ (DISPATCH PROHIBITED)",
        "status_fail_desc": "মারাত্মক নিরাপত্তা বা বোর্ড সংক্রান্ত ত্রুটি পাওয়া গেছে। ঠিক না করে গাড়ি ছাড়া যাবে না।",
        "score_label": "পরিদর্শন স্কোর",
        "total_items": "মোট চেকের সংখ্যা",
        "passed_items": "সঠিক পয়েন্ট (Pass)",
        "failed_items": "ত্রুটির সংখ্যা (Defects)",
        "all_sides": "সম্পূর্ণ গাড়ি (সব দিক)",
        "front_side": "সামনের অংশ (কেবিন)",
        "left_side": "বাম পাশ (খালাসী পাশ)",
        "right_side": "ডান পাশ (ড্রাইভার পাশ)",
        "back_side": "পেছনের অংশ (গেট)",
        "filter_all": "সব চেক দেখান",
        "filter_defects_only": "❌ শুধুমাত্র ভুল / ত্রুটিগুলো দেখান",
        "filter_correct_only": "✅ শুধুমাত্র সঠিকগুলো দেখান",
        "col_side": "ট্রাকের অংশ / দিক",
        "col_item": "চেকের বিষয়",
        "col_status": "অবস্থা",
        "col_correct": "✅ সঠিক কী হওয়া উচিত (নিয়ম/মানক)",
        "col_wrong": "❌ কী ভুল আছে (গাড়ির অবস্থা)",
        "col_action": "সংশোধনের উপায়",
        "status_compliant": "সঠিক (PASS)",
        "status_non_compliant": "ভুল / ত্রুটি (FAIL)",
        "status_warning": "সতর্কতা",
        "no_defect_found": "✅ কোনো ত্রুটি নেই। নিয়ম অনুযায়ী একদম সঠিক।",
        "action_none": "কোনো সংশোধনের প্রয়োজন নেই",
        "nav_table_tab": "📋 প্রধান চেকলিস্ট টেবিল (সব দিক)",
        "nav_front_tab": "1️⃣ সামনের অংশ",
        "nav_left_tab": "2️⃣ বাম পাশ (ইংরেজি)",
        "nav_right_tab": "3️⃣ ডান পাশ (হিন্দি)",
        "nav_back_tab": "4️⃣ পেছনের গেট",
        "nav_cert_tab": "📄 অফিসিয়াল সার্টিফিকেট",
        "download_cert": "📥 সার্টিফিকেট ডাউনলোড করুন (HTML)",
        "no_items_filter": "এই ফিল্টারে কোনো তথ্য পাওয়া যায়নি।",
        "remediation_label": "সংশোধনের পদক্ষেপ:"
    }
}

# Truck Sides Data
SIDE_METADATA: Dict[str, Dict[str, Any]] = {
    "front": {
        "icon": "🚛",
        "badge_bg": "#1e40af",
        "badge_fg": "#ffffff",
        "names": {
            "en": "Front View (Cabin)",
            "hi": "आगे का भाग (केबिन)",
            "bn": "সামনের অংশ (কেবিন)"
        },
        "short_names": {
            "en": "Front",
            "hi": "आगे",
            "bn": "সামনে"
        }
    },
    "left": {
        "icon": "◀️",
        "badge_bg": "#0e7490",
        "badge_fg": "#ffffff",
        "names": {
            "en": "Left Side (Helper / Cleaner)",
            "hi": "बायां भाग (खलासी तरफ)",
            "bn": "বাম পাশ (খালাসী / সহকারী)"
        },
        "short_names": {
            "en": "Left (Cleaner)",
            "hi": "बायां (खलासी)",
            "bn": "বাম (খালাসী)"
        }
    },
    "right": {
        "icon": "▶️",
        "badge_bg": "#4338ca",
        "badge_fg": "#ffffff",
        "names": {
            "en": "Right Side (Driver)",
            "hi": "दायां भाग (ड्राइवर तरफ)",
            "bn": "ডান পাশ (ড্রাইভার পাশ)"
        },
        "short_names": {
            "en": "Right (Driver)",
            "hi": "दायां (ड्राइवर)",
            "bn": "ডান (ড্রাইভার)"
        }
    },
    "back": {
        "icon": "🔙",
        "badge_bg": "#334155",
        "badge_fg": "#ffffff",
        "names": {
            "en": "Rear Gate (Back)",
            "hi": "पीछे का गेट (Back)",
            "bn": "পেছনের গেট (Back)"
        },
        "short_names": {
            "en": "Rear Gate",
            "hi": "पीछे का गेट",
            "bn": "পেছনের গেট"
        }
    }
}

# Comprehensive Rule Definitions & Translations for all 17 Items
RULE_TRANSLATIONS: Dict[str, Dict[str, Any]] = {
    "F1_GOODS_CARRIER": {
        "side": "front",
        "names": {
            "en": "'GOODS CARRIER' Sunshade Sticker",
            "hi": "सनशेड 'GOODS CARRIER' स्टीकर",
            "bn": "'GOODS CARRIER' সানশেড স্টিকার"
        },
        "correct_spec": {
            "en": "Size 310 mm x 1490 mm, royal blue background, bold white lettering 'GOODS CARRIER' with Class 2 Flammable Gas red diamond in center.",
            "hi": "साइज 310 x 1490 मिमी, गहरा नीला बैकग्राउंड, सफेद अक्षरों में 'GOODS CARRIER' और बीच में लाल क्लास 2 ज्वलनशील गैस डायमंड होना अनिवार्य है।",
            "bn": "সাইজ ৩১০ x ১৪৯০ মিমি, গাঢ় নীল ব্যাকগ্রাউন্ড, সাদা বড় হরফে 'GOODS CARRIER' এবং মাঝে লাল ক্লাস ২ দাহ্য গ্যাস ডায়মন্ড থাকা আবশ্যক।"
        },
        "default_defect": {
            "en": "Sunshade crown sticker missing, faded, peeling, or missing the center Class 2 hazard diamond.",
            "hi": "सनशेड स्टीकर गायब, फटा हुआ, पुराना या बीच में क्लास 2 खतरा डायमंड नहीं लगा है।",
            "bn": "সানশেড স্টিকার অনুপস্থিত, বিবর্ণ, ছেঁড়া অথবা মাঝে ক্লাস ২ বিপদ ডায়মন্ড নেই।"
        },
        "default_action": {
            "en": "Replace with approved 310x1490mm 'GOODS CARRIER' vinyl sticker with Class 2 diamond.",
            "hi": "क्लास 2 डायमंड युक्त 310x1490 मिमी का नया विनाइल स्टीकर लगाएं।",
            "bn": "ক্লাস ২ ডায়মন্ড যুক্ত ৩১০x১৪৯০ মিমি নতুন ভিনাইল স্টিকার লাগান।"
        }
    },
    "F2_BP_FRONT_LOGO": {
        "side": "front",
        "names": {
            "en": "'Bharat Petroleum' Front Logo",
            "hi": "विंडशील्ड के नीचे 'भारत पेट्रोलियम' लोगो",
            "bn": "উইন্ডশিল্ডের নিচে 'ভারত পেট্রোলিয়াম' লোগো"
        },
        "correct_spec": {
            "en": "Size 160 mm x 1300 mm, blue 'Bharat Petroleum' lettering with standard BPCL circular emblem, placed below windshield.",
            "hi": "साइज 160 x 1300 मिमी, विंडशील्ड के नीचे नीले अक्षरों में 'Bharat Petroleum' और बीपीसीएल का गोल चक्र लोगो।",
            "bn": "সাইজ ১৬০ x ১৩০০ মিমি, উইন্ডশিল্ডের নিচে নীল হরফে 'Bharat Petroleum' এবং বিপিসিএল-এর গোল চক্র লোগো।"
        },
        "default_defect": {
            "en": "Front logo is missing, heavily scratched, or peeling off cabin face.",
            "hi": "सामने का बीपीसीएल लोगो गायब है, उखड़ा हुआ है या विवरण मिट गया है।",
            "bn": "সামনের বিপিসিএল লোগো অনুপস্থিত, উঠে গেছে বা অস্পষ্ট।"
        },
        "default_action": {
            "en": "Affix new 160x1300mm Bharat Petroleum logo sticker below windshield.",
            "hi": "विंडशील्ड के नीचे 160x1300 मिमी का नया लोगो स्टीकर लगाएं।",
            "bn": "উইন্ডশিল্ডের নিচে ১৬০x১৩০০ মিমি নতুন লোগো স্টিকার লাগান।"
        }
    },
    "F3_FRONT_CLASS_LABEL": {
        "side": "front",
        "names": {
            "en": "Front Class 2 Flammable Gas Hazard Diamond",
            "hi": "सामने क्लास 2 ज्वलनशील गैस डायमंड स्टीकर",
            "bn": "সামনে ক্লাস ২ দাহ্য গ্যাস ডায়মন্ড স্টিকার"
        },
        "correct_spec": {
            "en": "Size 250 mm x 250 mm, red diamond sticker with white flame symbol and numeral '2' at bottom, affixed on front grill/bumper area.",
            "hi": "साइज 250 x 250 मिमी, लाल डायमंड स्टीकर जिसमें सफेद लौ का निशान और नीचे '2' लिखा हो, ग्रिल या बम्पर पर लगा होना चाहिए।",
            "bn": "সাইজ ২৫০ x ২৫০ মিমি, লাল ডায়মন্ড স্টিকার যাতে সাদা আগুনের শিখা এবং নিচে '২' লেখা থাকবে, গ্রিল বা বাম্পারে লাগানো থাকবে।"
        },
        "default_defect": {
            "en": "Hazard diamond is torn, peeled, missing, or faded, violating hazardous cargo rules.",
            "hi": "सामने का लाल क्लास 2 खतरा डायमंड स्टीकर गायब या फटा हुआ है।",
            "bn": "সামনের লাল ক্লাস ২ বিপদ ডায়মন্ড স্টিকার অনুপস্থিত বা উঠে গেছে।"
        },
        "default_action": {
            "en": "Affix new 250x250mm Class 2 Flammable Gas sticker on front grill.",
            "hi": "ग्रिल पर 250x250 मिमी का नया क्लास 2 ज्वलनशील गैस स्टीकर लगाएं।",
            "bn": "গ্রিলে ২৫০x২৫০ মিমি নতুন ক্লাস ২ দাহ্য গ্যাস স্টিকার লাগান।"
        }
    },
    "F4_CABIN_LIVERY": {
        "side": "front",
        "names": {
            "en": "Cabin Color Scheme & Livery",
            "hi": "केबिन का रंग व फिनिशिंग (नीला व सफेद)",
            "bn": "কেবিনের রঙ ও নকশা (নীল ও সাদা)"
        },
        "correct_spec": {
            "en": "Standard blue and white cabin finish matching BPCL standards, in clean and undamaged condition.",
            "hi": "बीपीसीएल मानक के अनुसार नीला और सफेद केबिन रंग, साफ-सुथरा और बिना डेंट के।",
            "bn": "বিপিসিএল নিয়ম অনুযায়ী নীল ও সাদা কেবিনের রঙ, পরিষ্কার এবং ক্ষতিমুক্ত।"
        },
        "default_defect": {
            "en": "Cabin paint heavily faded, rusted, mismatched colors, or dented.",
            "hi": "केबिन का पेंट उखड़ा हुआ, जंग लगा या गलत रंग का है।",
            "bn": "কেবিনের রঙ উঠে গেছে, মরিচা ধরেছে বা অন্য রঙের।"
        },
        "default_action": {
            "en": "Repaint cabin in standard BPCL blue and white shades.",
            "hi": "केबिन को बीपीसीएल मानक नीले और सफेद रंग में दोबारा पेंट कराएं।",
            "bn": "কেবিনকে বিপিসিএল অনুমোদিত নীল ও সাদা রঙে পুনরায় রঙ করুন।"
        }
    },
    "F5_FRONT_NUMBER_PLATE": {
        "side": "front",
        "names": {
            "en": "Registration Number Plate (Front)",
            "hi": "सामने की नंबर प्लेट (पंजीकरण संख्या)",
            "bn": "সামনের নম্বর প্লেট (গাড়ির রেজিস্ট্রেশন)"
        },
        "correct_spec": {
            "en": "Official high security / legible vehicle registration number plate mounted securely on front bumper.",
            "hi": "सामने बम्पर पर साफ दिखने वाली वैध और मजबूत नंबर प्लेट लगी होनी चाहिए।",
            "bn": "সামনের বাম্পারে পরিষ্কার ও স্পষ্ট বৈধ নম্বর প্লেট শক্তভাবে লাগানো থাকতে হবে।"
        },
        "default_defect": {
            "en": "Front registration plate broken, bent, illegible, or missing.",
            "hi": "सामने की नंबर प्लेट टूटी, मुड़ी हुई, गंदी या गायब है।",
            "bn": "সামনের নম্বর প্লেট ভাঙা, অস্পষ্ট বা অনুপস্থিত।"
        },
        "default_action": {
            "en": "Mount clear, legible high-security number plate on front bumper.",
            "hi": "सामने बम्पर पर नई और साफ नंबर प्लेट लगाएं।",
            "bn": "সামনে বাম্পারে পরিষ্কার ও স্পষ্ট নম্বর প্লেট লাগান।"
        }
    },
    "L1_BHARATGAS_CABIN": {
        "side": "left",
        "names": {
            "en": "'Bharatgas' Helper Cabin Door Sticker",
            "hi": "खलासी दरवाज़े पर 'भारतगैस' स्टीकर",
            "bn": "খালাসী দরজায় 'ভারতগ্যাস' স্টিকার"
        },
        "correct_spec": {
            "en": "Size 200 mm x 600 mm printed vinyl sticker with Bharatgas logo and 'COOK FOOD. SERVE LOVE.' tagline on helper side cabin door.",
            "hi": "साइज 200 x 600 मिमी, खलासी (बाईं) तरफ के दरवाजे पर 'Bharatgas' लोगो और 'COOK FOOD. SERVE LOVE.' का विनाइल स्टीकर।",
            "bn": "সাইজ ২০০ x ৬০০ মিমি, সহকারী/খালাসী (বাম) দরজায় 'Bharatgas' লোগো ও 'COOK FOOD. SERVE LOVE.' স্লোগানের ভিনাইল স্টিকার।"
        },
        "default_defect": {
            "en": "Helper cabin door sticker missing, scratched, or incorrect design.",
            "hi": "खलासी दरवाजे पर भारतगैस का स्टीकर गायब या फटा हुआ है।",
            "bn": "সহকারী দরজায় ভারতগ্যাস স্টিকার অনুপস্থিত বা ছেঁড়া।"
        },
        "default_action": {
            "en": "Affix approved 200x600mm Bharatgas sticker on helper cabin door.",
            "hi": "खलासी दरवाजे पर 200x600 मिमी का नया भारतगैस स्टीकर लगाएं।",
            "bn": "সহকারী দরজায় ২০০x৬০০ মিমি অনুমোদিত ভারতগ্যাস স্টিকার লাগান।"
        }
    },
    "L2_SIDE_PANEL_ENGLISH": {
        "side": "left",
        "names": {
            "en": "Side Main Panel in English ('Bharat Petroleum')",
            "hi": "बाईं ओर मुख्य पैनल - अंग्रेजी ('Bharat Petroleum')",
            "bn": "বাম পাশের মূল প্যানেল - ইংরেজি ('Bharat Petroleum')"
        },
        "correct_spec": {
            "en": "Size 4200 mm x 900 mm ACM board with pop rivets. Features BPCL roundel on left, blue English text 'Bharat Petroleum', and top/bottom yellow-blue wave ribbons.",
            "hi": "साइज 4200 x 900 मिमी एसीएम शीट बोर्ड, बाईं ओर बीपीसीएल प्रतीक, नीले रंग में अंग्रेजी 'Bharat Petroleum' और ऊपर-नीचे पीली-नीली लहरदार पट्टियां।",
            "bn": "সাইজ ৪২০০ x ৯০০ মিমি এসিএম বোর্ড, বাম পাশে বিপিসিএল গোল প্রতীক, নীল রঙে ইংরেজি 'Bharat Petroleum' এবং উপরে-নিচে হলুদ-নীল ঢেউখেলানো রিবন।"
        },
        "default_defect": {
            "en": "English side panel missing, damaged, peeling vinyl, loose rivets, or Hindi text mistakenly installed on left.",
            "hi": "बाईं तरफ का मुख्य पैनल गायब है, क्षतिग्रस्त है, या गलत भाषा का बोर्ड लगा है।",
            "bn": "বাম পাশের মূল প্যানেল অনুপস্থিত, ক্ষতিগ্রস্ত, রিভেট আলগা বা ভুল ভাষার লাগানো।"
        },
        "default_action": {
            "en": "Install 4200x900mm ACM panel with English Bharat Petroleum lettering and wave ribbons.",
            "hi": "बाईं तरफ 4200x900 मिमी का अंग्रेजी 'Bharat Petroleum' बोर्ड पॉप-रिवेट से कसकर लगाएं।",
            "bn": "বাম পাশে ৪২০০x৯০০ মিমি ইংরেজি 'Bharat Petroleum' বোর্ড পপ-রিভেট দিয়ে শক্ত করে লাগান।"
        }
    },
    "L3_LEFT_EIP_PANEL": {
        "side": "left",
        "names": {
            "en": "Emergency Information Panel (EIP) - Left Side",
            "hi": "आपातकालीन सूचना पैनल (EIP) - बाईं ओर",
            "bn": "জরুরী তথ্য প্যানেল (EIP) - বাম পাশ"
        },
        "correct_spec": {
            "en": "Size 800 mm x 600 mm metal board on lower left body. Mandatory: 'LIQUIFIED PETROLEUM GAS', 'UN No. 1075', 'HAZCHEM 2WE', Emergency dial (100, 101, 102), Specialist Advice, and Class 2 red diamond.",
            "hi": "साइज 800 x 600 मिमी धातु बोर्ड। अनिवार्य: 'LIQUIFIED PETROLEUM GAS', 'UN No. 1075', 'HAZCHEM 2WE', आपातकालीन नंबर (100, 101, 102), विशेषज्ञ सलाह, और क्लास 2 लाल डायमंड।",
            "bn": "সাইজ ৮০০ x ৬০০ মিমি মেটাল বোর্ড। আবশ্যিক: 'LIQUIFIED PETROLEUM GAS', 'UN No. 1075', 'HAZCHEM 2WE', জরুরী নম্বর (100, 101, 102), বিশেষজ্ঞ পরামর্শ, ও ক্লাস ২ লাল ডায়মন্ড।"
        },
        "default_defect": {
            "en": "Left EIP panel missing, numbers illegible, phone numbers faded, or hazard diamond missing.",
            "hi": "बाईं ओर का EIP बोर्ड गायब है या आपातकालीन नंबर मिटे हुए/अस्पष्ट हैं।",
            "bn": "বাম পাশের EIP বোর্ড অনুপস্থিত বা জরুরী নম্বরগুলি অস্পষ্ট।"
        },
        "default_action": {
            "en": "Install approved 800x600mm EIP panel with UN 1075, HAZCHEM 2WE, and contact numbers.",
            "hi": "बाईं ओर नया 800x600 मिमी का स्पष्ट EIP बोर्ड लगाएं।",
            "bn": "বাম পাশে নতুন ৮০০x৬০০ মিমি স্পষ্ট EIP বোর্ড লাগান।"
        }
    },
    "L4_LEFT_CAGE_STRUCTURE": {
        "side": "left",
        "names": {
            "en": "Cylinder Cage & Locking Integrity (Left)",
            "hi": "सिलेंडर पिंजरा और लॉकिंग सुरक्षा (बायां)",
            "bn": "সিলিন্ডার খাঁচা ও লকিং নিরাপত্তা (বাম)"
        },
        "correct_spec": {
            "en": "Standard blue/white horizontal slotted cage frame for cylinder containment, clamped securely with M10 U-clamps.",
            "hi": "सिलेंडर रोकने के लिए नीला/सफेद लोहे का जालीदार पिंजरा, M10 यू-क्लैंप से मजबूती से कसा हुआ।",
            "bn": "সিলিন্ডার আটকে রাখার জন্য নীল/সাদা লোহার খাঁচা, M10 ইউ-ক্ল্যাম্প দিয়ে শক্তভাবে আটকানো।"
        },
        "default_defect": {
            "en": "Left cage frame bent, bars broken, loose U-clamps, or unstable containment.",
            "hi": "बाईं तरफ का पिंजरा मुड़ा हुआ, सरिया टूटा हुआ या क्लैंप ढीला है।",
            "bn": "বাম পাশের খাঁচা বাঁকা, রড ভাঙা বা ক্ল্যাম্প আলগা।"
        },
        "default_action": {
            "en": "Repair/straighten cage frame and tighten all M10 U-clamps.",
            "hi": "पिंजरे की मरम्मत करें और सभी M10 यू-क्लैंप कसें।",
            "bn": "খাঁচা মেরামত করুন এবং সমস্ত M10 ইউ-ক্ল্যাম্প শক্ত করে আঁটুন।"
        }
    },
    "R1_BHARATGAS_CABIN": {
        "side": "right",
        "names": {
            "en": "'Bharatgas' Driver Cabin Door Sticker",
            "hi": "ड्राइवर दरवाज़े पर 'भारतगैस' स्टीकर",
            "bn": "ড্রাইভার দরজায় 'ভারতগ্যাস' স্টিকার"
        },
        "correct_spec": {
            "en": "Size 200 mm x 600 mm printed vinyl sticker with Bharatgas Hindi logo 'भारतगैस' and 'बनाईये खाना. परोसिये प्यार.' on driver cabin door.",
            "hi": "साइज 200 x 600 मिमी, ड्राइवर (दाएं) दरवाजे पर देवनागरी 'भारतगैस' लोगो और 'बनाईये खाना. परोसिये प्यार.' का विनाइल स्टीकर।",
            "bn": "সাইজ ২০০ x ৬০০ মিমি, ড্রাইভার (ডান) দরজায় দেবনাগরী 'भारतगैस' লোগো এবং 'बनाईये खाना. परोसिये प्यार.' স্লোগানের ভিনাইল স্টিকার।"
        },
        "default_defect": {
            "en": "Driver cabin door sticker missing, wrong English version installed, or peeled.",
            "hi": "ड्राइवर दरवाजे पर 'भारतगैस' हिंदी स्टीकर गायब है या फटा हुआ है।",
            "bn": "ড্রাইভার দরজায় 'ভারতগ্যাস' হিন্দি স্টিকার অনুপস্থিত বা ছেঁড়া।"
        },
        "default_action": {
            "en": "Affix approved 200x600mm Hindi Bharatgas sticker on driver door.",
            "hi": "ड्राइवर दरवाजे पर 200x600 मिमी का हिंदी 'भारतगैस' स्टीकर लगाएं।",
            "bn": "ড্রাইভার দরজায় ২০০x৬০০ মিমি হিন্দি 'ভারতগ্যাস' স্টিকার লাগান।"
        }
    },
    "R2_SIDE_PANEL_HINDI": {
        "side": "right",
        "names": {
            "en": "Side Main Panel in Hindi ('भारत पेट्रोलियम')",
            "hi": "दाईं ओर मुख्य पैनल - हिन्दी ('भारत पेट्रोलियम')",
            "bn": "ডান পাশের মূল প্যানেল - হিন্দি ('भारत पेट्रोलियम')"
        },
        "correct_spec": {
            "en": "Size 4200 mm x 900 mm ACM board. MUST feature Devanagari Hindi text 'भारत पेट्रोलियम' in blue with BPCL emblem and wave ribbons (Driver side).",
            "hi": "साइज 4200 x 900 मिमी एसीएम बोर्ड। अनिवार्य: ड्राइवर तरफ देवनागरी हिन्दी में 'भारत पेट्रोलियम' लिखा होना चाहिए।",
            "bn": "সাইজ ৪২০০ x ৯০০ মিমি এসিএম বোর্ড। আবশ্যিক: ড্রাইভারের পাশে দেবনাগরী হিন্দিতে 'भारत पेट्रोलियम' লেখা থাকতে হবে।"
        },
        "default_defect": {
            "en": "CRITICAL VIOLATION: Right side panel has English text instead of mandatory Hindi ('भारत पेट्रोलियम'), or panel is missing.",
            "hi": "गंभीर गलती: दाईं तरफ अनिवार्य हिन्दी ('भारत पेट्रोलियम') के स्थान पर अंग्रेजी बोर्ड लगा है या बोर्ड गायब है।",
            "bn": "মারাত্মক ত্রুটি: ডান পাশে বাধ্যতামূলক হিন্দি ('भारत पेट्रोलियम') লেখার বদলে ইংরেজি বোর্ড লাগানো আছে বা বোর্ডটি নেই।"
        },
        "default_action": {
            "en": "Replace right panel with Hindi 'भारत पेट्रोलियम' ACM board per BPCL guideline.",
            "hi": "दाईं ओर नियम अनुसार 4200x900 मिमी का हिन्दी 'भारत पेट्रोलियम' बोर्ड लगाएं।",
            "bn": "ডান পাশে নিয়ম অনুযায়ী ৪২০০x৯০০ মিমি হিন্দি 'भारत पेट्रोलियम' বোর্ড লাগান।"
        }
    },
    "R3_RIGHT_EIP_PANEL": {
        "side": "right",
        "names": {
            "en": "Emergency Information Panel (EIP) - Right Side",
            "hi": "आपातकालीन सूचना पैनल (EIP) - दाईं ओर",
            "bn": "জরুরী তথ্য প্যানেল (EIP) - ডান পাশ"
        },
        "correct_spec": {
            "en": "Size 800 mm x 600 mm metal board on right side. Mandatory: UN 1075, HAZCHEM 2WE, 'LIQUIFIED PETROLEUM GAS', Emergency 100/101/102, Specialist Advice, and Class 2 red diamond.",
            "hi": "साइज 800 x 600 मिमी धातु बोर्ड, दाईं ओर। अनिवार्य: UN 1075, HAZCHEM 2WE, आपातकालीन नंबर 100/101/102 और क्लास 2 लाल डायमंड।",
            "bn": "সাইজ ৮০০ x ৬০০ মিমি মেটাল বোর্ড, ডান পাশে। আবশ্যিক: UN 1075, HAZCHEM 2WE, জরুরী নম্বর 100/101/102 ও ক্লাস ২ লাল ডায়মন্ড।"
        },
        "default_defect": {
            "en": "Right EIP panel missing, corroded, emergency numbers not readable.",
            "hi": "दाईं ओर का EIP पैनल गायब है या आपातकालीन नंबर मिट चुके हैं।",
            "bn": "ডান পাশের EIP প্যানেল অনুপস্থিত বা তথ্য মুছে গেছে।"
        },
        "default_action": {
            "en": "Install approved 800x600mm EIP panel on right side.",
            "hi": "दाईं ओर 800x600 मिमी का नया वैध EIP बोर्ड लगाएं।",
            "bn": "ডান পাশে ৮০০x৬০০ মিমি নতুন বৈধ EIP বোর্ড লাগান।"
        }
    },
    "R4_RIGHT_CAGE_STRUCTURE": {
        "side": "right",
        "names": {
            "en": "Right Cylinder Cage Frame",
            "hi": "दाईं ओर का सिलेंडर पिंजरा",
            "bn": "ডান পাশের সিলিন্ডার খাঁচা"
        },
        "correct_spec": {
            "en": "Properly painted and maintained cylinder containment cage bars without physical structural damage.",
            "hi": "मजबूत और सही पेंट किया हुआ लोहे का पिंजरा, जिसमें कोई सरिया टूटा या मुड़ा न हो।",
            "bn": "মজবুত ও রঙ করা লোহার খাঁচা, যাতে কোনো রড ভাঙা বা বাঁকা না থাকে।"
        },
        "default_defect": {
            "en": "Right cage damaged, bent bars, rusted, or compromised containment.",
            "hi": "पिंजरे की सरिया मुड़ी हुई, जंग लगी या टूटी हुई है।",
            "bn": "খাঁচার রড বাঁকা, মরিচা ধরা বা ভাঙা।"
        },
        "default_action": {
            "en": "Straighten, weld, or paint cage bars.",
            "hi": "पिंजरे की मरम्मत कर सही पेंट करें।",
            "bn": "খাঁচা মেরামত করে রঙ করুন।"
        }
    },
    "B1_REAR_EIP_PANEL": {
        "side": "back",
        "names": {
            "en": "Rear Emergency Information Panel (EIP)",
            "hi": "पीछे का आपातकालीन सूचना पैनल (EIP)",
            "bn": "পেছনের জরুরী তথ্য প্যানেল (EIP)"
        },
        "correct_spec": {
            "en": "Size 800 mm x 600 mm board on rear mesh gate. Must contain: 'LIQUIFIED PETROLEUM GAS', 'UN No. 1075', 'HAZCHEM 2WE', Emergency dial (100/101/102), Specialist Advice, and Class 2 red diamond.",
            "hi": "साइज 800 x 600 मिमी बोर्ड पीछे के गेट पर कसा हुआ। अनिवार्य: UN 1075, HAZCHEM 2WE, आपातकालीन डायल 100/101/102 और क्लास 2 लाल डायमंड।",
            "bn": "সাইজ ৮০০ x ৬০০ মিমি বোর্ড পেছনের গেটে লাগানো। আবশ্যিক: UN 1075, HAZCHEM 2WE, জরুরী ডায়াল 100/101/102 ও ক্লাস ২ লাল ডায়মন্ড।"
        },
        "default_defect": {
            "en": "CRITICAL VIOLATION: Rear 3rd EIP board is completely MISSING from rear mesh gate.",
            "hi": "गंभीर गलती: पीछे के जालीदार गेट से तीसरा EIP बोर्ड पूरी तरह गायब है।",
            "bn": "মারাত্মক ত্রুটি: পেছনের গেট থেকে ৩য় EIP বোর্ডটি সম্পূর্ণ অনুপস্থিত।"
        },
        "default_action": {
            "en": "Fabricate and rivet 800x600mm EIP panel (UN 1075, HAZCHEM 2WE) to rear gate before dispatch.",
            "hi": "गाड़ी रवाना करने से पहले पीछे के गेट पर 800x600 मिमी का EIP बोर्ड रिवेट करें।",
            "bn": "গাড়ি ছাড়ার আগে পেছনের গেটে ৮০০x৬০০ মিমি EIP বোর্ড রিভেট করে লাগান।"
        }
    },
    "B2_REAR_CLASS_LABEL_REFLECTORS": {
        "side": "back",
        "names": {
            "en": "Rear Class 2 Diamond & Safety Reflective Striping",
            "hi": "पीछे क्लास 2 डायमंड और रिफ्लेक्टिव स्ट्रिप",
            "bn": "পেছনে ক্লাস ২ ডায়মন্ড ও প্রতিফলক স্ট্রিপ"
        },
        "correct_spec": {
            "en": "Class 2 Flammable Gas diamond (250x250mm) and high-visibility reflective red/white warning tape on rear bumper.",
            "hi": "क्लास 2 लाल डायमंड स्टीकर (250x250 मिमी) और बम्पर पर लाल/सफेद चमकने वाली रिफ्लेक्टिव टेप लगी होनी चाहिए।",
            "bn": "ক্লাস ২ লাল ডায়মন্ড স্টিকার (২৫০x২৫০ মিমি) এবং বাম্পারে লাল/সাদা উজ্জ্বল প্রতিফলক টেপ লাগানো থাকতে হবে।"
        },
        "default_defect": {
            "en": "Reflective tape faded/missing on bumper, or Class 2 hazard label missing.",
            "hi": "पीछे की रिफ्लेक्टिव टेप गायब, फटी हुई या पुरानी है, या क्लास 2 डायमंड नहीं है।",
            "bn": "পেছনের প্রতিফলক টেপ অনুপস্থিত, ছেঁড়া বা পুরানো, অথবা ক্লাস ২ ডায়মন্ড নেই।"
        },
        "default_action": {
            "en": "Affix approved high-intensity reflective tape and Class 2 label.",
            "hi": "नया हाई-इंटेंसिटी रिफ्लेक्टिव टेप और क्लास 2 स्टीकर लगाएं।",
            "bn": "নতুন হাই-ইনটেনসিটি প্রতিফলক টেপ ও ক্লাস ২ স্টিকার লাগান।"
        }
    },
    "B3_REAR_NUMBER_PLATE": {
        "side": "back",
        "names": {
            "en": "Rear Vehicle Registration Plate",
            "hi": "पीछे की नंबर प्लेट और लाइट",
            "bn": "পেছনের নম্বর প্লেট ও আলো"
        },
        "correct_spec": {
            "en": "Clearly legible registration plate affixed on rear bumper with functioning illumination lamp.",
            "hi": "पीछे के बम्पर पर साफ दिखने वाली नंबर प्लेट और रात के लिए नंबर प्लेट लाइट चालू होनी चाहिए।",
            "bn": "পেছনের বাম্পারে স্পষ্ট নম্বর প্লেট এবং কার্যকর নম্বর প্লেট বাতি থাকতে হবে।"
        },
        "default_defect": {
            "en": "Rear number plate dirty, broken, illegible, or lamp not working.",
            "hi": "पीछे की नंबर प्लेट गंदी, टूटी हुई या लाइट बंद है।",
            "bn": "পেছনের নম্বর প্লেট নোংরা, ভাঙা বা আলো জ্বলছে না।"
        },
        "default_action": {
            "en": "Clean/replace registration plate and fix illumination bulb.",
            "hi": "नंबर प्लेट साफ करें या बदलें और लाइट ठीक करें।",
            "bn": "নম্বর প্লেট পরিষ্কার করুন বা বদলান এবং বাতি মেরামত করুন।"
        }
    },
    "B4_REAR_GATE_LOCKING": {
        "side": "back",
        "names": {
            "en": "Rear Gate Mesh & Locking Latches",
            "hi": "पीछे का जालीदार गेट और लॉक कुंडी",
            "bn": "পেছনের জালের গেট ও লক ছিটকিনি"
        },
        "correct_spec": {
            "en": "Sturdy mesh frame with functional locking latch to ensure cylinder load cannot be displaced or opened in transit.",
            "hi": "मजबूत लोहे का जालीदार गेट और चालू लॉक कुंडी, ताकि रास्ते में सिलेंडर गिरे नहीं।",
            "bn": "শক্তিশালী জালের গেট এবং কার্যকর লক ছিটকিনি, যাতে যাত্রাপথে সিলিন্ডার না পড়ে।"
        },
        "default_defect": {
            "en": "Rear gate mesh broken, latch missing or unable to lock properly.",
            "hi": "गेट की जाली कटी हुई है, कुंडी टूटी है या लॉक नहीं लग रहा।",
            "bn": "গেটের জাল কাটা, ছিটকিনি ভাঙা বা লক আটকানো যাচ্ছে না।"
        },
        "default_action": {
            "en": "Weld mesh repair and replace broken gate latch/padlock.",
            "hi": "जाली की वेल्डिंग कराएं और मजबूत कुंडी/ताला लगाएं।",
            "bn": "জাল ওয়েল্ডিং করুন এবং মজবুত ছিটকিনি/তালা লাগান।"
        }
    }
}


def get_ui_text(key: str, lang: str = "en") -> str:
    """Retrieves UI text by key and language code."""
    lang_dict = UI_TEXT.get(lang, UI_TEXT["en"])
    return lang_dict.get(key, UI_TEXT["en"].get(key, key))


def localize_item(item: Dict[str, Any], lang: str = "en") -> Dict[str, Any]:
    """
    Returns a normalized, fully translated dictionary for a checklist row,
    including 'side', 'name', 'status', 'what_is_correct', 'what_is_wrong',
    and 'action'.
    """
    rule_id = item.get("id", "")
    rule_info = RULE_TRANSLATIONS.get(rule_id, {})
    side_key = rule_info.get("side", item.get("side", "front"))
    status = item.get("status", "PASS")

    # Localized side information
    side_meta = SIDE_METADATA.get(side_key, SIDE_METADATA["front"])
    side_name = side_meta["names"].get(lang, side_meta["names"]["en"])
    side_short = side_meta["short_names"].get(lang, side_meta["short_names"]["en"])

    # Localized item name
    if rule_info and "names" in rule_info:
        item_name = rule_info["names"].get(lang, item.get("name", rule_id))
    else:
        item_name = item.get("name", rule_id)

    # What is correct (Standard Specification)
    if rule_info and "correct_spec" in rule_info:
        what_is_correct = rule_info["correct_spec"].get(lang, rule_info["correct_spec"]["en"])
    else:
        what_is_correct = item.get("required_compliance", "BPCL Standard Specification")

    # What is wrong (Vehicle condition)
    if status == "PASS":
        what_is_wrong = get_ui_text("no_defect_found", lang)
        action_text = get_ui_text("action_none", lang)
    else:
        # If there is a defect
        if rule_info and "default_defect" in rule_info:
            defect_template = rule_info["default_defect"].get(lang, rule_info["default_defect"]["en"])
        else:
            defect_template = item.get("defect_reason", item.get("observation", "Defect observed on vehicle"))

        # Check if item has custom observation or defect_reason from vision/auditor
        obs = item.get("observation", "")
        defect_r = item.get("defect_reason", "")
        
        # In English, keep original observation if descriptive; in Hindi/Bengali, use the high-quality localized defect
        if lang == "en":
            what_is_wrong = defect_r or obs or defect_template
        else:
            what_is_wrong = defect_template

        if rule_info and "default_action" in rule_info:
            action_text = rule_info["default_action"].get(lang, rule_info["default_action"]["en"])
        else:
            action_text = item.get("corrective_action", "Repair or replace per BPCL standard")

    # Status labels in language
    if status == "PASS":
        status_label = get_ui_text("status_compliant", lang)
        status_badge_html = f'<span style="background:#d1fae5; color:#065f46; border:1px solid #a7f3d0; padding:6px 14px; border-radius:6px; font-weight:800; font-size:13px; display:inline-block; white-space:nowrap;">✅ {status_label}</span>'
    elif status == "WARNING":
        status_label = get_ui_text("status_warning", lang)
        status_badge_html = f'<span style="background:#fef3c7; color:#92400e; border:1px solid #fde68a; padding:6px 14px; border-radius:6px; font-weight:800; font-size:13px; display:inline-block; white-space:nowrap;">⚠️ {status_label}</span>'
    else:
        status_label = get_ui_text("status_non_compliant", lang)
        status_badge_html = f'<span style="background:#fee2e2; color:#991b1b; border:1px solid #fecaca; padding:6px 14px; border-radius:6px; font-weight:800; font-size:13px; display:inline-block; white-space:nowrap;">❌ {status_label}</span>'

    return {
        "id": rule_id,
        "side_key": side_key,
        "side_name": side_name,
        "side_short": side_short,
        "side_icon": side_meta["icon"],
        "side_badge_bg": side_meta["badge_bg"],
        "side_badge_fg": side_meta["badge_fg"],
        "name": item_name,
        "status": status,
        "status_label": status_label,
        "status_badge_html": status_badge_html,
        "what_is_correct": what_is_correct,
        "what_is_wrong": what_is_wrong,
        "action": action_text
    }
