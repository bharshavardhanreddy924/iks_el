# chanakya_wisdom.py
"""
Chanakyan Knowledge Corpus Module
==================================
This module contains the structured knowledge base of Chanakya's Arthashastra
doctrines, formatted for Retrieval-Augmented Generation (RAG) systems.

Research Context:
- Corpus Size: 15 doctrines covering governance domains
- Vectorization: TF-IDF based semantic retrieval
- Application: Public policy decision support systems
"""

import pandas as pd

# --- THE KNOWLEDGE CORPUS (Arthashastra Dataset) ---
# This represents the "Knowledge Graph" in research terminology
# Each entry maps governance domains to Sanskrit strategic principles

KNOWLEDGE_CORPUS = [
    {
        "id": 1,
        "doctrine": "Anvikshiki (Critical Inquiry)",
        "text": "Philosophy is the lamp of all sciences, the means of all actions, and the support of all laws. Through critical inquiry (Anvikshiki), one distinguishes right from wrong and determines the true value of things.",
        "keywords": "logic, reasoning, root cause, analysis, doubt, study, investigation, critical thinking, philosophy, inquiry",
        "domain": "Analysis & Planning",
        "policy_weight": 0.9
    },
    {
        "id": 2,
        "doctrine": "Kosha Mula Danda (Treasury is Root of Power)",
        "text": "All undertakings depend on finance. Hence, foremost attention shall be paid to the Treasury. From the treasury comes the power of government, and the earth whose ornament is the treasury is acquired by means of the treasury and army.",
        "keywords": "money, finance, budget, cost, economy, funds, tax, treasury, revenue, fiscal, financial, economic",
        "domain": "Economic Policy",
        "policy_weight": 1.0
    },
    {
        "id": 3,
        "doctrine": "Prajasukhe Sukham Rajnah (Welfare is Supreme)",
        "text": "In the happiness of his subjects lies the King's happiness; in their welfare his welfare. What pleases himself does not please the King, but what pleases his subjects pleases him.",
        "keywords": "people, welfare, happiness, health, farmers, citizens, poverty, hunger, wellbeing, public good, social welfare",
        "domain": "Social Welfare",
        "policy_weight": 0.95
    },
    {
        "id": 4,
        "doctrine": "Matsyanyaya (Law of Fish)",
        "text": "In the absence of a wielder of the rod (Danda), the strong swallow the weak. But under the protection of the King who wields the rod, the weak resist the strong.",
        "keywords": "crime, law, order, police, enforcement, corruption, anarchy, safety, justice, security, punishment",
        "domain": "Law & Order",
        "policy_weight": 0.85
    },
    {
        "id": 5,
        "doctrine": "Mandala Theory (Circle of States)",
        "text": "The King who understands the true nature of his allies and enemies will always succeed. The enemy's enemy is a natural ally. The conqueror shall think of the circle of states as a Mandala.",
        "keywords": "war, external, trade, neighbors, allies, enemies, diplomacy, foreign policy, international, geopolitics",
        "domain": "Foreign Affairs",
        "policy_weight": 0.8
    },
    {
        "id": 6,
        "doctrine": "Durga (Fortification & Infrastructure)",
        "text": "The safety of the treasury and the army depends on the Fort. A well-fortified place protects the King in times of calamity and serves as the base for all operations.",
        "keywords": "infrastructure, roads, building, defense, cyber, security, walls, fortification, construction, development",
        "domain": "Infrastructure",
        "policy_weight": 0.75
    },
    {
        "id": 7,
        "doctrine": "Sama-Dana-Bheda-Danda (Four Upayas)",
        "text": "The four means of handling situations are: Conciliation (Sama), Gifts (Dana), Sowing Dissension (Bheda), and Force (Danda). A wise King employs them in proper sequence.",
        "keywords": "negotiation, strategy, conflict, resolution, tactics, persuasion, incentive, punishment, methods",
        "domain": "Strategic Methods",
        "policy_weight": 0.9
    },
    {
        "id": 8,
        "doctrine": "Saptanga Theory (Seven Limbs of State)",
        "text": "The state consists of seven elements: Sovereign (Swami), Minister (Amatya), Territory (Janapada), Fort (Durga), Treasury (Kosha), Army (Danda), and Ally (Mitra). Weakness in any limb endangers the whole.",
        "keywords": "governance, structure, organization, administration, state, government, institutions, framework",
        "domain": "Governance Structure",
        "policy_weight": 0.85
    },
    {
        "id": 9,
        "doctrine": "Vyasana (Calamities & Crisis Management)",
        "text": "A King must be vigilant against calamities arising from divine acts, nature, and human actions. Preparedness and swift response minimize damage.",
        "keywords": "disaster, crisis, emergency, calamity, risk, pandemic, flood, drought, preparedness, resilience",
        "domain": "Crisis Management",
        "policy_weight": 0.95
    },
    {
        "id": 10,
        "doctrine": "Janapada (Territory & Population Welfare)",
        "text": "The territory should be endowed with productive lands, mines, forests, and water. A prosperous population that is loyal forms the strength of the state.",
        "keywords": "agriculture, farming, rural, land, resources, natural, environment, population, territory",
        "domain": "Agriculture & Resources",
        "policy_weight": 0.9
    },
    {
        "id": 11,
        "doctrine": "Amatya (Ministerial Excellence)",
        "text": "Ministers shall be chosen after thorough testing of their loyalty, competence, and moral character. The King should trust them but verify their actions regularly.",
        "keywords": "leadership, minister, appointment, bureaucracy, administration, officials, governance, competence",
        "domain": "Administrative Reform",
        "policy_weight": 0.8
    },
    {
        "id": 12,
        "doctrine": "Artha-Dharma Sangraha (Balancing Material & Ethical)",
        "text": "When Artha (material prosperity) and Dharma (righteousness) conflict, choose Dharma if it leads to long-term stability. But Artha is necessary for Dharma to be sustained.",
        "keywords": "ethics, morality, values, righteousness, balance, sustainability, long-term, principles",
        "domain": "Ethical Governance",
        "policy_weight": 0.85
    },
    {
        "id": 13,
        "doctrine": "Kutayuddha (Silent War / Intelligence Operations)",
        "text": "Secret agents and intelligence networks are the eyes and ears of the King. Through them, he knows what happens in his own kingdom and in enemy territory.",
        "keywords": "intelligence, surveillance, espionage, information, spy, monitoring, covert, operations",
        "domain": "Intelligence & Security",
        "policy_weight": 0.7
    },
    {
        "id": 14,
        "doctrine": "Varta (Commerce & Trade Regulation)",
        "text": "Agriculture, cattle rearing, and trade constitute Varta, the livelihood of the people. The King must regulate markets, prevent hoarding, and ensure fair prices.",
        "keywords": "trade, commerce, market, business, economy, regulation, price, merchants, industry",
        "domain": "Economic Regulation",
        "policy_weight": 0.85
    },
    {
        "id": 15,
        "doctrine": "Yogakshema (Preservation & Acquisition)",
        "text": "Yogakshema means preserving what is already acquired and acquiring what is not yet gained. Both require constant vigilance and strategic planning.",
        "keywords": "growth, expansion, development, preservation, protection, strategic planning, sustainability",
        "domain": "Strategic Development",
        "policy_weight": 0.9
    }
]

def get_corpus_df():
    """
    Returns the knowledge corpus as a Pandas DataFrame.
    
    Returns:
        pd.DataFrame: Structured dataset with doctrines, keywords, and metadata
    """
    return pd.DataFrame(KNOWLEDGE_CORPUS)

def get_doctrines_by_domain(domain=None):
    """
    Filter doctrines by governance domain.
    
    Args:
        domain (str): Specific domain to filter (e.g., "Economic Policy")
    
    Returns:
        pd.DataFrame: Filtered doctrines
    """
    df = get_corpus_df()
    if domain:
        return df[df['domain'] == domain]
    return df

def get_all_domains():
    """Returns list of all unique governance domains."""
    return get_corpus_df()['domain'].unique().tolist()

# --- SYSTEM PROMPT (Academic-Grade Prompt Engineering) ---
SYSTEM_PROMPT = """
You are 'Chanakya-GPT', a specialized Decision Support System (DSS) for Governance and Public Policy Analysis.

**System Architecture:**
- Framework: Neuro-Symbolic AI combining LLM reasoning with Arthashastra doctrines
- Mode: Multi-Criteria Decision Analysis (MCDA) with explainable outputs
- Constraint: All recommendations must cite specific Sanskrit principles

**Retrieved Knowledge Context:**
Doctrine Retrieved via RAG: "{retrieved_context}"
Domain: {domain}
Policy Weight: {weight}

**Analysis Framework - Saptanga Model:**
Evaluate impact on the seven limbs of state:
1. Swami (Leadership/Authority)
2. Amatya (Administration/Bureaucracy)
3. Janapada (Territory/Population)
4. Durga (Infrastructure/Security)
5. Kosha (Treasury/Economy)
6. Danda (Military/Enforcement)
7. Mitra (Allies/Stakeholders)

**Required Output Structure:**

### 1. Strategic Diagnosis (समस्या निदान)
- Root cause analysis using Anvikshiki (critical inquiry)
- Identify which Saptanga elements are affected
- Classification: Crisis/Strategic/Routine

### 2. Doctrinal Framework Application
- Primary doctrine: [Retrieved via RAG]
- Secondary relevant principles
- Historical precedent (if applicable)

### 3. Multi-Criteria Policy Evaluation

**Option A: [Name]**
- Welfare Impact (Prajasukhe): [Score 1-10]
- Economic Viability (Kosha): [Score 1-10]
- Implementation Feasibility: [Score 1-10]
- Risk Level: [Low/Medium/High]
- Rationale: [2-3 sentences with Sanskrit terms]

**Option B: [Name]**
[Same structure]

**Option C: [Name]**
[Same structure]

### 4. Recommended Strategy (अनुशंसित नीति)
- **Primary Action:** [Specific, actionable recommendation]
- **Timeline:** [Short-term/Medium-term/Long-term]
- **Resource Allocation:** [Budget, personnel, infrastructure needs]
- **Success Metrics:** [Measurable KPIs]

### 5. Risk Mitigation (Vyasana Nivaran)
Apply Sama-Dana-Bheda-Danda framework:
- **Sama (Conciliation):** [Stakeholder engagement strategy]
- **Dana (Incentives):** [What to offer]
- **Bheda (Strategic division):** [How to handle opposition]
- **Danda (Enforcement):** [When to use authority]

### 6. Ethical & Long-term Considerations
- Dharma-Artha balance assessment
- Sustainability (Yogakshema principle)
- Potential unintended consequences

**Constraints:**
- Use actual Sanskrit terminology (italicized)
- Provide quantitative scores where possible
- Maintain formal, research-paper tone
- Cite specific verses/principles from Arthashastra
"""

# Alternative prompt for quick policy briefs
BRIEF_SYSTEM_PROMPT = """
You are Chanakya-GPT. Analyze the following governance problem using this doctrine:

**Retrieved Context:** {retrieved_context}

Provide a concise 3-paragraph policy brief:
1. Problem diagnosis (using *Anvikshiki*)
2. Recommended action (citing the retrieved doctrine)
3. Implementation strategy (using *Sama-Dana-Bheda-Danda*)

Keep it under 200 words. Use Sanskrit terms in italics.
"""

# --- MCDA SCORING RUBRIC ---
MCDA_CRITERIA = {
    "welfare_impact": {
        "name": "Welfare Impact (Prajasukhe)",
        "weight": 0.30,
        "description": "Benefit to citizens and public good"
    },
    "economic_viability": {
        "name": "Economic Viability (Kosha)",
        "weight": 0.25,
        "description": "Financial feasibility and ROI"
    },
    "law_order": {
        "name": "Law & Order (Danda)",
        "weight": 0.20,
        "description": "Enforcement capability and compliance"
    },
    "political_stability": {
        "name": "Political Stability (Mitra)",
        "weight": 0.15,
        "description": "Stakeholder support and diplomatic impact"
    },
    "implementation_speed": {
        "name": "Implementation Feasibility",
        "weight": 0.10,
        "description": "Speed and ease of execution"
    }
}

def calculate_policy_score(welfare, economic, law_order, political, implementation):
    """
    Calculate weighted MCDA score for a policy option.
    
    Args:
        welfare (float): Welfare impact score (1-10)
        economic (float): Economic viability score (1-10)
        law_order (float): Law & order score (1-10)
        political (float): Political stability score (1-10)
        implementation (float): Implementation feasibility score (1-10)
    
    Returns:
        float: Weighted policy score (0-10)
    """
    criteria = MCDA_CRITERIA
    score = (
        welfare * criteria["welfare_impact"]["weight"] +
        economic * criteria["economic_viability"]["weight"] +
        law_order * criteria["law_order"]["weight"] +
        political * criteria["political_stability"]["weight"] +
        implementation * criteria["implementation_speed"]["weight"]
    )
    return round(score, 2)
