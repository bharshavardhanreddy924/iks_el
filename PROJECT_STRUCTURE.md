# Project Structure

## Overview
This document outlines the complete architecture of the Chanakyan Decision Intelligence System.

## Directory Structure

```
iks-el/
│
├── app.py                          # Main Streamlit application
│   ├── UI Components
│   ├── Tab Navigation (4 tabs)
│   ├── RAG Pipeline Integration
│   └── Visualization Generation
│
├── chanakya_wisdom.py             # Knowledge Corpus Module
│   ├── KNOWLEDGE_CORPUS (15 doctrines)
│   ├── SYSTEM_PROMPT (LLM prompt engineering)
│   ├── MCDA_CRITERIA (scoring framework)
│   └── Helper Functions
│
├── requirements.txt               # Python dependencies
├── .env.example                  # Environment template
├── .gitignore                    # Git exclusions
├── README.md                     # Project documentation
├── SETUP_GUIDE.md               # Installation instructions
└── PROJECT_STRUCTURE.md         # This file

```

## Module Breakdown

### 1. app.py (Main Application)

**Imports:**
- `streamlit` - Web UI framework
- `google.generativeai` - LLM API
- `sklearn.feature_extraction.text` - TF-IDF vectorization
- `sklearn.metrics.pairwise` - Cosine similarity
- `plotly.graph_objects` - Interactive visualizations
- `pandas`, `numpy` - Data processing

**Core Functions:**

#### `rag_retrieval(query, top_k=2)`
**Purpose:** Implements Retrieval-Augmented Generation
**Process:**
1. Converts user query and corpus to TF-IDF vectors
2. Calculates cosine similarity scores
3. Returns top matching doctrine(s)

**Parameters:**
- `query` (str): User's problem statement
- `top_k` (int): Number of matches to return

**Returns:**
- `df_row`: Matched doctrine data
- `conf_score`: Confidence score (0-1)
- `all_scores`: Similarity scores for all doctrines

**Research Significance:** Core ML component demonstrating semantic retrieval

---

#### `generate_radar_chart(welfare, economic, law_order, political, implementation)`
**Purpose:** MCDA visualization using radar/spider chart
**Process:**
1. Creates polar coordinate system
2. Maps 5 policy dimensions
3. Fills area to show policy profile

**Returns:** Plotly Figure object

**Research Significance:** Multi-criteria trade-off visualization

---

#### `generate_heatmap(df_corpus, similarity_scores)`
**Purpose:** Visualize RAG relevance across all doctrines
**Process:**
1. Creates matrix of similarity scores
2. Color-codes by relevance
3. Labels each doctrine

**Returns:** Plotly heatmap

**Research Significance:** Demonstrates RAG transparency

---

#### `generate_saptanga_analysis(policy_scores)`
**Purpose:** Seven Limbs of State impact assessment
**Process:**
1. Maps policy scores to Saptanga elements
2. Creates bar chart with color coding
3. Highlights critical areas

**Returns:** Plotly bar chart

**Research Significance:** Integration of traditional framework with modern analytics

---

#### `calculate_governance_index(scores)`
**Purpose:** Compute weighted Governance Effectiveness Index (GEI)
**Formula:** GEI = Σ(score_i × weight_i)

**Research Significance:** Quantitative policy evaluation metric

---

### 2. chanakya_wisdom.py (Knowledge Module)

#### Data Structures:

**KNOWLEDGE_CORPUS** (List of Dicts)
```python
{
    "id": int,                    # Unique identifier
    "doctrine": str,              # Name in Sanskrit + English
    "text": str,                  # Full doctrine explanation
    "keywords": str,              # Space-separated keywords for TF-IDF
    "domain": str,                # Governance domain classification
    "policy_weight": float        # Importance weight (0-1)
}
```

**Total Corpus Size:** 15 doctrines × 10 domains

**Domains Covered:**
1. Analysis & Planning
2. Economic Policy
3. Social Welfare
4. Law & Order
5. Foreign Affairs
6. Infrastructure
7. Strategic Methods
8. Governance Structure
9. Crisis Management
10. Agriculture & Resources

---

#### Prompt Engineering:

**SYSTEM_PROMPT** (Research-Grade Template)
- Structured output format
- Sanskrit terminology integration
- Saptanga impact analysis
- MCDA scoring requirements
- Ethical considerations
- Risk mitigation framework (Sama-Dana-Bheda-Danda)

**BRIEF_SYSTEM_PROMPT** (Quick Analysis Mode)
- Concise 3-paragraph format
- Faster inference
- Essential recommendations only

---

#### MCDA Framework:

**MCDA_CRITERIA** (Dict)
```python
{
    "welfare_impact": {"weight": 0.30, ...},
    "economic_viability": {"weight": 0.25, ...},
    "law_order": {"weight": 0.20, ...},
    "political_stability": {"weight": 0.15, ...},
    "implementation_speed": {"weight": 0.10, ...}
}
```

**Total Weight:** 1.0 (normalized)

**Interpretation:**
- Welfare prioritized (30%)
- Economic feasibility important (25%)
- Enforcement capability (20%)
- Political considerations (15%)
- Speed/feasibility (10%)

---

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────┐
│ USER INPUT                                               │
│ - Problem statement (text)                              │
│ - MCDA sliders (5 parameters)                           │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ PREPROCESSING                                            │
│ - Text tokenization                                      │
│ - TF-IDF vectorization (100 features, unigrams+bigrams) │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ RAG RETRIEVAL                                            │
│ - Load KNOWLEDGE_CORPUS (15 doctrines)                  │
│ - Calculate cosine_similarity(query, corpus)            │
│ - Sort by score, select top match                       │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ PROMPT CONSTRUCTION                                      │
│ - SYSTEM_PROMPT template                                │
│ - Inject retrieved doctrine context                     │
│ - Add user problem + MCDA parameters                    │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ LLM INFERENCE                                            │
│ - API call to Google Gemini                             │
│ - Temperature, top_p parameters                         │
│ - Generate structured response                          │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ POST-PROCESSING                                          │
│ - Calculate GEI score                                   │
│ - Generate radar chart                                  │
│ - Generate heatmap                                      │
│ - Generate Saptanga chart                               │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ OUTPUT                                                   │
│ - Textual policy analysis                               │
│ - Interactive visualizations                            │
│ - Downloadable reports                                  │
└─────────────────────────────────────────────────────────┘
```

---

## Key Design Decisions

### 1. Why TF-IDF + Cosine Similarity?

**Advantages:**
- Lightweight (no GPU required)
- Interpretable (clear similarity scores)
- Fast inference (<1 second)
- No training required
- Reproducible results

**Research Justification:**
Classic NLP baseline, suitable for small corpus (<100 documents)

**Alternative Considered:**
- Sentence-BERT embeddings (more accurate but heavier)
- Fine-tuned language models (requires training data)

---

### 2. Why Structured Prompts?

**Purpose:**
- Enforce consistent output format
- Enable downstream parsing
- Improve reproducibility
- Support academic evaluation

**Structure:**
1. Diagnosis (root cause)
2. Doctrinal framework
3. Multiple policy options with scores
4. Recommended strategy
5. Risk mitigation
6. Ethical considerations

---

### 3. Why Plotly?

**Advantages:**
- Interactive (zoom, hover, pan)
- Publication-quality exports
- Integrates with Streamlit
- Supports complex chart types

**Charts Used:**
- Radar chart (MCDA)
- Heatmap (RAG similarity)
- Bar chart (Saptanga)
- All configurable and styled

---

## Session State Management

**Streamlit Session State Variables:**

```python
st.session_state = {
    'result': str,              # Generated policy analysis
    'rag_doc': dict,            # Retrieved doctrine metadata
    'scores': list[float],      # MCDA parameter values
    'problem': str,             # User's input problem
    'gei': float,               # Governance Effectiveness Index
    'all_similarity_scores': np.array,  # RAG scores for all doctrines
    'timestamp': datetime       # When analysis was run
}
```

**Purpose:** Persist results across Streamlit reruns

---

## API Integration

**Google Gemini Configuration:**

```python
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',  # or gemini-1.5-pro
    generation_config={
        "temperature": 0.4,          # Creativity (0-1)
        "top_p": 0.8,                # Nucleus sampling
        "max_output_tokens": 2048    # Response length
    }
)
```

**Error Handling:**
- API key validation
- Connection timeout handling
- Rate limit management
- Graceful degradation

---

## Performance Characteristics

### Computational Complexity:

**RAG Retrieval:**
- TF-IDF: O(n × m) where n=corpus size, m=vocab size
- Cosine Similarity: O(n × d) where d=feature dimensions
- **Total:** ~0.5 seconds for 15 doctrines

**LLM Inference:**
- API latency: 5-15 seconds (depends on response length)
- Temperature impact: Higher = slightly slower

**Visualization:**
- Plotly rendering: <1 second per chart
- Streamlit rerun: ~2 seconds

**Total Workflow Time:** 10-20 seconds

---

### Memory Usage:

- Base Streamlit app: ~50 MB
- TF-IDF vectors: ~2 MB
- Session state: ~1 MB
- **Total:** <100 MB (very lightweight)

---

## Testing Strategy

### Unit Tests (Recommended):

```python
def test_rag_retrieval():
    query = "budget deficit crisis"
    doc, score, _ = rag_retrieval(query)
    assert doc['domain'] == "Economic Policy"
    assert score > 0.2

def test_mcda_scoring():
    scores = [8, 6, 7, 5, 6]
    gei = calculate_governance_index(scores)
    assert 0 <= gei <= 10

def test_corpus_integrity():
    df = get_corpus_df()
    assert len(df) == 15
    assert all(df['policy_weight'] <= 1.0)
```

---

### Integration Tests:

1. **End-to-end workflow:** Input → RAG → LLM → Visualization
2. **Sample problems:** All 4 sample cases should produce valid outputs
3. **Parameter sensitivity:** Change MCDA sliders, verify GEI changes
4. **Edge cases:** Empty input, invalid API key, network failure

---

## Deployment Considerations

### Local Deployment (Current):
- Streamlit on localhost:8501
- Single-user mode
- No authentication required

### Production Deployment (Future):

**Option 1: Streamlit Cloud**
- Free tier available
- Automatic HTTPS
- GitHub integration
- Secrets management

**Option 2: Docker Container**
```dockerfile
FROM python:3.9-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["streamlit", "run", "app.py"]
```

**Option 3: AWS/Azure/GCP**
- VM with Streamlit
- Load balancer for scaling
- Database for session persistence

---

## Security Considerations

### API Key Protection:
- Never commit `.env` to Git
- Use environment variables in production
- Rotate keys periodically
- Monitor API usage

### Input Validation:
- Sanitize user inputs before LLM calls
- Limit input length (prevent abuse)
- Rate limiting (future enhancement)

### Output Safety:
- No personal data in generated reports
- Disclaimer about AI-generated content
- Human review recommended for critical decisions

---

## Research Contribution Summary

### 1. Novel Architecture
Hybrid neuro-symbolic system combining:
- Classical ML (TF-IDF, cosine similarity)
- Modern LLMs (Gemini)
- Traditional knowledge (Arthashastra)

### 2. Evaluation Framework
- Quantitative: GEI score, similarity scores
- Qualitative: Expert review of recommendations
- Visual: Multiple chart types for transparency

### 3. Domain Adaptation
Successfully adapted ancient strategic principles to:
- Modern governance problems
- Computational representation
- Explainable AI outputs

### 4. Open Source Contribution
- Complete codebase for replication
- Documented methodology
- Extensible architecture

---

## Future Work

### Short-term:
1. Add more doctrines (30+ total)
2. Multi-language support
3. Export to PDF/DOCX
4. User authentication

### Medium-term:
1. Fine-tune custom LLM on Arthashastra
2. Real-time data integration (government APIs)
3. Historical case study database
4. Comparative analysis mode

### Long-term:
1. Multi-agent simulation (Mandala Theory)
2. Predictive policy modeling
3. Integration with GIS for spatial analysis
4. Mobile application

---

## Citation

If using this system in research, please cite:

```bibtex
@software{chanakya_dss_2025,
  title={Chanakyan Doctrine-Driven Decision Intelligence Model},
  author={Datta, Kota Vishnu and Naveen, Chillale and Reddy, Boru Harshavardhan and Reddy, Jaswanth M},
  year={2025},
  institution={RV College of Engineering},
  course={Indian Knowledge System (HS271T)},
  supervisor={Hiremath, Lingayya}
}
```

---

*This document is maintained as part of the IKS project documentation.*
*Last updated: 2025*
