import streamlit as st
import joblib
import numpy as np

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Blueberry Sales Predictor",
    page_icon="🫐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# BLUEBERRY THEME
# ---------------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99, 102, 241, 0.25), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(168, 85, 247, 0.20), transparent 30%),
        linear-gradient(135deg, #08051a 0%, #15103b 50%, #08051a 100%);
    color: white;
    font-family: 'Poppins', sans-serif;
}

/* Remove Streamlit default elements */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ---------------------------------------------------------
   HEADER
--------------------------------------------------------- */

.hero {
    text-align: center;
    padding: 30px 10px 35px 10px;
}

.berry-icon {
    font-size: 65px;
    margin-bottom: 5px;
    filter: drop-shadow(0px 0px 18px rgba(129, 140, 248, 0.8));
}

.title {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #f5f3ff;
    margin: 0;
}

.title span {
    color: #a78bfa;
}

.subtitle {
    font-family: 'Poppins', sans-serif;
    color: #c4b5fd;
    font-size: 14px;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-top: 8px;
}

.tag {
    display: inline-block;
    margin-top: 18px;
    padding: 7px 18px;
    border-radius: 30px;
    background: rgba(124, 58, 237, 0.15);
    border: 1px solid rgba(167, 139, 250, 0.5);
    color: #c4b5fd;
    font-size: 11px;
    letter-spacing: 2px;
}

/* ---------------------------------------------------------
   CARDS
--------------------------------------------------------- */

.card {
    background: rgba(17, 12, 45, 0.82);
    border: 1px solid rgba(139, 92, 246, 0.35);
    border-radius: 22px;
    padding: 28px;
    box-shadow:
        0px 15px 40px rgba(0, 0, 0, 0.3),
        inset 0px 0px 25px rgba(139, 92, 246, 0.04);
    backdrop-filter: blur(12px);
}

.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 23px;
    font-weight: 700;
    color: #ddd6fe;
}

.card-description {
    color: #8b86a8;
    font-size: 13px;
    margin-top: 5px;
    margin-bottom: 20px;
}

/* ---------------------------------------------------------
   INPUTS
--------------------------------------------------------- */

label {
    color: #c4b5fd !important;
    font-weight: 600 !important;
    font-family: 'Poppins', sans-serif !important;
}

div[data-testid="stNumberInput"] input {
    background: rgba(8, 5, 26, 0.9) !important;
    color: #f5f3ff !important;
    border: 1px solid #433875 !important;
    border-radius: 12px !important;
    font-family: 'Poppins', sans-serif !important;
}

div[data-testid="stNumberInput"] input:focus {
    border: 1px solid #8b5cf6 !important;
    box-shadow: 0px 0px 12px rgba(139, 92, 246, 0.3) !important;
}

/* ---------------------------------------------------------
   BUTTON
--------------------------------------------------------- */

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: 1px solid #8b5cf6;
    background: linear-gradient(
        135deg,
        #4c1d95,
        #6d28d9
    );
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1px;
    transition: all 0.25s ease;
    box-shadow: 0px 8px 25px rgba(109, 40, 217, 0.25);
}

.stButton > button:hover {
    transform: translateY(-2px);
    background: linear-gradient(
        135deg,
        #6d28d9,
        #8b5cf6
    );
    box-shadow: 0px 10px 30px rgba(139, 92, 246, 0.45);
}

/* ---------------------------------------------------------
   SIDE INFORMATION
--------------------------------------------------------- */

.info-title {
    font-family: 'Playfair Display', serif;
    font-size: 21px;
    color: #ddd6fe;
    margin-bottom: 15px;
}

.info-item {
    padding: 13px;
    margin: 10px 0;
    border-radius: 12px;
    background: rgba(139, 92, 246, 0.08);
    border-left: 3px solid #8b5cf6;
}

.info-item b {
    color: #c4b5fd;
}

.info-item span {
    color: #777394;
    font-size: 12px;
}

/* ---------------------------------------------------------
   PREDICTION RESULT
--------------------------------------------------------- */

.result {
    text-align: center;
    margin-top: 25px;
    padding: 32px;
    border-radius: 22px;
    background:
        radial-gradient(
            circle at center,
            rgba(124, 58, 237, 0.25),
            rgba(17, 12, 45, 0.9)
        );
    border: 1px solid #8b5cf6;
    box-shadow:
        0px 0px 35px rgba(139, 92, 246, 0.18);
}

.result-label {
    color: #a78bfa;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 600;
}

.result-number {
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    font-weight: 800;
    color: #f5f3ff;
    margin: 5px 0;
    text-shadow: 0px 0px 20px rgba(167, 139, 250, 0.6);
}

.result-success {
    color: #86efac;
    font-size: 12px;
    letter-spacing: 1px;
}

/* ---------------------------------------------------------
   FOOTER
--------------------------------------------------------- */

.custom-footer {
    text-align: center;
    color: #625d7d;
    font-size: 10px;
    letter-spacing: 2px;
    margin-top: 40px;
    padding-bottom: 15px;
}

.custom-footer span {
    color: #8b5cf6;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------

model = joblib.load(open("linear_reg.sav", "rb"))

# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------

st.markdown("""
<div class="hero">

    <div class="berry-icon">🫐</div>

    <div class="title">
        Blueberry <span>Analytics</span>
    </div>

    <div class="subtitle">
        Sales Prediction Studio
    </div>

    <div class="tag">
        ✦ INTELLIGENT SALES FORECASTING ✦
    </div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------------

left, right = st.columns([1.7, 1], gap="large")

# ---------------------------------------------------------
# LEFT PANEL
# ---------------------------------------------------------

with left:

    st.markdown("""
    <div class="card">

        <div class="card-title">
            🫐 Advertising Parameters
        </div>

        <div class="card-description">
            Enter your advertising investments to discover the
            expected sales performance.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    TV = st.number_input(
        "📺 TV Advertising Budget",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

    Radio = st.number_input(
        "🎧 Radio Advertising Budget",
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

    st.write("")

    predict = st.button("🫐  PREDICT SALES")

# ---------------------------------------------------------
# RIGHT PANEL
# ---------------------------------------------------------

with right:

    st.markdown("""
    <div class="card">

        <div class="info-title">
            🫐 Prediction Intelligence
        </div>

        <div class="info-item">
            <b>📺 TV</b><br>
            <span>Television advertising investment</span>
        </div>

        <div class="info-item">
            <b>🎧 Radio</b><br>
            <span>Radio advertising investment</span>
        </div>

        <div class="info-item">
            <b>📰 Newspaper</b><br>
            <span>Print advertising investment</span>
        </div>

        <br>

        <div style="
            text-align:center;
            color:#a78bfa;
            font-size:13px;
        ">
            ✦ AI MODEL READY ✦
        </div>

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------

if predict:

    input_data = np.array([
        [TV, Radio, Newspaper]
    ])

    prediction = model.predict(input_data)[0]

    st.markdown(f"""
    <div class="result">

        <div class="result-label">
            🫐 PREDICTED SALES
        </div>

        <div class="result-number">
            {prediction:.2f}
        </div>

        <div class="result-success">
            ✓ FORECAST GENERATED SUCCESSFULLY
        </div>

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("""
<div class="custom-footer">
    🫐 BLUEBERRY ANALYTICS
    <span>•</span>
    MACHINE LEARNING SALES PREDICTOR
    <span>•</span>
    DATA DRIVEN DECISIONS
</div>
""", unsafe_allow_html=True)
