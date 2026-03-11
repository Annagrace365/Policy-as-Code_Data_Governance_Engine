import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pipeline.run_pipeline import run_governance_pipeline

st.set_page_config(
    page_title="Content Governance Engine",
    page_icon="🛡️",
    layout="centered"
)

# ── Brown Theme CSS ──────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Root palette ── */
:root {
    --bg-deep:    #1a0f07;
    --bg-mid:     #2c1a0e;
    --bg-card:    #3d2512;
    --accent:     #c8863a;
    --accent-lt:  #e8a95a;
    --text-main:  #f5e6d3;
    --text-muted: #b89070;
    --border:     #5a3820;
    --success-bg: #2a1f0e;
    --success-bd: #8a6030;
}

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background: linear-gradient(135deg, var(--bg-deep) 0%, var(--bg-mid) 50%, #1f1208 100%);
    min-height: 100vh;
}

/* ── Hide default header decorations ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Hero banner ── */
.hero-banner {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    margin-bottom: 1.5rem;
}
.hero-icon {
    font-size: 3.5rem;
    display: block;
    margin-bottom: 0.6rem;
    filter: drop-shadow(0 0 18px #c8863a88);
    animation: pulse 3s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { transform: scale(1);   filter: drop-shadow(0 0 18px #c8863a88); }
    50%       { transform: scale(1.06); filter: drop-shadow(0 0 30px #e8a95acc); }
}
.hero-title {
    font-size: 2.6rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent-lt) 0%, var(--accent) 50%, #a06828 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.02em;
    margin: 0;
}
.hero-sub {
    color: var(--text-muted);
    font-size: 1rem;
    margin-top: 0.5rem;
    font-weight: 400;
}

/* ── Card wrapper ── */
.card {
    background: linear-gradient(145deg, var(--bg-card), #2a1810);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.6rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(200,134,58,0.15);
    transition: box-shadow 0.3s ease;
}
.card:hover {
    box-shadow: 0 12px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(200,134,58,0.25);
}
.card-label {
    color: var(--accent);
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}

/* ── Textarea ── */
.stTextArea textarea {
    background: #110a04 !important;
    color: var(--text-main) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1.2rem !important;
    padding: 0.9rem 1rem !important;
    transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
    resize: vertical;
}
.stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(200,134,58,0.18) !important;
    outline: none !important;
}
.stTextArea label { color: var(--text-muted) !important; font-size: 0.85rem !important; }

/* ── Button ── */
.stButton {
    display: flex !important;
    justify-content: center !important;
}
.stButton > button {
    width: auto !important;
    min-width: 260px !important;
    background: linear-gradient(135deg, var(--accent) 0%, #a06828 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.75rem 2.5rem !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
    cursor: pointer !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 15px rgba(200,134,58,0.35) !important;
    margin-top: 0.4rem;
}
.stButton > button:hover {
    background: linear-gradient(135deg, var(--accent-lt) 0%, var(--accent) 100%) !important;
    box-shadow: 0 6px 22px rgba(200,134,58,0.55) !important;
    transform: translateY(-2px) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Success result box ── */
.stSuccess {
    background: var(--success-bg) !important;
    border: 1px solid var(--success-bd) !important;
    border-radius: 10px !important;
    color: var(--text-main) !important;
}

/* ── Warning / info ── */
.stWarning {
    background: #251500 !important;
    border-left: 4px solid #c88030 !important;
    border-radius: 8px !important;
    color: var(--text-main) !important;
}

/* ── Result subheader ── */
.result-header {
    color: var(--accent-lt);
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(to right, transparent, var(--border), transparent);
    margin: 1rem 0;
}

/* ── Footer ── */
.footer {
    text-align: center;
    color: #5a3820;
    font-size: 0.75rem;
    margin-top: 2.5rem;
    padding-bottom: 1.5rem;
    letter-spacing: 0.06em;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <span class="hero-icon">🛡️</span>
    <h1 class="hero-title">Content Governance Engine</h1>
    <p class="hero-sub">Detect &amp; sanitize sensitive data based on governance policies</p>
</div>
""", unsafe_allow_html=True)

# ── Input Card ────────────────────────────────────────────────────────────────
st.markdown('<div class="card"><div class="card-label">📝 Input</div>', unsafe_allow_html=True)
user_input = st.text_area(
    "Enter text to analyze",
    placeholder="Paste or type your content here…",
    height=180,
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

# ── Run Button ───────────────────────────────────────────────────────────────
run = st.button("🔍  Run Governance Check")

# ── Result ───────────────────────────────────────────────────────────────────
if run:
    if user_input.strip() == "":
        st.warning("⚠️  Please enter some text before running the check.")
    else:
        with st.spinner("Analyzing content…"):
            result = run_governance_pipeline(user_input)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card">'
                    '<div class="card-label">✅ Sanitized Output</div>',
                    unsafe_allow_html=True)
        st.success(result)
        st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown('<div class="footer">Policy-as-Code · Data Governance Engine · 2026</div>',
            unsafe_allow_html=True)