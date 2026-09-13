import streamlit as st
import joblib
import numpy as np

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Blueberry Analytics",
    page_icon="🫐",
    layout="wide"
)

# ---------------------------------------------------------
# BLUEBERRY THEME
# ---------------------------------------------------------

st.title("🫐 Blueberry Analytics")
st.subheader("✨ Sales Prediction Studio")

st.write(
    "A simple machine learning dashboard for predicting sales "
    "based on advertising expenditure."
)

st.divider()

# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------

model = joblib.load(open("linear_reg.sav", "rb"))

# ---------------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------------

left, right = st.columns([2, 1])

# ---------------------------------------------------------
# LEFT PANEL — INPUTS
# ---------------------------------------------------------

with left:

    st.header("🫐 Advertising Parameters")

    st.info(
        "Enter your advertising budgets below and let the "
        "prediction model estimate your expected sales."
    )

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

    predict = st.button(
        "🫐 Predict Sales",
        use_container_width=True
    )

# ---------------------------------------------------------
# RIGHT PANEL — INFORMATION
# ---------------------------------------------------------

with right:

    st.header("🔵 Model Intelligence")

    st.success("🟢 Model Online")

    st.metric(
        "📺 TV",
        f"{TV:.0f}"
    )

    st.metric(
        "🎧 Radio",
        f"{Radio:.0f}"
    )

    st.metric(
        "📰 Newspaper",
        f"{Newspaper:.0f}"
    )

    st.caption(
        "🫐 Three advertising channels • "
        "One intelligent prediction"
    )

# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------

if predict:

    input_data = np.array([
        [TV, Radio, Newspaper]
    ])

    prediction = model.predict(input_data)[0]

    st.divider()

    st.header("🫐 Prediction Result")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.success("✨ Prediction generated successfully!")

        st.metric(
            label="EXPECTED SALES",
            value=f"{prediction:.2f}"
        )

        st.write(
            "🫐 Your advertising investment has been "
            "processed by the sales prediction model."
        )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "🫐 Blueberry Analytics • Machine Learning Sales Predictor"
)
