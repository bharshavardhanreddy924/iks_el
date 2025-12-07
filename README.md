# Chanakyan Doctrine-Driven Decision Intelligence Model

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🏛️ Project Overview

A **Neuro-Symbolic AI System** that integrates ancient Indian strategic wisdom from **Chanakya's Arthashastra** with modern **Decision Intelligence** techniques to support governance and public policy optimization.

### 🎓 Academic Context

- **Institution:** RV College of Engineering
- **Department:** Artificial Intelligence and Machine Learning
- **Course:** Indian Knowledge System (HS271T)
- **Guide:** Dr. Lingayya Hiremath, Prof Biotechnology

### 👨‍💻 Team Members

1. **Kota Vishnu Datta** (1RV22AI024)
2. **Chillale Naveen** (1RV22AI013)
3. **Boru Harshavardhan Reddy** (1RV22AI065)
4. **Jaswanth Reddy M** (1RV22AI020)

---

## 🚀 Key Features

### 1. **Retrieval-Augmented Generation (RAG)**
- TF-IDF vectorization of Arthashastra corpus
- Cosine similarity-based semantic retrieval
- Dynamic doctrine matching to policy problems

### 2. **Multi-Criteria Decision Analysis (MCDA)**
- 5-dimensional policy evaluation framework
- Weighted scoring across:
  - Welfare Impact (Prajasukhe)
  - Economic Viability (Kosha)
  - Law & Order (Danda)
  - Political Stability (Mitra)
  - Implementation Feasibility

### 3. **Advanced Visualizations**
- **Radar Charts:** Multi-criteria policy trade-off analysis
- **Heatmaps:** RAG similarity scores across all doctrines
- **Saptanga Analysis:** Impact on seven limbs of state
- **Interactive Dashboards:** Real-time policy scoring

### 4. **LLM-Powered Analysis**
- Google Gemini integration (1.5-flash / 1.5-pro)
- Structured policy recommendations
- Sanskrit terminology integration
- Explainable AI outputs

---

## 🛠️ Technical Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Input Layer                          │
│              (Policy Problem Statement)                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  RAG Pipeline Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ TF-IDF       │→ │ Vectorization │→ │ Cosine       │      │
│  │ Tokenization │  │               │  │ Similarity   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            Knowledge Base (Arthashastra)                     │
│     15 Doctrines × 10 Domains × Policy Weights              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                LLM Inference Layer                           │
│          (Google Gemini with Retrieved Context)              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              MCDA Scoring & Visualization                    │
│    Radar Charts | Heatmaps | Saptanga Analysis              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               Policy Recommendation Output                   │
│         (Markdown Report + Downloadable Files)               │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))

### Step 1: Clone/Download the Project

```powershell
cd "c:\Users\borut\Desktop\iks el"
```

### Step 2: Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 4: Configure API Key

Create a `.env` file (or enter directly in the app):

```powershell
Copy-Item .env.example .env
# Edit .env and add your API key
```

Or simply enter your API key in the sidebar when you run the app.

### Step 5: Run the Application

```powershell
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📖 Usage Guide

### 1. **Policy Analysis Workflow**

1. **Select/Enter Problem:** Choose a sample problem or enter your own governance scenario
2. **Set Parameters:** Adjust MCDA sliders based on policy priorities
3. **Execute Pipeline:** Click "Execute Analysis Pipeline"
4. **Review Results:**
   - RAG retrieval shows matched Arthashastra doctrine
   - Visualizations display policy trade-offs
   - LLM generates detailed strategic recommendations
5. **Export Report:** Download as Markdown for documentation

### 2. **Knowledge Base Explorer**

- Browse all 15 Arthashastra doctrines
- Filter by governance domain
- View keywords and policy weights
- Understand the corpus structure

### 3. **Analytics Dashboard**

- View RAG similarity heatmaps
- Analyze top relevant doctrines
- Compare MCDA weighted scores
- Diagnostic insights into the decision process

---

## 🔬 Research Methodology

### Phase 1: Knowledge Extraction
- Identified 15 core Chanakyan doctrines
- Structured as computational knowledge graph
- Added keywords, domains, policy weights

### Phase 2: RAG Implementation
```python
# Core RAG Function
def rag_retrieval(query, top_k=2):
    # TF-IDF Vectorization
    tfidf_vectorizer = TfidfVectorizer(max_features=100, ngram_range=(1, 2))
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    
    # Cosine Similarity
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Return top match
    return best_match, confidence_score
```

### Phase 3: MCDA Framework
- 5 criteria with differential weights
- Governance Effectiveness Index (GEI) calculation
- Visual trade-off analysis

### Phase 4: LLM Integration
- Dynamic prompt construction with retrieved context
- Structured output format
- Sanskrit terminology grounding

---

## 📊 Sample Output

### Input Problem:
> "The state is facing a severe deficit in the electricity sector due to power theft and unpaid bills by rural consumers."

### RAG Retrieval:
> **Matched Doctrine:** Kosha Mula Danda (Treasury is Root of Power)  
> **Confidence:** 0.4523  
> **Domain:** Economic Policy

### Policy Recommendation (Excerpt):
```
### Strategic Diagnosis (समस्या निदान)

Root Cause: Systemic revenue leakage (अर्थक्षय) combined with 
enforcement deficit (दंडाभाव). Affects Kosha (Treasury) and 
Danda (Enforcement) limbs.

### Recommended Strategy

Primary Action: Implement tiered pricing with Sama-Dana (incentives 
for bill payment) before Danda (legal action).

Budget: ₹500 Cr for smart metering + ₹200 Cr for subsidies
Timeline: 18 months
Success Metric: 40% reduction in theft within 12 months
```

### Visualizations:
- **Radar Chart:** Shows high welfare priority, moderate enforcement
- **Saptanga Chart:** Identifies Kosha and Danda as critical limbs
- **Heatmap:** Displays similarity scores across all doctrines

---

## 🎯 Research Contributions

### 1. **Novel Dataset**
First structured digital corpus of Arthashastra for AI systems

### 2. **Hybrid Architecture**
Demonstrates practical integration of symbolic knowledge with neural models

### 3. **Applied ML**
Implements TF-IDF + Cosine Similarity for semantic doctrine retrieval

### 4. **Cultural AI**
Proves traditional knowledge systems can enhance modern AI applications

### 5. **Decision Intelligence**
Framework applicable across multiple governance domains

---

## 📚 Knowledge Corpus Structure

The system contains **15 doctrines** across **10 domains**:

| Domain | Example Doctrine | Keywords |
|--------|-----------------|----------|
| Economic Policy | Kosha Mula Danda | finance, budget, treasury |
| Social Welfare | Prajasukhe Sukham | welfare, happiness, citizens |
| Law & Order | Matsyanyaya | crime, enforcement, justice |
| Foreign Affairs | Mandala Theory | diplomacy, allies, enemies |
| Infrastructure | Durga | fortification, construction |
| Crisis Management | Vyasana | disaster, emergency, resilience |
| Strategic Methods | Sama-Dana-Bheda-Danda | tactics, negotiation |
| ... | ... | ... |

---

## 🎓 For Conference Presentation

### Talking Points:

1. **"We implemented a Retrieval-Augmented Generation (RAG) pipeline"**
   - Point to `rag_retrieval()` function in code
   - Explain TF-IDF → Cosine Similarity → Doctrine Matching

2. **"We use mathematical vectorization to map modern problems to ancient Sanskrit sutras"**
   - Show live demo of heatmap visualization
   - Emphasize explainability via similarity scores

3. **"Human-in-the-loop optimization via MCDA sliders"**
   - Demonstrate how sliders bias the model's recommendations
   - Show radar chart responding to parameter changes

4. **"Culturally-grounded AI instead of generic Western models"**
   - Compare outputs with/without Chanakyan context
   - Highlight Sanskrit terminology in generated text

### Demo Flow:
1. Show architecture diagram (5 min)
2. Live demo: Enter problem → RAG retrieval → Visualization → LLM output (10 min)
3. Show code: RAG function + MCDA scoring (5 min)
4. Q&A about methodology (10 min)

---

## 🧪 Testing & Validation

### Test Cases Included:

1. **Power Sector Crisis** → Economic Policy (Kosha)
2. **Healthcare Emergency** → Crisis Management (Vyasana)
3. **Agricultural Distress** → Agriculture & Resources (Janapada)
4. **Urban Water Crisis** → Infrastructure (Durga)

### Validation Metrics:
- RAG Precision: Does retrieved doctrine match problem domain?
- MCDA Consistency: Do scores align with policy priorities?
- Output Quality: Are recommendations actionable and grounded?

---

## 📈 Future Enhancements

1. **Expanded Corpus:** Add 50+ more Arthashastra verses
2. **Fine-tuned LLM:** Domain-specific model training
3. **Real-time Data Integration:** Connect to government APIs
4. **Multi-language Support:** Hindi, Sanskrit, regional languages
5. **Historical Case Studies:** Analyze past policies through Chanakyan lens
6. **Stakeholder Simulation:** Multi-agent modeling (Mandala Theory)

---

## 🤝 Contributing

This is an academic research project. For collaboration:
- Contact team via RV College of Engineering
- Submit issues/suggestions via project repository
- Cite this work in your research

---

## 📄 License

MIT License - Free for educational and research purposes.

---

## 📚 References

1. **Kautilya's Arthashastra** (300 BCE) - R. Shamasastry Translation
2. Davenport, T. (2022). *Decision Intelligence: A Practical Framework*
3. OECD (2023). *Explainable AI in Public Policy*
4. Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*
5. Saaty, T.L. (1980). *The Analytic Hierarchy Process* (MCDA methodology)

---

## 📧 Contact

**RV College of Engineering**  
Department of Artificial Intelligence and Machine Learning  
Bangalore, India

**Team Leads:**
- Kota Vishnu Datta: 7396755649
- Project Guide: Dr. Lingayya Hiremath

---

## 🙏 Acknowledgments

- Dr. Lingayya Hiremath for project guidance
- RV College of Engineering for infrastructure support
- Google for Gemini API access
- The ancient wisdom of Chanakya for timeless strategic insights

---

<div align="center">

**Integrating Ancient Wisdom with Modern AI for Better Governance**

*Built with ❤️ by the IKS Team | 2025*

</div>
