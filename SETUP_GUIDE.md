# SETUP_GUIDE.md

# Complete Setup Guide for Chanakya DSS

## 🎯 Quick Start (5 Minutes)

### Option 1: Windows PowerShell

```powershell
# Navigate to project directory
cd "c:\Users\borut\Desktop\iks el"

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Option 2: Command Prompt

```cmd
cd "c:\Users\borut\Desktop\iks el"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔧 Detailed Installation Steps

### Step 1: Verify Python Installation

Check if Python is installed:

```powershell
python --version
```

You should see `Python 3.9.x` or higher. If not, download from [python.org](https://www.python.org/downloads/).

### Step 2: Create Virtual Environment

Why? Isolates project dependencies from your system Python.

```powershell
python -m venv venv
```

This creates a `venv` folder in your project directory.

### Step 3: Activate Virtual Environment

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**If you get an execution policy error:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
venv\Scripts\activate
```

You should see `(venv)` prefix in your terminal.

### Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

This installs:
- `streamlit` - Web interface
- `google-generativeai` - Gemini API
- `pandas` - Data manipulation
- `scikit-learn` - TF-IDF and ML functions
- `plotly` - Interactive visualizations
- `numpy` - Numerical computing

**Installation takes ~2-3 minutes depending on internet speed.**

### Step 5: Get Google Gemini API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (looks like: `AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`)

**Two ways to use the key:**

**Option A: Enter in App (Recommended for testing)**
- Just run the app and paste in the sidebar

**Option B: Create .env file (Recommended for development)**
```powershell
Copy-Item .env.example .env
notepad .env
```

Add your key:
```
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### Step 6: Run the Application

```powershell
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 🚨 Troubleshooting

### Problem 1: "Python is not recognized"

**Solution:** Add Python to PATH

1. Search "Environment Variables" in Windows
2. Click "Environment Variables"
3. Under "System Variables", find "Path"
4. Add Python installation directory (e.g., `C:\Python39\`)
5. Restart terminal

### Problem 2: "Cannot activate virtual environment"

**Solution:** Change execution policy

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problem 3: "pip install fails"

**Solution 1:** Upgrade pip
```powershell
python -m pip install --upgrade pip
```

**Solution 2:** Use specific Python version
```powershell
python3.9 -m pip install -r requirements.txt
```

### Problem 4: "Streamlit command not found"

**Solution:** Ensure virtual environment is activated

```powershell
# Check if (venv) appears in prompt
# If not, activate again:
.\venv\Scripts\Activate.ps1

# Verify streamlit is installed:
pip list | Select-String streamlit
```

### Problem 5: "API Key Invalid"

**Checklist:**
- Did you copy the full key (including `AIza...`)?
- No extra spaces before/after the key?
- Is the key active? (Check Google AI Studio)
- Are you connected to the internet?

### Problem 6: "Module not found errors"

**Solution:** Reinstall dependencies

```powershell
pip install --force-reinstall -r requirements.txt
```

---

## 🎓 For First-Time Users

### What happens when I run the app?

1. **Streamlit starts a local web server** on port 8501
2. **Browser opens automatically** showing the interface
3. **You can now interact** with the system

### Understanding the Interface

**Sidebar (Left):**
- Team information
- API key input
- Model configuration
- System status

**Main Area (Center):**
- 4 tabs: Policy Analysis, Knowledge Base, Analytics, About
- Input area for problems
- Sliders for policy parameters
- Results and visualizations

### First Test Run

1. **Don't enter your own problem yet**
2. **Select "Power Sector Crisis"** from dropdown
3. **Leave sliders at default**
4. **Enter your API key** in sidebar
5. **Click "Execute Analysis Pipeline"**
6. **Wait 15-20 seconds** for results

You should see:
- RAG retrieval information
- Retrieved Arthashastra doctrine
- Radar chart visualization
- Generated policy analysis

---

## 📊 Verifying Installation

### Run this checklist:

```powershell
# 1. Check Python
python --version
# Expected: Python 3.9.x or higher

# 2. Check virtual environment
.\venv\Scripts\Activate.ps1
# Expected: (venv) appears in prompt

# 3. Check installed packages
pip list
# Expected: See streamlit, google-generativeai, pandas, etc.

# 4. Check Streamlit
streamlit --version
# Expected: Streamlit, version 1.29.0 or similar

# 5. Check project files
Get-ChildItem
# Expected: app.py, chanakya_wisdom.py, requirements.txt, etc.
```

---

## 🖥️ Running on Different Systems

### Windows (PowerShell/CMD)
✅ Already covered above

### macOS / Linux

```bash
cd "/path/to/iks el"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### Google Colab (Online, No Installation)

```python
# Install dependencies
!pip install streamlit google-generativeai pandas scikit-learn plotly

# Run with tunneling
!streamlit run app.py & npx localtunnel --port 8501
```

---

## 🔒 Security Best Practices

### API Key Safety

**DO:**
- ✅ Use `.env` file (add to `.gitignore`)
- ✅ Enter key directly in app for temporary use
- ✅ Rotate keys periodically

**DON'T:**
- ❌ Commit API keys to Git
- ❌ Share keys in screenshots
- ❌ Hard-code keys in source files

### Verify .gitignore

Check that `.gitignore` includes:
```
.env
```

---

## 📦 File Structure After Setup

```
c:\Users\borut\Desktop\iks el\
│
├── venv/                      # Virtual environment (auto-generated)
│   ├── Lib/
│   ├── Scripts/
│   └── ...
│
├── app.py                     # Main Streamlit application
├── chanakya_wisdom.py         # Knowledge corpus + RAG functions
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── SETUP_GUIDE.md            # This file
├── .env.example              # Template for environment variables
├── .env                      # Your actual API key (create this)
└── .gitignore                # Git ignore rules
```

---

## 🚀 Performance Optimization

### For Faster Loading

1. **Use gemini-1.5-flash** (faster, cheaper)
2. **Reduce temperature** slider (less creative = faster)
3. **Enable "Brief Mode"** in sidebar

### For Better Results

1. **Use gemini-1.5-pro** (more accurate)
2. **Increase temperature** to 0.6-0.7
3. **Disable "Brief Mode"**
4. **Provide detailed problem statements**

---

## 🎯 Next Steps After Setup

### 1. Test with Sample Problems
Run all 4 sample problems to see different doctrines retrieved

### 2. Explore Knowledge Base
Tab 2 shows all 15 Arthashastra doctrines

### 3. Analyze Your Own Problem
Enter a real governance challenge from your region

### 4. Experiment with Parameters
Adjust MCDA sliders to see how recommendations change

### 5. Export Reports
Download generated analyses as Markdown files

---

## 🆘 Getting Help

### If you're stuck:

1. **Read error messages carefully** - they usually tell you what's wrong
2. **Check this guide's Troubleshooting section**
3. **Verify all files are present** (app.py, chanakya_wisdom.py, etc.)
4. **Ensure internet connection** for API calls
5. **Try restarting the terminal** and running again

### Common Commands to Remember

```powershell
# Activate environment
.\venv\Scripts\Activate.ps1

# Run app
streamlit run app.py

# Stop app
# Press Ctrl+C in terminal

# Deactivate environment
deactivate

# Reinstall dependencies
pip install -r requirements.txt
```

---

## ✅ Setup Complete Checklist

- [ ] Python 3.9+ installed
- [ ] Virtual environment created (`venv` folder exists)
- [ ] Virtual environment activated (`(venv)` in prompt)
- [ ] Dependencies installed (no errors during `pip install`)
- [ ] API key obtained from Google AI Studio
- [ ] API key entered in app or `.env` file
- [ ] Streamlit app runs (`streamlit run app.py`)
- [ ] Browser opens to `http://localhost:8501`
- [ ] Sample problem analysis works successfully

**If all checked, you're ready to use the system! 🎉**

---

## 📞 Support

For technical issues related to:
- **Streamlit:** https://docs.streamlit.io/
- **Gemini API:** https://ai.google.dev/docs
- **This project:** Contact team via RV College of Engineering

---

*Last Updated: 2025 | For RV College IKS Project*
