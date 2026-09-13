import streamlit as st
import joblib
import numpy as np

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AVENGERS | Sales Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CAPTAIN AMERICA / AVENGERS CSS
# ============================================================

st.markdown("""
<style>

    /* ---------- GLOBAL ---------- */
    .stApp {
        background:
            radial-gradient(circle at 50% 10%, rgba(30, 70, 130, 0.35), transparent 35%),
            linear-gradient(135deg, #020617 0%, #07152e 45%, #020617 100%);
        color: #f8fafc;
        font-family: 'Arial', sans-serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ---------- HERO HEADER ---------- */

    .hero {
        text-align: center;
        padding: 35px 20px 25px 20px;
        margin-bottom: 25px;
    }

    .shield {
        font-size: 72px;
        margin-bottom: 5px;
        filter: drop-shadow(0px 0px 18px rgba(37, 99, 235, 0.7));
    }

    .avengers-title {
        font-size: 48px;
        font-weight: 900;
        letter-spacing: 5px;
        color: #ffffff;
        text-shadow:
            0px 0px 10px rgba(59, 130, 246, 0.8),
            0px 0px 25px rgba(220, 38, 38, 0.4);
        margin: 0;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 16px;
        letter-spacing: 3px;
        margin-top: 8px;
        text-transform: uppercase;
    }

    .mission {
        display: inline-block;
        margin-top: 18px;
        padding: 7px 18px;
        border-radius: 20px;
        border: 1px solid #dc2626;
        color: #fca5a5;
        background: rgba(127, 29, 29, 0.25);
        font-size: 12px;
        letter-spacing: 2px;
        font-weight: bold;
    }

    /* ---------- CARDS ---------- */

    .section-card {
        background: rgba(15, 23, 42, 0.82);
        border: 1px solid rgba(59, 130, 246, 0.45);
        border-radius: 18px;
        padding: 25px;
        box-shadow:
            0 8px 30px rgba(0, 0, 0, 0.35),
            inset 0 0 20px rgba(30, 64, 175, 0.08);
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 20px;
        font-weight: 800;
        color: #e2e8f0;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }

    .section-description {
        color: #64748b;
        font-size: 13px;
        margin-bottom: 20px;
    }

    /* ---------- INPUT LABELS ---------- */

    label {
        color: #cbd5e1 !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px;
    }

    /* ---------- NUMBER INPUT ---------- */

    div[data-testid="stNumberInput"] input {
        background: rgba(2, 6, 23, 0.9) !important;
        color: #f8fafc !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }

    div[data-testid="stNumberInput"] input:focus {
        border: 1px solid #3b82f6 !important;
        box-shadow: 0 0 12px rgba(59, 130, 246, 0.35) !important;
    }

    /* ---------- PREDICT BUTTON ---------- */

    div.stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 12px;
        border: 2px solid #dc2626;
        background:
            linear-gradient(135deg, #b91c1c, #dc2626);
        color: white;
        font-size: 17px;
        font-weight: 900;
        letter-spacing: 2px;
        transition: all 0.25s ease;
        box-shadow:
            0 0 15px rgba(220, 38, 38, 0.25);
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        border-color: #60a5fa;
        background: linear-gradient(135deg, #dc2626, #991b1b);
        box-shadow:
            0 0 25px rgba(220, 38, 38, 0.5);
    }

    /* ---------- RESULT ---------- */

    .result-card {
        text-align: center;
        padding: 30px;
        margin-top: 25px;
        border-radius: 18px;
        border: 2px solid #3b82f6;
        background:
            radial-gradient(circle at center,
                rgba(37, 99, 235, 0.25),
                rgba(15, 23, 42, 0.9));
        box-shadow:
            0 0 30px rgba(37, 99, 235, 0.25);
    }

    .result-label {
        color: #93c5fd;
        font-size: 13px;
        letter-spacing: 3px;
        font-weight: bold;
    }

    .result-number {
        font-size: 48px;
        font-weight: 900;
        color: #ffffff;
        margin: 8px 0;
        text-shadow: 0 0 15px rgba(96, 165, 250, 0.7);
    }

    .result-status {
        color: #86efac;
        font-size: 13px;
        letter-spacing: 1px;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        margin-top: 35px;
        padding: 15px;
        color: #475569;
        font-size: 11px;
        letter-spacing: 2px;
    }

    .footer span {
        color: #dc2626;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load(open('linear_reg.sav', 'rb'))


# ============================================================
# HERO SECTION
# ============================================================

st.markdown("""
<div class="hero">

    <div class="shield">🛡️</div>

    <div class="avengers-title">
        AVENGERS
    </div>

    <div class="subtitle">
        Sales Intelligence Command Center
    </div>

    <div class="mission">
        ◉ MISSION STATUS : ACTIVE
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MAIN LAYOUT
# ============================================================

left, right = st.columns([1.8, 1], gap="large")


# ============================================================
# INPUT PANEL
# ============================================================

with left:

    st.markdown("""
    <div class="section-card">

        <div class="section-title">
            ⚡ MISSION PARAMETERS
        </div>

        <div class="section-description">
            Configure advertising resources to deploy the Sales Prediction Protocol.
        </div>

    </div>
    """, unsafe_allow_html=True)

    TV = st.number_input(
        "📺 TV Advertising Budget",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

    Radio = st.number_input(
        "📻 Radio Advertising Budget",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

    Newspaper = st.number_input(
        "📰 Newspaper Advertising Budget",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

    st.markdown("<br>", unsafe_allow_html=True)

    predict = st.button("🛡️  INITIATE SALES PREDICTION")


# ============================================================
# AVENGERS STATUS PANEL
# ============================================================

with right:

    st.markdown("""
    <div class="section-card">

        <div class="section-title">
            ⭐ AVENGERS PROTOCOL
        </div>

        <div class="section-description">
            Predictive intelligence system online.
        </div>

        <p style="color:#94a3b8; font-size:13px;">
            The model analyses your advertising allocation
            across three channels and estimates the expected
            sales outcome.
        </p>

        <br>

        <div style="
            border-left:3px solid #dc2626;
            padding-left:15px;
            margin-bottom:15px;
        ">
            <div style="color:#f87171;font-weight:bold;">
                CAPTAIN AMERICA
            </div>
            <div style="color:#64748b;font-size:12px;">
                Strategy & Coordination
            </div>
        </div>

        <div style="
            border-left:3px solid #3b82f6;
            padding-left:15px;
        ">
            <div style="color:#60a5fa;font-weight:bold;">
                JARVIS
            </div>
            <div style="color:#64748b;font-size:12px;">
                Predictive Intelligence
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# PREDICTION
# ============================================================

if predict:

    input_data = np.array([
        [TV, Radio, Newspaper]
    ])

    prediction = model.predict(input_data)[0]

    st.markdown(f"""
    <div class="result-card">

        <div class="result-label">
            🛡️ PREDICTION PROTOCOL COMPLETE
        </div>

        <div class="result-number">
            {prediction:.2f}
        </div>

        <div class="result-status">
            ✓ SALES FORECAST SUCCESSFULLY GENERATED
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    AVENGERS SALES INTELLIGENCE SYSTEM
    <span> • </span>
    POWERED BY MACHINE LEARNING
    <span> • </span>
    MARVEL-INSPIRED INTERFACE
</div>
""", unsafe_allow_html=True)
