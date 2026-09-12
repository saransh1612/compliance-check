@echo off
title BPCL LPG Packed Truck Compliance Inspector
echo ===============================================================
echo Starting Bharat Petroleum LPG Packed Truck Compliance Inspector
echo ===============================================================
echo.
cd /d "%~dp0"
py -3 -m streamlit run app.py
pause
