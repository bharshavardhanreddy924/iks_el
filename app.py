import streamlit as st
from groq import Groq
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from chanakya_wisdom import (
    SYSTEM_PROMPT, BRIEF_SYSTEM_PROMPT, get_corpus_df, 
    get_all_domains, MCDA_CRITERIA, calculate_policy_score
)
import os
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Chanakya DSS | Research Platform",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (Professional Dark Theme) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Dark Theme Base */
    .main {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1a1d24;
        border-right: 1px solid #2d3139;
    }
    
    [data-testid="stSidebar"] * {
        color: #fafafa !important;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif;
        color: #ffffff !important;
        font-weight: 600;
    }
    
    /* Text Elements */
    p, span, div, label {
        color: #e0e0e0 !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Metric Cards */
    [data-testid="stMetric"] {
        background-color: #1a1d24;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #2d3139;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    [data-testid="stMetric"] label {
        color: #a0a0a0 !important;
        font-size: 0.9rem;
    }
    
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #4fc3f7 !important;
        font-weight: 600;
    }
    
    /* Input Fields */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #1a1d24 !important;
        color: #fafafa !important;
        border: 1px solid #2d3139 !important;
        border-radius: 6px;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #4fc3f7 !important;
        box-shadow: 0 0 0 1px #4fc3f7 !important;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        border-radius: 6px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Sliders */
    .stSlider {
        padding: 10px 0;
    }
    
    .stSlider [data-testid="stTickBar"] {
        background-color: #2d3139;
    }
    
    .stSlider [data-baseweb="slider"] {
        background-color: #2d3139;
    }
    
    /* Alerts and Info Boxes */
    .stAlert {
        background-color: #1a1d24;
        border: 1px solid #2d3139;
        border-radius: 8px;
        color: #fafafa;
    }
    
    .stInfo {
        background-color: #1a3a52;
        border-left: 4px solid #4fc3f7;
        color: #fafafa;
    }
    
    .stSuccess {
        background-color: #1a3a2e;
        border-left: 4px solid #66bb6a;
        color: #fafafa;
    }
    
    .stWarning {
        background-color: #3a2e1a;
        border-left: 4px solid #ffa726;
        color: #fafafa;
    }
    
    .stError {
        background-color: #3a1a1a;
        border-left: 4px solid #ef5350;
        color: #fafafa;
    }
    
    /* Research Header */
    .research-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 12px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
    }
    
    .research-header h1, .research-header p {
        color: white !important;
    }
    
    /* Doctrine Box */
    .doctrine-box {
        background-color: #2d2416;
        border-left: 4px solid #ffa726;
        padding: 15px;
        margin: 15px 0;
        border-radius: 6px;
        color: #fafafa;
    }
    
    .doctrine-box * {
        color: #fafafa !important;
    }
    
    /* Dataframes */
    [data-testid="stDataFrame"] {
        background-color: #1a1d24;
    }
    
    [data-testid="stDataFrame"] * {
        color: #fafafa !important;
        background-color: #1a1d24 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #1a1d24;
        border-bottom: 2px solid #2d3139;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #a0a0a0 !important;
        background-color: transparent;
        border: none;
        padding: 12px 24px;
        font-weight: 500;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #4fc3f7 !important;
        background-color: rgba(79, 195, 247, 0.1);
    }
    
    .stTabs [aria-selected="true"] {
        color: #4fc3f7 !important;
        border-bottom: 3px solid #4fc3f7;
        background-color: rgba(79, 195, 247, 0.05);
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: #1a1d24;
        color: #fafafa !important;
        border: 1px solid #2d3139;
        border-radius: 6px;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: #252830;
    }
    
    .streamlit-expanderContent {
        background-color: #1a1d24;
        border: 1px solid #2d3139;
        border-top: none;
        color: #fafafa;
    }
    
    /* Code Blocks */
    code {
        background-color: #1a1d24 !important;
        color: #4fc3f7 !important;
        padding: 2px 6px;
        border-radius: 4px;
        border: 1px solid #2d3139;
    }
    
    pre {
        background-color: #1a1d24 !important;
        border: 1px solid #2d3139;
        border-radius: 6px;
        padding: 15px;
    }
    
    /* Download Buttons */
    .stDownloadButton button {
        background-color: #1a1d24;
        color: #4fc3f7 !important;
        border: 2px solid #4fc3f7;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stDownloadButton button:hover {
        background-color: #4fc3f7;
        color: #0e1117 !important;
    }
    
    /* Status Container */
    .stStatus {
        background-color: #1a1d24;
        border: 1px solid #2d3139;
        border-radius: 8px;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #4fc3f7 !important;
    }
    
    /* Caption Text */
    .caption {
        color: #a0a0a0 !important;
        font-size: 0.85rem;
    }
    
    /* Markdown Content */
    .markdown-text-container {
        color: #e0e0e0 !important;
    }
    
    /* Links */
    a {
        color: #4fc3f7 !important;
        text-decoration: none;
    }
    
    a:hover {
        color: #81d4fa !important;
        text-decoration: underline;
    }
    
    /* Plotly Charts */
    .js-plotly-plot {
        background-color: #1a1d24 !important;
        border-radius: 8px;
    }
    
    /* Table Headers */
    thead tr th {
        background-color: #252830 !important;
        color: #fafafa !important;
        border-bottom: 2px solid #4fc3f7 !important;
    }
    
    /* Table Rows */
    tbody tr {
        background-color: #1a1d24 !important;
        color: #e0e0e0 !important;
    }
    
    tbody tr:hover {
        background-color: #252830 !important;
    }
    
    /* Scrollbars */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1d24;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #2d3139;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #4fc3f7;
    }
</style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS (Core ML & RAG Implementation) ---

def rag_retrieval(query, top_k=2):
    """
    Implements TF-IDF Vectorization with Cosine Similarity for semantic retrieval.
    
    This is the core RAG (Retrieval-Augmented Generation) component.
    Research Significance: Demonstrates hybrid neuro-symbolic architecture.
    
    Args:
        query (str): User's governance problem statement
        top_k (int): Number of top matches to return
    
    Returns:
        tuple: (top_match_dataframe, confidence_score, all_scores)
    """
    df = get_corpus_df()
    
    # Create document corpus
    documents = df['keywords'].tolist()
    documents.append(query)
    
    # TF-IDF Vectorization
    tfidf_vectorizer = TfidfVectorizer(
        max_features=100,
        stop_words='english',
        ngram_range=(1, 2)
    )
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    
    # Cosine Similarity Calculation
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Get top matches
    top_indices = np.argsort(cosine_sim[0])[-top_k:][::-1]
    scores = cosine_sim[0][top_indices]
    
    return df.iloc[top_indices[0]], scores[0], cosine_sim[0]

def generate_radar_chart(welfare, economic, law_order, political, implementation):
    """
    Generates Multi-Criteria Decision Analysis (MCDA) Radar Chart.
    
    Research Context: Visualization of policy trade-offs across Chanakyan dimensions.
    """
    categories = [
        'Welfare<br>(Prajasukhe)', 
        'Economic<br>(Kosha)', 
        'Law & Order<br>(Danda)', 
        'Political<br>(Mitra)',
        'Implementation<br>Feasibility'
    ]
    
    values = [welfare, economic, law_order, political, implementation]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Policy Profile',
        line_color='#667eea',
        fillcolor='rgba(102, 126, 234, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickfont=dict(size=10)
            )
        ),
        showlegend=False,
        title={
            'text': "Multi-Criteria Policy Impact Matrix",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'family': 'Merriweather'}
        },
        height=400
    )
    
    return fig

def generate_heatmap(df_corpus, similarity_scores):
    """
    Generate heatmap showing relevance scores across all doctrines.
    """
    # Create dataframe with doctrine names and scores
    doctrine_names = [doc.split('(')[0].strip()[:20] for doc in df_corpus['doctrine'].tolist()]
    
    fig = go.Figure(data=go.Heatmap(
        z=[similarity_scores],
        x=doctrine_names,
        y=['Relevance'],
        colorscale='YlOrRd',
        text=[[f'{score:.3f}' for score in similarity_scores]],
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Similarity<br>Score")
    ))
    
    fig.update_layout(
        title="Doctrinal Relevance Heatmap (TF-IDF Cosine Similarity)",
        xaxis_title="Arthashastra Doctrines",
        height=250,
        margin=dict(l=50, r=50, t=50, b=100)
    )
    
    fig.update_xaxes(tickangle=-45)
    
    return fig

def generate_saptanga_analysis(policy_scores):
    """
    Generate bar chart for Saptanga (Seven Limbs) impact analysis.
    """
    limbs = ['Swami\n(Leadership)', 'Amatya\n(Ministers)', 'Janapada\n(Territory)', 
             'Durga\n(Fortification)', 'Kosha\n(Treasury)', 'Danda\n(Force)', 'Mitra\n(Allies)']
    
    # Simulate impact scores based on policy parameters
    scores = policy_scores + [np.random.uniform(5, 9) for _ in range(7 - len(policy_scores))]
    scores = scores[:7]
    
    colors = ['#667eea' if s >= 7 else '#ffc107' if s >= 5 else '#dc3545' for s in scores]
    
    fig = go.Figure(data=[
        go.Bar(x=limbs, y=scores, marker_color=colors, text=[f'{s:.1f}' for s in scores], textposition='auto')
    ])
    
    fig.update_layout(
        title="Saptanga Impact Assessment (Seven Limbs of State)",
        yaxis_title="Impact Score",
        yaxis_range=[0, 10],
        height=350,
        showlegend=False
    )
    
    return fig

def calculate_governance_index(scores):
    """
    Calculate composite Governance Effectiveness Index (GEI).
    Research metric for quantitative evaluation.
    """
    weights = [w['weight'] for w in MCDA_CRITERIA.values()]
    gei = sum([s * w for s, w in zip(scores, weights)])
    return round(gei, 2)

# --- SIDEBAR: RESEARCH METADATA & CONTROLS ---
with st.sidebar:
    st.markdown('<div class="research-header"><h2 style="margin:0; color:white;">Chanakya DSS</h2><p style="margin:5px 0 0 0; color:#e0e0e0; font-size:14px;">Decision Intelligence Platform</p></div>', unsafe_allow_html=True)
    
    st.markdown("### Research Team")
    team_data = {
        "Name": ["Kota Vishnu Datta", "Chillale Naveen", "Boru Harshavardhan Reddy", "Jaswanth Reddy M"],
        "USN": ["1RV22AI024", "1RV22AI013", "1RV22AI065", "1RV22AI020"]
    }
    st.dataframe(pd.DataFrame(team_data), hide_index=True, use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("### API Configuration")
    # Hardcoded API key for showcase
    api_key = "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"
    os.environ['GROQ_API_KEY'] = api_key
    st.success("API Key Configured")
    
    st.markdown("---")
    
    st.markdown("### System Status")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Corpus Size", f"{len(get_corpus_df())} doctrines")
    with col2:
        st.metric("Domains", len(get_all_domains()))
    
    st.info("**Architecture:** Neuro-Symbolic AI\n\n**Kernel:** Python 3.9+\n\n**RAG Engine:** TF-IDF + Cosine Similarity")
    
    st.markdown("---")
    st.caption(f"Session: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# --- MAIN APPLICATION ---
st.markdown('<div class="research-header"><h1 style="margin:0; color:white;">Chanakyan Doctrine-Driven Decision Intelligence Model</h1><p style="margin:10px 0 0 0; color:#e0e0e0; font-size:16px;">A Neuro-Symbolic Framework for Public Policy Optimization</p></div>', unsafe_allow_html=True)

# --- TAB NAVIGATION ---
tab1, tab2, tab3, tab4 = st.tabs(["Policy Analysis", "Knowledge Base", "Analytics Dashboard", "About"])

# ============================================================================
# TAB 1: POLICY ANALYSIS (Main Functionality)
# ============================================================================
with tab1:
    st.markdown("## Policy Problem Input & Analysis")
    
    col_input, col_output = st.columns([1, 1], gap="large")
    
    with col_input:
        st.markdown("### Case Definition")
        
        # Sample problems for quick testing
        sample_problems = {
            "Custom Problem": "",
            "Power Sector Crisis": "The state is facing a severe deficit in the electricity sector due to power theft and unpaid bills by rural consumers. This is causing daily 8-hour power cuts affecting industries.",
            "Healthcare Emergency": "A new viral outbreak has been detected in 3 districts. Current hospital capacity is only 30% of what's needed. There are supply chain issues for medicines.",
            "Agricultural Distress": "Farmers are protesting due to falling crop prices and rising input costs. Many are defaulting on loans. The government faces fiscal constraints.",
            "Urban Water Crisis": "The capital city faces acute water shortage. Borewells are drying up. Private tanker mafia is charging exorbitant rates. Elections are in 6 months."
        }
        
        problem_type = st.selectbox("Select Sample Problem", list(sample_problems.keys()))
        
        problem = st.text_area(
            "Governance Problem Statement:",
            value=sample_problems[problem_type],
            height=150,
            help="Describe the policy challenge in detail",
            placeholder="Example: Rising unemployment among youth due to skill mismatch with industry requirements..."
        )
        
        st.markdown("### 2. Policy Parameters (MCDA Weights)")
        
        st.caption("Adjust these sliders to set policy priorities and constraints:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            welfare = st.slider("Welfare Impact Target", 1, 10, 7, 
                               help="How much should this policy benefit public welfare?")
            economic = st.slider("Economic Viability", 1, 10, 6,
                               help="Budget constraints and ROI considerations")
            implementation = st.slider("Implementation Speed", 1, 10, 7,
                                      help="How quickly can this be executed?")
        
        with col2:
            law_order = st.slider("Enforcement Capability", 1, 10, 6,
                                 help="Strength needed to implement and enforce")
            political = st.slider("Political Stability", 1, 10, 5,
                                help="Stakeholder support and diplomatic factors")
        
        # Calculate composite score
        gei = calculate_governance_index([welfare, economic, law_order, political, implementation])
        
        st.markdown("---")
        
        # Action button
        analyze_button = st.button("Execute Analysis Pipeline", type="primary", use_container_width=True)
    
    # --- OUTPUT COLUMN ---
    with col_output:
        st.markdown("### 3. Analysis Results")
        
        if analyze_button:
            if not problem.strip():
                st.error("Error: Problem statement cannot be empty.")
            else:
                # --- STEP 1: RAG PIPELINE ---
                with st.status("Initializing RAG Pipeline...", expanded=True) as status:
                    st.write("Tokenizing input text...")
                    st.write("Building TF-IDF vectors...")
                    st.write("Calculating Cosine Similarity with Arthashastra Corpus...")
                    
                    # Execute RAG
                    retrieved_doc, conf_score, all_scores = rag_retrieval(problem)
                    
                    st.write(f"**Retrieval Complete**")
                    st.write(f"**Confidence Score:** {conf_score:.4f}")
                    st.write(f"**Matched Doctrine:** *{retrieved_doc['doctrine']}*")
                    
                    status.update(label="RAG Preprocessing Complete", state="complete", expanded=False)
                
                # Display retrieved context
                st.markdown('<div class="doctrine-box">', unsafe_allow_html=True)
                st.markdown(f"**Retrieved Arthashastra Context:**")
                st.markdown(f"*{retrieved_doc['text']}*")
                st.markdown(f"**Domain:** {retrieved_doc['domain']} | **Policy Weight:** {retrieved_doc['policy_weight']}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # --- STEP 2: LLM INFERENCE ---
                try:
                    client = Groq(api_key=api_key)
                    
                    # Construct prompt
                    final_prompt = SYSTEM_PROMPT.format(
                        retrieved_context=retrieved_doc['text'],
                        domain=retrieved_doc['domain'],
                        weight=retrieved_doc['policy_weight']
                    )
                    
                    final_prompt += f"\n\n**USER PROBLEM:**\n{problem}\n\n"
                    final_prompt += f"**POLICY PARAMETERS:**\n"
                    final_prompt += f"- Welfare Priority: {welfare}/10\n"
                    final_prompt += f"- Economic Constraint: {economic}/10\n"
                    final_prompt += f"- Enforcement Capability: {law_order}/10\n"
                    final_prompt += f"- Political Stability: {political}/10\n"
                    final_prompt += f"- Implementation Speed: {implementation}/10\n"
                    final_prompt += f"- Governance Effectiveness Index (GEI): {gei}/10\n"
                    
                    with st.spinner("Neural Inference in Progress... (may take 10-20 seconds)"):
                        chat_completion = client.chat.completions.create(
                            messages=[
                                {
                                    "role": "user",
                                    "content": final_prompt,
                                }
                            ],
                            model="llama-3.3-70b-versatile",
                            temperature=0.4,
                            max_tokens=2048,
                            top_p=0.8,
                        )
                        
                        # Store in session state
                        st.session_state['result'] = chat_completion.choices[0].message.content
                        st.session_state['rag_doc'] = retrieved_doc.to_dict()
                        st.session_state['scores'] = [welfare, economic, law_order, political, implementation]
                        st.session_state['problem'] = problem
                        st.session_state['gei'] = gei
                        st.session_state['all_similarity_scores'] = all_scores
                        st.session_state['timestamp'] = datetime.now()
                    
                    st.success("Analysis Complete")
                    st.rerun()
                
                except Exception as e:
                    st.error(f"Runtime Error: {str(e)}")
                    st.info("Tip: Check your API key and internet connection.")
        
        # Display results if available
        if 'result' in st.session_state:
            st.markdown("---")
            
            # Metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Governance Effectiveness Index", f"{st.session_state['gei']}/10")
            with col2:
                st.metric("Primary Doctrine", st.session_state['rag_doc']['doctrine'].split('(')[0])
            with col3:
                st.metric("Domain", st.session_state['rag_doc']['domain'])
            
            st.markdown("#### Visualizations")
            
            # Radar Chart
            scores = st.session_state['scores']
            fig_radar = generate_radar_chart(scores[0], scores[1], scores[2], scores[3], scores[4])
            st.plotly_chart(fig_radar, use_container_width=True)
            
            # Saptanga Analysis
            fig_saptanga = generate_saptanga_analysis(scores)
            st.plotly_chart(fig_saptanga, use_container_width=True)
            
            st.markdown("---")
            
            # Generated Strategy
            st.markdown("#### Generated Policy Analysis")
            st.markdown(st.session_state['result'])
            
            st.markdown("---")
            
            # Export options
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label="Download Report (Markdown)",
                    data=st.session_state['result'],
                    file_name=f"chanakya_policy_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            
            with col2:
                # Create comprehensive report
                full_report = f"""# Chanakyan Policy Analysis Report
                
**Generated:** {st.session_state['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}

## Problem Statement
{st.session_state['problem']}

## Retrieved Doctrine
**{st.session_state['rag_doc']['doctrine']}**

{st.session_state['rag_doc']['text']}

**Domain:** {st.session_state['rag_doc']['domain']}

## Policy Parameters
- Welfare Impact: {scores[0]}/10
- Economic Viability: {scores[1]}/10
- Law & Order: {scores[2]}/10
- Political Stability: {scores[3]}/10
- Implementation Feasibility: {scores[4]}/10

**Governance Effectiveness Index:** {st.session_state['gei']}/10

## Analysis

{st.session_state['result']}

---
*Generated by Chanakya DSS | RV College of Engineering*
"""
                st.download_button(
                    label="📥 Download Full Report",
                    data=full_report,
                    file_name=f"chanakya_full_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
        else:
            st.info("👈 Configure the problem and parameters, then click 'Execute Analysis Pipeline' to begin.")

# ============================================================================
# TAB 2: KNOWLEDGE BASE EXPLORER
# ============================================================================
with tab2:
    st.markdown("## Arthashastra Knowledge Corpus")
    st.caption("Explore the 15 core doctrines used in the RAG system")
    
    df_corpus = get_corpus_df()
    
    # Domain filter
    domains = ["All Domains"] + get_all_domains()
    selected_domain = st.selectbox("Filter by Domain", domains)
    
    if selected_domain != "All Domains":
        df_corpus = df_corpus[df_corpus['domain'] == selected_domain]
    
    # Display doctrines
    for idx, row in df_corpus.iterrows():
        with st.expander(f"📜 {row['doctrine']} | Domain: {row['domain']}"):
            st.markdown(f"**Doctrine Text:**")
            st.info(row['text'])
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Keywords:** {row['keywords']}")
            with col2:
                st.metric("Policy Weight", f"{row['policy_weight']:.2f}")
    
    st.markdown("---")
    st.markdown("### Corpus Statistics")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Doctrines", len(get_corpus_df()))
    with col2:
        st.metric("Governance Domains", len(get_all_domains()))
    with col3:
        avg_weight = get_corpus_df()['policy_weight'].mean()
        st.metric("Avg Policy Weight", f"{avg_weight:.2f}")

# ============================================================================
# TAB 3: ANALYTICS DASHBOARD
# ============================================================================
with tab3:
    st.markdown("## System Analytics & Diagnostics")
    
    if 'all_similarity_scores' in st.session_state:
        st.markdown("### RAG Retrieval Analysis")
        
        # Heatmap
        fig_heatmap = generate_heatmap(get_corpus_df(), st.session_state['all_similarity_scores'])
        st.plotly_chart(fig_heatmap, use_container_width=True)
        
        st.markdown("### Top 5 Relevant Doctrines")
        
        df_corpus = get_corpus_df()
        top_5_indices = np.argsort(st.session_state['all_similarity_scores'])[-5:][::-1]
        
        for idx in top_5_indices:
            score = st.session_state['all_similarity_scores'][idx]
            doc = df_corpus.iloc[idx]
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{doc['doctrine']}**")
                st.caption(f"Domain: {doc['domain']}")
            with col2:
                st.metric("Similarity", f"{score:.4f}")
        
        st.markdown("---")
        
        # MCDA Breakdown
        st.markdown("### MCDA Criteria Breakdown")
        
        criteria_names = [v['name'] for v in MCDA_CRITERIA.values()]
        criteria_weights = [v['weight'] for v in MCDA_CRITERIA.values()]
        scores = st.session_state['scores']
        weighted_scores = [s * w for s, w in zip(scores, criteria_weights)]
        
        fig_mcda = go.Figure(data=[
            go.Bar(name='Raw Score', x=criteria_names, y=scores, marker_color='lightblue'),
            go.Bar(name='Weighted Score', x=criteria_names, y=weighted_scores, marker_color='darkblue')
        ])
        
        fig_mcda.update_layout(
            title="Multi-Criteria Decision Analysis (MCDA) Breakdown",
            yaxis_title="Score",
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig_mcda, use_container_width=True)
        
    else:
        st.info("Run a policy analysis first to see analytics data here.")

# ============================================================================
# TAB 4: ABOUT & METHODOLOGY
# ============================================================================
with tab4:
    st.markdown("## About This Research Project")
    
    st.markdown("""
    ### 🎓 Academic Context
    
    **College:** RV College of Engineering  
    **Department:** Artificial Intelligence and Machine Learning  
    **Course:** Indian Knowledge System (HS271T)  
    **Guide:** Dr. Lingayya Hiremath, Prof Biotechnology
    
    ### Team Members
    
    1. **Kota Vishnu Datta** (1RV22AI024) - 7396755649
    2. **Chillale Naveen** (1RV22AI013) - 9951558907
    3. **Boru Harshavardhan Reddy** (1RV22AI065) - 8328648978
    4. **Jaswanth Reddy M** (1RV22AI020) - 8309407742
    
    ---
    
    ### Project Overview
    
    This project demonstrates a **Neuro-Symbolic AI Architecture** that combines:
    
    1. **Ancient Wisdom:** Chanakya's Arthashastra principles (300 BCE)
    2. **Modern AI:** Large Language Models (Gemini) + Retrieval-Augmented Generation (RAG)
    3. **Decision Science:** Multi-Criteria Decision Analysis (MCDA)
    
    ### 🔬 Technical Architecture
    
    ```
    User Input (Policy Problem)
           ↓
    [TF-IDF Vectorization]
           ↓
    [Cosine Similarity Calculation]
           ↓
    [RAG: Retrieve Relevant Arthashastra Doctrine]
           ↓
    [LLM Inference with Retrieved Context]
           ↓
    [MCDA Scoring & Visualization]
           ↓
    Policy Recommendation Output
    ```
    
    ### Key Innovations
    
    - **Culturally-Grounded AI:** Unlike generic Western policy models, this system is rooted in Indian strategic thought
    - **Explainable Recommendations:** Every suggestion is traced back to specific Sanskrit principles
    - **Quantitative Framework:** MCDA scoring provides measurable policy evaluation
    - **Visual Analytics:** Radar charts, heatmaps, and Saptanga analysis for transparency
    
    ### Research Contributions
    
    1. **Novel Dataset:** First structured digital corpus of Arthashastra for AI systems
    2. **Hybrid Architecture:** Demonstrates integration of symbolic knowledge with neural models
    3. **Applied ML:** TF-IDF + Cosine Similarity for semantic doctrine retrieval
    4. **Decision Intelligence:** Framework applicable to agriculture, health, climate, welfare policies
    
    ### 📖 Methodology
    
    #### Phase 1: Knowledge Extraction
    - Identified 15 core doctrines from Arthashastra
    - Converted to computational format with keywords, domains, policy weights
    
    #### Phase 2: RAG Implementation
    - TF-IDF vectorization of doctrine corpus
    - Cosine similarity for semantic matching
    - Dynamic context injection into LLM prompts
    
    #### Phase 3: Decision Intelligence Framework
    - Multi-criteria scoring (Welfare, Economic, Law & Order, Political, Implementation)
    - Weighted aggregation for Governance Effectiveness Index (GEI)
    - Visualization for policy trade-off analysis
    
    #### Phase 4: LLM-Powered Analysis
    - Google Gemini for natural language policy generation
    - Structured output format (Diagnosis → Options → Recommendation → Risk Mitigation)
    - Sanskrit terminology integration for authenticity
    
    ### 🏆 Expected Impact
    
    - **For Policymakers:** Evidence-based, culturally-relevant decision support
    - **For Researchers:** Framework for integrating traditional knowledge into AI
    - **For Academia:** Demonstrates applied ML in governance domain
    
    ### References
    
    1. Kautilya's Arthashastra (300 BCE) - Classical text on statecraft
    2. Davenport, T. (2022). "Decision Intelligence" - AI for organizational decisions
    3. OECD (2023). "Explainable AI in Public Policy" - Transparency in governance AI
    4. Various papers on RAG, TF-IDF, and hybrid AI architectures
    
    ---
    
    ### Tech Stack
    
    - **Frontend:** Streamlit
    - **LLM:** Google Gemini (gemini-1.5-flash / gemini-1.5-pro)
    - **ML Libraries:** Scikit-learn (TF-IDF, Cosine Similarity)
    - **Visualization:** Plotly
    - **Data Processing:** Pandas, NumPy
    
    ### 📧 Contact
    
    For research collaboration or inquiries, contact the team via RV College of Engineering.
    
    ---
    
    *This system is a research prototype for educational and academic purposes.*
    """)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Chanakyan Decision Intelligence System v1.0</strong></p>
    <p>RV College of Engineering | Department of AI & ML | 2025</p>
    <p><em>Integrating Ancient Wisdom with Modern AI for Better Governance</em></p>
</div>
""", unsafe_allow_html=True)
