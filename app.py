import os
import sys
import streamlit as st
from dotenv import load_dotenv

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.pipeline import SupportPipeline

# Load environment variables
load_dotenv(override=True)

# ── Page Configuration ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AmazonHelp AI Support Copilot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom Styling ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    .status-card {
        padding: 1.25rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border: 1px solid #E2E8F0;
    }
    .auto-handle-badge {
        background-color: #DCFCE7;
        color: #15803D;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 1.1rem;
        display: inline-block;
        border: 1px solid #86EFAC;
    }
    .escalate-badge {
        background-color: #FEF2F2;
        color: #B91C1C;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 1.1rem;
        display: inline-block;
        border: 1px solid #FCA5A5;
    }
    .flag-tag {
        background-color: #F1F5F9;
        color: #334155;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 6px;
        border: 1px solid #CBD5E1;
        display: inline-block;
    }
    .reply-box {
        background-color: #F8FAFC;
        border-left: 4px solid #2563EB;
        padding: 1.25rem;
        border-radius: 0 8px 8px 0;
        font-size: 1.05rem;
        color: #1E293B;
        line-height: 1.6;
    }
    .evidence-item {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        padding: 0.8rem 1rem;
        border-radius: 6px;
        margin-bottom: 0.6rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar Configuration ──────────────────────────────────────────────────────
st.sidebar.image("https://img.icons8.com/color/96/amazon.png", width=64)
st.sidebar.title("Configuration")

# Preset examples
PRESETS = {
    "Select a sample message...": "",
    "📦 Delivery Inquiry": "@AmazonHelp The last two packages were supposed to be delivered by AMZL US today but haven't arrived.",
    "💸 Delayed Refund": "@AmazonHelp Please don't play around. I have been promised by Amazon many times for refund but fact is it is not honoring.",
    "🚨 Security Concern": "@AmazonHelp My account was hacked and an unauthorized order of $500 was placed on my credit card!",
    "📷 Damaged Package": "Wow! @AmazonHelp this packaging job is atrocious. I don't order books for them to arrive damaged https://t.co/sJNSq2qqM8"
}

selected_preset = st.sidebar.selectbox("⚡ Quick Presets", list(PRESETS.keys()))

st.sidebar.markdown("---")
mock_mode = st.sidebar.checkbox("🔌 Offline Mock Mode", value=False, help="Run without calling live LLM API")

st.sidebar.markdown("---")
st.sidebar.markdown("### System Architecture")
st.sidebar.markdown("- **Model**: `openai/gpt-4o-mini`")
st.sidebar.markdown("- **Retriever**: Hybrid Vector + BM25")
st.sidebar.markdown("- **Escalation Rules**: Multi-layer Risk Engine")
st.sidebar.markdown("- **API Security**: Server-side `.env` key storage")

# ── Main UI Layout ─────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">AmazonHelp AI Support Copilot</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Automated Intent Classification, Grounded Retrieval, Reply Generation & Escalation Decision Engine</div>', unsafe_allow_html=True)

# Determine default input value from preset selection
default_msg = PRESETS[selected_preset] if selected_preset != "Select a sample message..." else ""

# Input Form
with st.container():
    customer_message = st.text_area(
        "Customer Support Message",
        value=default_msg,
        height=100,
        placeholder="Enter customer tweet or support message (e.g., @AmazonHelp Where is my refund for order #123?)"
    )

    with st.expander("➕ Additional Conversation Context (Optional)", expanded=False):
        context_input = st.text_area(
            "Prior Conversation Context",
            height=80,
            placeholder="Paste prior back-and-forth messages if available..."
        )

    submit_btn = st.button("🚀 Analyze & Generate Reply", type="primary", use_container_width=True)

# ── Processing & Output Display ────────────────────────────────────────────────
if submit_btn:
    if not customer_message.strip():
        st.warning("Please enter a customer support message before processing.")
    else:
        with st.spinner("Processing pipeline: Classifying Intent ➔ Retrieving Evidence ➔ Generating Reply ➔ Evaluating Escalation..."):
            try:
                pipeline = SupportPipeline(mock_mode=mock_mode)
                result = pipeline.process(
                    customer_message=customer_message.strip(),
                    context=context_input.strip() if context_input else None
                )

                st.markdown("---")
                st.markdown("### Pipeline Output")

                # Metrics Row
                col1, col2, col3 = st.columns([1.5, 1.5, 2])
                
                with col1:
                    conf_val = result.get("confidence", 0.0)
                    conf_delta = f"{conf_val * 100:.1f}% Confidence" if conf_val > 0.0 else "Confidence Unavailable"
                    st.metric(
                        label="Predicted Intent",
                        value=result["intent"],
                        delta=conf_delta
                    )

                with col2:
                    decision = result["decision"]
                    if decision == "AUTO-HANDLE":
                        st.markdown('**Decision Status**')
                        st.markdown('<div class="auto-handle-badge">✅ AUTO-HANDLE</div>', unsafe_allow_html=True)
                    else:
                        st.markdown('**Decision Status**')
                        st.markdown('<div class="escalate-badge">🚨 ESCALATE TO HUMAN</div>', unsafe_allow_html=True)

                with col3:
                    st.markdown('**Escalation Reason & Risk Flags**')
                    st.write(f"*{result['escalation_reason']}*")
                    if result["risk_flags"]:
                        flag_html = "".join([f'<span class="flag-tag">{flag}</span>' for flag in result["risk_flags"]])
                        st.markdown(flag_html, unsafe_allow_html=True)
                    else:
                        st.markdown('<span class="flag-tag">NO_RISK_DETECTED</span>', unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                # Intent Explanation
                with st.expander("🔍 Intent Classification Explanation", expanded=False):
                    st.write(f"**Classifier Rationale**: {result['intent_reason']}")

                # AI Generated Reply Card
                st.markdown("#### 🤖 AI-Generated Support Reply")
                st.markdown(f'<div class="reply-box">{result["generated_reply"]}</div>', unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                # Historical Evidence Accordion
                retrieved_list = result.get("retrieved_evidence", [])
                with st.expander(f"📚 Retrieved Historical Context ({len(retrieved_list)} items)", expanded=True):
                    if not retrieved_list:
                        st.info("No historical evidence retrieved for this query.")
                    else:
                        for idx, item in enumerate(retrieved_list, 1):
                            intent_lbl = item.get('intent', 'N/A')
                            similarity = item.get('similarity_score', 0.0)
                            cust_msg = item.get('customer_message') or item.get('text') or "N/A"
                            brand_resp = item.get('historical_response') or item.get('response_text')
                            resp_html = f'<div style="margin-top: 4px; color: #334155;"><strong>AmazonHelp Reply:</strong> "{brand_resp}"</div>' if brand_resp else '<div style="margin-top: 4px; color: #94A3B8;"><em>No associated historical response available</em></div>'

                            st.markdown(
                                f"""
                                <div class="evidence-item">
                                    <strong>Example #{idx}</strong> | <em>Intent: {intent_lbl}</em> | <span>Similarity: {similarity:.2f}</span><br>
                                    <div style="margin-top: 6px; color: #0F172A;"><strong>Customer Message:</strong> "{cust_msg}"</div>
                                    {resp_html}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

            except Exception as e:
                st.error("Pipeline Execution Error")
                st.write(f"An error occurred while calling the support pipeline: `{str(e)}`")
                st.info("💡 **Troubleshooting**: Check your `.env` configuration or switch to 'Offline Mock Mode' in the sidebar.")
