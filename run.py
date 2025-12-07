"""
Quick Launch Script for Chanakya DSS
=====================================

This script automates the setup and launch process.
Run this instead of manually typing commands.

Usage:
    python run.py
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.9 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print(f"❌ Error: Python 3.9+ required, but you have {version.major}.{version.minor}")
        print("   Download from: https://www.python.org/downloads/")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_venv():
    """Check if virtual environment exists."""
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Virtual environment found")
        return True
    else:
        print("⚠️  Virtual environment not found")
        return False

def create_venv():
    """Create virtual environment."""
    print("\n🔧 Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False

def install_dependencies():
    """Install required packages."""
    print("\n📦 Installing dependencies...")
    
    # Determine pip path based on OS
    if sys.platform == "win32":
        pip_path = Path("venv/Scripts/pip.exe")
    else:
        pip_path = Path("venv/bin/pip")
    
    if not pip_path.exists():
        print("❌ Pip not found in virtual environment")
        return False
    
    try:
        subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_api_key():
    """Check if API key is configured."""
    env_file = Path(".env")
    if env_file.exists():
        with open(env_file) as f:
            content = f.read()
            if "GOOGLE_API_KEY" in content and "your_api_key_here" not in content:
                print("✅ API key configured in .env")
                return True
    
    print("⚠️  API key not found in .env file")
    print("   You can enter it in the app's sidebar instead")
    return False

def launch_app():
    """Launch the Streamlit application."""
    print("\n🚀 Launching Chanakya DSS...")
    print("=" * 60)
    print("The app will open in your browser at http://localhost:8501")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Determine streamlit path based on OS
    if sys.platform == "win32":
        streamlit_path = Path("venv/Scripts/streamlit.exe")
    else:
        streamlit_path = Path("venv/bin/streamlit")
    
    if not streamlit_path.exists():
        print("❌ Streamlit not found. Try reinstalling dependencies.")
        return False
    
    try:
        subprocess.run([str(streamlit_path), "run", "app.py"])
        return True
    except KeyboardInterrupt:
        print("\n\n✅ Application stopped")
        return True
    except Exception as e:
        print(f"❌ Failed to launch app: {e}")
        return False

def main():
    """Main execution flow."""
    print("=" * 60)
    print("Chanakya Decision Intelligence System - Quick Launch")
    print("=" * 60)
    print()
    
    # Step 1: Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Step 2: Check/create virtual environment
    if not check_venv():
        response = input("\nCreate virtual environment? (y/n): ").lower()
        if response == 'y':
            if not create_venv():
                sys.exit(1)
        else:
            print("❌ Cannot proceed without virtual environment")
            sys.exit(1)
    
    # Step 3: Check/install dependencies
    print("\n📋 Checking dependencies...")
    
    # Try to import streamlit to see if already installed
    try:
        if sys.platform == "win32":
            sys.path.insert(0, str(Path("venv/Lib/site-packages")))
        else:
            sys.path.insert(0, str(Path("venv/lib/python3.9/site-packages")))
        
        import streamlit
        print("✅ Dependencies already installed")
    except ImportError:
        print("⚠️  Dependencies not installed")
        response = input("Install dependencies? (y/n): ").lower()
        if response == 'y':
            if not install_dependencies():
                sys.exit(1)
        else:
            print("❌ Cannot proceed without dependencies")
            sys.exit(1)
    
    # Step 4: Check API key (optional)
    check_api_key()
    
    # Step 5: Launch
    print("\n" + "=" * 60)
    response = input("Launch application? (y/n): ").lower()
    if response == 'y':
        launch_app()
    else:
        print("\n✅ Setup complete. Run 'streamlit run app.py' to launch.")

if __name__ == "__main__":
    main()
