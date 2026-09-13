import streamlit as st
import joblib
import numpy as np

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Avengers Sales Intelligence",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------------------------------
# CAPTAIN AMERICA THEME
# ---------------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #020617, #071a3d, #020617);
        color: white;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 900;
        letter-spacing: 5px;
        color: white;
        margin-bottom: 0px;
        text-shadow: 0px 0px 15px #2563eb;
    }

    .sub-title {
        text-align: center;
        color: #93c5fd;
        font-size: 15px;
        letter-spacing: 3px;
        margin-bottom: 30px;
    }

    /* Cards */
    .card {
        background: rgba(15, 23, 42, 0.9);
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #2563eb;
        box-shadow: 0px 0px 20px rgba(37, 99, 235, 0.2);
    }

    .card-title {
        color: #60a5fa;
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .card-text {
        color: #94a3b8;
        font-size: 14px;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background: #b91c1c;
        color: white;
        border: 2px solid #ef4444;
        border-radius: 12px;
        height: 55px;
        font-size: 17px;
        font-weight: 800;
        letter-spacing: 1px;
    }

    .stButton > button:hover {
        background: #dc2626;
        border-color: #60a5fa;
        box-shadow: 0px 0px 20px rgba(220, 38, 38, 0.5);
    }

    /* Input boxes */
    div[data-testid="stNumberInput"] input {
        background-color: #020617;
        color: white;
        border: 1px solid #334155;
        border-radius: 10px;
    }

    /* Prediction */
    .prediction {
        text-align: center;
        background: linear-gradient(
            135deg,
            rgba(30, 64, 175, 0.4),
            rgba(127, 29, 29, 0.4)
        );
        border: 2px solid #3b82f6;
        border-radius: 18px;
        padding: 25px;
        margin-top: 25px;
    }

    .prediction-title {
        color: #93c5fd;
        font-size: 14px;
        letter-spacing: 2px;
    }

    .prediction-value {
        color: white;
        font-size: 48px;
        font-weight: 900;
        text-shadow: 0px 0px 15px #3b82f6;
    }

    .footer {
        text-align: center;
        color: #475569;
        font-size: 11px;
        letter-spacing: 2px;
        margin-top: 35px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------
model = joblib.load(open("linear_reg.sav", "rb"))

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">🛡️ AVENGERS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">SALES INTELLIGENCE COMMAND CENTER</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# LAYOUT
# ---------------------------------------------------------
left, right = st.columns([1.7, 1])

# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------
with left:

    st.markdown(
        '<div class="card">'
        '<div class="card-title">⚡ MISSION PARAMETERS</div>'
        '<div class="card-text">'
        'Configure the advertising budget to generate the sales forecast.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

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

    st.write("")

    predict = st.button("🛡️ INITIATE SALES PREDICTION")

# ---------------------------------------------------------
# AVENGERS PANEL
# ---------------------------------------------------------
with right:

    st.markdown(
        '<div class="card">'
        '<div class="card-title">⭐ AVENGERS PROTOCOL</div>'
        '<div class="card-text">'
        '<br>'
        '🛡️ <b>CAPTAIN AMERICA</b><br>'
        '<span style="color:#64748b;">Strategy & Coordination</span>'
        '<br><br>'
        '🤖 <b>JARVIS</b><br>'
        '<span style="color:#64748b;">Predictive Intelligence</span>'
        '<br><br>'
        '🔴 <b>MISSION STATUS</b><br>'
        '<span style="color:#4ade80;">● SYSTEM ONLINE</span>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------
if predict:

    input_data = np.array([[TV, Radio, Newspaper]])

    prediction = model.predict(input_data)[0]

    st.markdown(
        f'<div class="prediction">'
        f'<div class="prediction-title">'
        f'🛡️ SALES PREDICTION COMPLETE'
        f'</div>'
        f'<div class="prediction-value">'
        f'{prediction:.2f}'
        f'</div>'
        f'<div style="color:#4ade80;">'
        f'✓ FORECAST GENERATED SUCCESSFULLY'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    '<div class="footer">'
    'AVENGERS SALES INTELLIGENCE • MACHINE LEARNING SYSTEM'
    '</div>',
    unsafe_allow_html=True
)
