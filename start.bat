@echo off
REM Quick Start Script for Chanakya DSS (Windows Batch File)
REM Double-click this file to automatically set up and run the application

echo ============================================================
echo Chanakya Decision Intelligence System - Quick Start
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python detected
echo.

REM Check if virtual environment exists
if exist "venv\" (
    echo [OK] Virtual environment found
) else (
    echo [SETUP] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
)

echo.

REM Activate virtual environment and install dependencies
echo [SETUP] Installing dependencies...
call venv\Scripts\activate.bat
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    echo Try running: pip install -r requirements.txt
    pause
    exit /b 1
)

echo [OK] Dependencies installed
echo.

REM Launch the application
echo ============================================================
echo Starting Chanakya DSS...
echo The app will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo ============================================================
echo.

streamlit run app.py

pause
