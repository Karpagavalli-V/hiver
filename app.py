import os
import sys
import streamlit as st
from dotenv import load_dotenv

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.pipeline import SupportPipeline

# Load environment variables
load_dotenv(override=True)

# Page Configuration
st.set_page_config(
    page_title="AmazonHelp AI Support Copilot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Mode Custom Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #0D1117 !important;
        color: #E6EDF3 !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1200px;
        background-color: #0D1117 !important;
    }

    /* Sidebar Dark Amazon Theme */
    [data-testid="stSidebar"] {
        background-color: #131921 !important;
        border-right: 1px solid #232F3E !important;
    }
    [data-testid="stSidebar"] * { color: #D5D9D9 !important; }
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #FF9900 !important;
        font-weight: 700 !important;
    }
    [data-testid="stSidebar"] hr { border-color: #2C3E50 !important; }
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stCheckbox label {
        color: #AAB7C4 !important;
        font-size: 0.83rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Header */
    .header-wrap {
        background: linear-gradient(135deg, #161B22 0%, #0D1117 100%);
        border: 1px solid #21262D;
        border-radius: 12px;
        padding: 1.4rem 1.75rem;
        margin-bottom: 1.2rem;
        position: relative;
        overflow: hidden;
    }
    .header-wrap::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #FF9900, #FF6B35, #FF9900);
        background-size: 200% 100%;
        animation: shimmer 3s linear infinite;
    }
    @keyframes shimmer {
        0%   { background-position: -200% 0; }
        100% { background-position:  200% 0; }
    }
    .header-title {
        font-size: 1.9rem; font-weight: 800;
        color: #E6EDF3; letter-spacing: -0.02em; margin-bottom: 0.2rem;
    }
    .header-title span { color: #FF9900; }
    .header-subtitle {
        font-size: 0.88rem; color: #8B949E;
        font-weight: 500; margin-bottom: 0.75rem;
    }

    /* Pulsing Status Dots */
    .status-indicator {
        display: inline-flex; align-items: center; gap: 8px;
        background-color: rgba(63, 185, 80, 0.1);
        color: #3FB950;
        border: 1px solid rgba(63, 185, 80, 0.3);
        padding: 5px 14px; border-radius: 9999px;
        font-size: 0.8rem; font-weight: 600;
    }
    .status-dot {
        width: 8px; height: 8px;
        background-color: #3FB950; border-radius: 50%;
        animation: pulse-green 2s infinite;
    }
    .status-dot-processing {
        width: 8px; height: 8px;
        background-color: #FF9900; border-radius: 50%;
        animation: pulse-orange 1s infinite;
    }
    @keyframes pulse-green {
        0%   { box-shadow: 0 0 0 0   rgba(63,185,80,0.6); }
        70%  { box-shadow: 0 0 0 8px rgba(63,185,80,0);   }
        100% { box-shadow: 0 0 0 0   rgba(63,185,80,0);   }
    }
    @keyframes pulse-orange {
        0%   { box-shadow: 0 0 0 0   rgba(255,153,0,0.7); }
        70%  { box-shadow: 0 0 0 8px rgba(255,153,0,0);   }
        100% { box-shadow: 0 0 0 0   rgba(255,153,0,0);   }
    }

    /* Pipeline Flow */
    .pipeline-flow {
        display: flex; align-items: center; justify-content: center;
        gap: 0.4rem; flex-wrap: wrap;
        background: #161B22; border: 1px solid #21262D;
        border-radius: 8px; padding: 0.6rem 1rem;
        margin-bottom: 1.2rem;
        font-size: 0.78rem; color: #8B949E; font-weight: 600;
    }
    .pipeline-step {
        background: #21262D; border: 1px solid #30363D;
        border-radius: 5px; padding: 3px 10px; color: #C9D1D9; white-space: nowrap;
    }
    .pipeline-arrow { color: #484F58; font-size: 0.85rem; }

    /* Cards */
    .card-label {
        font-size: 0.7rem; font-weight: 700;
        text-transform: uppercase; letter-spacing: 0.08em;
        color: #8B949E; margin-bottom: 0.5rem;
    }

    /* Confidence Ring Wrapper */
    .conf-ring-wrap {
        display: flex; flex-direction: column;
        align-items: center; gap: 6px;
    }
    .conf-ring-label {
        font-size: 0.72rem; font-weight: 600;
        color: #8B949E; text-transform: uppercase; letter-spacing: 0.06em;
    }

    /* Risk Gauge */
    .risk-gauge-wrap { margin-top: 0.4rem; }
    .risk-bar-bg {
        background: #21262D; border-radius: 9999px;
        height: 10px; width: 100%; overflow: hidden; margin: 6px 0 4px;
    }
    .risk-bar-fill-low    { height:100%; border-radius:9999px; background:linear-gradient(90deg,#3FB950,#2EA043); }
    .risk-bar-fill-medium { height:100%; border-radius:9999px; background:linear-gradient(90deg,#FF9900,#D68910); }
    .risk-bar-fill-high   { height:100%; border-radius:9999px; background:linear-gradient(90deg,#F85149,#C0392B); }
    .risk-label-row {
        display: flex; justify-content: space-between;
        font-size: 0.7rem; color: #8B949E; font-weight: 600;
    }

    /* Decision Badges */
    .badge-auto-handle {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(63,185,80,0.12); color: #3FB950;
        border: 1px solid rgba(63,185,80,0.35);
        padding: 6px 16px; border-radius: 7px;
        font-weight: 700; font-size: 1rem;
    }
    .badge-escalate {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(248,81,73,0.12); color: #F85149;
        border: 1px solid rgba(248,81,73,0.35);
        padding: 6px 16px; border-radius: 7px;
        font-weight: 700; font-size: 1rem;
    }

    /* Intent Chip */
    .intent-chip {
        display: inline-block;
        background: rgba(255,153,0,0.15); color: #FF9900;
        border: 1px solid rgba(255,153,0,0.4);
        padding: 4px 14px; border-radius: 6px;
        font-size: 1rem; font-weight: 700; margin-top: 4px;
    }

    /* Flag Pills */
    .flag-pill {
        background: rgba(248,81,73,0.1); color: #F85149;
        border: 1px solid rgba(248,81,73,0.3);
        padding: 3px 10px; border-radius: 5px;
        font-size: 0.78rem; font-weight: 600;
        margin-right: 5px; margin-top: 4px; display: inline-block;
    }

    /* Reply Box */
    .reply-container {
        background: #161B22; border-left: 4px solid #FF9900;
        padding: 1.1rem 1.3rem; border-radius: 0 8px 8px 0;
        font-size: 1rem; color: #C9D1D9; line-height: 1.7;
        margin-bottom: 0.5rem;
        border-top: 1px solid #21262D;
        border-right: 1px solid #21262D;
        border-bottom: 1px solid #21262D;
    }
    .grounding-tag {
        font-size: 0.78rem; color: #79C0FF; font-weight: 600;
        display: inline-flex; align-items: center; gap: 5px;
    }

    /* Evidence Cards */
    .evidence-card {
        background: #161B22; border: 1px solid #21262D;
        padding: 0.85rem 1rem; border-radius: 8px; margin-bottom: 0.6rem;
    }
    .evidence-meta { font-size:0.78rem; color:#8B949E; font-weight:600; margin-bottom:0.35rem; }
    .evidence-cust { font-size:0.9rem; color:#C9D1D9; margin-bottom:0.25rem; }
    .evidence-resp { font-size:0.9rem; color:#8B949E; }

    /* Expander overrides */
    [data-testid="stExpander"] {
        background: #161B22 !important;
        border: 1px solid #21262D !important;
        border-radius: 8px !important;
    }
    [data-testid="stExpander"] summary { color: #C9D1D9 !important; font-weight: 600 !important; }

    /* Text area */
    textarea, .stTextArea textarea {
        background: #161B22 !important; color: #C9D1D9 !important;
        border: 1px solid #30363D !important; border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
    }
    textarea:focus, .stTextArea textarea:focus {
        border-color: #FF9900 !important;
        box-shadow: 0 0 0 3px rgba(255,153,0,0.15) !important;
    }

    /* Primary button */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #FF9900, #FF6B35) !important;
        color: #0D1117 !important; font-weight: 700 !important;
        border: none !important; border-radius: 8px !important;
        font-size: 0.95rem !important; padding: 0.6rem 1.2rem !important;
        transition: transform 0.15s ease, box-shadow 0.15s ease !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(255,153,0,0.35) !important;
    }

    hr { border-color: #21262D !important; }
</style>
""", unsafe_allow_html=True)


# Sidebar — Amazon Dark Theme
st.sidebar.markdown("""
<div style="padding:1rem 0.5rem 0.6rem 0.5rem; text-align:center;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 90" width="160" height="48">
        <text x="4" y="62" font-family="Arial Black,sans-serif" font-size="64"
              font-weight="900" fill="#FFFFFF" letter-spacing="-2">amazon</text>
        <path d="M100 75 Q152 98 204 75" stroke="#FF9900" stroke-width="6"
              fill="none" stroke-linecap="round"/>
        <polygon points="200,68 208,78 196,80" fill="#FF9900"/>
    </svg>
    <div style="font-size:0.7rem; color:#8B949E; letter-spacing:0.12em;
                font-weight:600; margin-top:4px; text-transform:uppercase;">
        AI Support Copilot
    </div>
</div>
<hr style="border-color:#2C3E50; margin:0.5rem 0 1rem 0;">
""", unsafe_allow_html=True)

st.sidebar.markdown("### ⚡ Configuration")

PRESETS = {
    "Select a sample message...": "",
    "📦 Delivery Inquiry": "@AmazonHelp The last two packages were supposed to be delivered by AMZL US today but haven't arrived.",
    "💸 Delayed Refund": "@AmazonHelp Please don't play around. I have been promised by Amazon many times for refund but fact is it is not honoring.",
    "🚨 Security Concern": "@AmazonHelp My account was hacked and an unauthorized order of $500 was placed on my credit card!",
    "📷 Damaged Package": "Wow! @AmazonHelp this packaging job is atrocious. I don't order books for them to arrive damaged https://t.co/sJNSq2qqM8"
}

selected_preset = st.sidebar.selectbox("⚡ Quick Presets", list(PRESETS.keys()))

st.sidebar.markdown("---")
mock_mode = st.sidebar.checkbox("🔌 Offline Mock Mode", value=False, help="Run pipeline offline without live API calls")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏗 System Architecture")
st.sidebar.markdown("""
- **Model**: `gpt-4o-mini` via OpenRouter
- **Retriever**: TF-IDF + Cosine Similarity
- **Escalation**: Multi-Layer Risk Engine
- **Security**: Server-side `.env` key storage
""")

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="font-size:0.72rem; color:#484F58; text-align:center; padding-top:0.5rem;">
    Hiver SDE Intern Assignment<br>
    <span style="color:#FF9900; font-weight:600;">AmazonHelp TWCS Dataset</span>
</div>
""", unsafe_allow_html=True)


# Helper: Confidence Ring SVG
def confidence_ring(pct: float, size: int = 90) -> str:
    import math
    radius = (size - 14) // 2
    circumference = 2 * math.pi * radius
    filled = circumference * pct
    gap = circumference - filled
    if pct == 0:
        color, label = "#484F58", "N/A"
    elif pct >= 0.7:
        color, label = "#3FB950", f"{pct*100:.0f}%"
    elif pct >= 0.4:
        color, label = "#FF9900", f"{pct*100:.0f}%"
    else:
        color, label = "#F85149", f"{pct*100:.0f}%"
    font_size = 14 if pct > 0 else 10
    cx = size // 2
    return f"""
<div class="conf-ring-wrap">
  <svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">
    <circle cx="{cx}" cy="{cx}" r="{radius}" fill="none" stroke="#21262D" stroke-width="7"/>
    <circle cx="{cx}" cy="{cx}" r="{radius}" fill="none" stroke="{color}" stroke-width="7"
            stroke-linecap="round"
            stroke-dasharray="{filled:.2f} {gap:.2f}"
            transform="rotate(-90 {cx} {cx})"/>
    <text x="{cx}" y="{cx + font_size//3}" text-anchor="middle"
          font-family="Inter,sans-serif" font-size="{font_size}"
          font-weight="700" fill="{color}">{label}</text>
  </svg>
  <div class="conf-ring-label">Confidence</div>
</div>"""


# Helper: Risk Gauge
def risk_gauge(decision: str, flags: list) -> str:
    n_flags = len(flags) if flags else 0
    if decision == "AUTO-HANDLE":
        label, width, css_class, color = "LOW RISK",    "22%", "risk-bar-fill-low",    "#3FB950"
    elif n_flags >= 3:
        label, width, css_class, color = "HIGH RISK",   "90%", "risk-bar-fill-high",   "#F85149"
    else:
        label, width, css_class, color = "MEDIUM RISK", "55%", "risk-bar-fill-medium", "#FF9900"
    return f"""
<div class="risk-gauge-wrap">
  <div class="card-label">RISK LEVEL</div>
  <div style="font-size:1.1rem;font-weight:800;color:{color};letter-spacing:0.03em;">{label}</div>
  <div class="risk-bar-bg"><div class="{css_class}" style="width:{width};"></div></div>
  <div class="risk-label-row"><span>LOW</span><span>MEDIUM</span><span>HIGH</span></div>
</div>"""


# Header
st.markdown("""
<div class="header-wrap">
  <div class="header-title">Amazon<span>Help</span> AI Support Copilot</div>
  <div class="header-subtitle">
    Intent Classification &nbsp;&bull;&nbsp; Historical Retrieval &nbsp;&bull;&nbsp;
    Grounded Reply &nbsp;&bull;&nbsp; Escalation Engine
  </div>
  <div class="status-indicator">
    <span class="status-dot"></span>
    <span>AI Pipeline Ready</span>
  </div>
</div>
""", unsafe_allow_html=True)

# Pipeline Flow Bar
st.markdown("""
<div class="pipeline-flow">
  <div class="pipeline-step">📥 Customer Message</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-step">🏷️ Intent Classification</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-step">📚 Historical Retrieval</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-step">🤖 Grounded Reply</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-step">🛡️ Escalation Engine</div>
  <div class="pipeline-arrow">→</div>
  <div class="pipeline-step">📋 Operator Decision</div>
</div>
""", unsafe_allow_html=True)

# Customer Message Input
st.markdown("### 💬 Customer Message")
st.caption("Enter a customer tweet or message to analyze and generate a grounded support response.")

default_msg = PRESETS[selected_preset] if selected_preset != "Select a sample message..." else ""

with st.container():
    customer_message = st.text_area(
        "Message Input",
        value=default_msg,
        height=95,
        placeholder="e.g. @AmazonHelp Where is my refund for order #123-456?",
        label_visibility="collapsed"
    )
    with st.expander("➕ Additional Conversation Context (Optional)", expanded=False):
        context_input = st.text_area(
            "Prior Conversation Context",
            height=70,
            placeholder="Paste prior back-and-forth messages if available...",
            label_visibility="collapsed"
        )
    submit_btn = st.button("🚀  Analyze & Generate Support Response", type="primary", use_container_width=True)


# Processing & Output Display
if submit_btn:
    if not customer_message.strip():
        st.warning("⚠️ Enter a customer message to begin.")
    else:
        processing_placeholder = st.empty()
        processing_placeholder.markdown("""
<div class="status-indicator" style="background:rgba(255,153,0,0.1);
     color:#FF9900; border-color:rgba(255,153,0,0.35); margin-bottom:0.8rem;">
  <span class="status-dot-processing"></span>
  <span>Pipeline Processing — Intent → Retrieval → Reply → Escalation...</span>
</div>
""", unsafe_allow_html=True)

        with st.spinner(""):
            try:
                pipeline = SupportPipeline(mock_mode=mock_mode)
                result = pipeline.process(
                    customer_message=customer_message.strip(),
                    context=context_input.strip() if context_input else None
                )

                processing_placeholder.empty()

                st.markdown("---")
                st.markdown("### 📊 Analysis & Pipeline Output")

                col1, col2, col3, col4 = st.columns([1.6, 1.1, 1.5, 1.6])

                with col1:
                    st.markdown('<div class="card-label">PREDICTED INTENT</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="intent-chip">{result["intent"]}</div>', unsafe_allow_html=True)

                with col2:
                    conf_val = result.get("confidence", 0.0) or 0.0
                    st.markdown(confidence_ring(conf_val, size=88), unsafe_allow_html=True)

                with col3:
                    st.markdown('<div class="card-label">SUPPORT DECISION</div>', unsafe_allow_html=True)
                    decision = result["decision"]
                    if decision == "AUTO-HANDLE":
                        st.markdown('<div class="badge-auto-handle">✅ AUTO-HANDLE</div>', unsafe_allow_html=True)
                    else:
                        st.markdown('<div class="badge-escalate">🚨 ESCALATE TO HUMAN</div>', unsafe_allow_html=True)
                    st.markdown(
                        f'<div style="font-size:0.82rem;color:#8B949E;margin-top:8px;">{result["escalation_reason"]}</div>',
                        unsafe_allow_html=True
                    )

                with col4:
                    risk_flags = result.get("risk_flags", [])
                    st.markdown(risk_gauge(decision, risk_flags), unsafe_allow_html=True)
                    if risk_flags:
                        st.markdown('<div class="card-label" style="margin-top:8px;">FLAGS</div>', unsafe_allow_html=True)
                        flag_html = "".join([f'<span class="flag-pill">{f}</span>' for f in risk_flags])
                        st.markdown(flag_html, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                with st.expander("🔍 Intent Classification Rationale", expanded=False):
                    st.write(f"**Reasoning**: {result['intent_reason']}")

                st.markdown("### 🤖 AI-Generated Reply")
                st.markdown(f'<div class="reply-container">{result["generated_reply"]}</div>', unsafe_allow_html=True)

                retrieved_list = result.get("retrieved_evidence", [])
                if retrieved_list:
                    st.markdown('<div class="grounding-tag">🔗 Grounded using historical support evidence</div>', unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                with st.expander(f"📚 Historical Support Evidence ({len(retrieved_list)} items)", expanded=True):
                    if not retrieved_list:
                        st.info("No historical evidence available for this query.")
                    else:
                        for idx, item in enumerate(retrieved_list, 1):
                            intent_lbl   = item.get("intent", "N/A")
                            similarity   = item.get("similarity_score", 0.0)
                            cust_msg     = item.get("customer_message") or item.get("text") or "N/A"
                            brand_resp   = item.get("historical_response") or item.get("response_text")
                            ts           = f" | {item.get('timestamp')}" if item.get("timestamp") else ""
                            resp_html = (
                                f'<div class="evidence-resp"><strong style="color:#C9D1D9;">AmazonHelp:</strong> "{brand_resp}"</div>'
                                if brand_resp else
                                '<div style="color:#484F58;font-size:0.85rem;"><em>No historical response available</em></div>'
                            )
                            st.markdown(f"""
<div class="evidence-card">
  <div class="evidence-meta">#{idx} &nbsp;|&nbsp; Intent: {intent_lbl} &nbsp;|&nbsp; Similarity: {similarity:.2f}{ts}</div>
  <div class="evidence-cust"><strong style="color:#8B949E;">Customer:</strong> "{cust_msg}"</div>
  {resp_html}
</div>""", unsafe_allow_html=True)

            except Exception as e:
                processing_placeholder.empty()
                st.error("🔴 Pipeline Execution Error")
                st.write(f"Error: `{str(e)}`")
                st.info("💡 Check your `.env` configuration or enable **Offline Mock Mode** in the sidebar.")


# Footer Accordions
st.markdown("---")
col_exp1, col_exp2 = st.columns([1, 1])

with col_exp1:
    with st.expander("ℹ️ How It Works", expanded=False):
        st.markdown("""
1. **Intent Classification**: Incoming message → 1 of 9 AmazonHelp intents via `gpt-4o-mini`.
2. **Historical Retrieval**: Top-K similar resolved interactions from 66,027 TWCS training threads.
3. **Grounded Reply Generation**: AI formulates a brand-aligned reply grounded in retrieved evidence.
4. **Escalation Rules Engine**: Evaluates safety risks, financial disputes, account security, and retrieval confidence.
5. **Operator Copilot View**: Displays intent, evidence, reply, and escalation status for agent decisioning.
        """)

with col_exp2:
    with st.expander("📊 Evaluation Snapshot", expanded=False):
        st.markdown("""
**Final Benchmark Results (200 Golden Set Examples)**:
- **Intent Accuracy**: **56.50%** *(vs 34.50% TF-IDF, 39.50% Majority)*
- **Intent Macro F1**: **60.61%** *(vs 35.93% TF-IDF, 6.29% Majority)*
- **LLM Judge Reply Quality**: **4.20 / 5.00**
- **Reply Pass Rate**: **96.5%** *(193/200)*

**Inter-Rater Reliability (N=20 Human Ratings)**:
- **Macro QWK**: **0.3038** | **Cohen\'s Kappa**: **0.1949**
- Safety QWK: **1.0000** | Helpfulness QWK: **0.3443**
        """)
