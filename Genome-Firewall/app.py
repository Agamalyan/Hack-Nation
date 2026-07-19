
import streamlit as st
import pandas as pd
import joblib


model = joblib.load("genome_firewall_model.pkl")


st.title("🧬 Genome Firewall")
st.subheader("AI-assisted antibiotic resistance prediction")


st.warning(
    "This prototype is for research demonstration only. "
    "Results must be confirmed by laboratory testing."
)


st.write("Enter bacterial genome metadata:")


genome_name = st.text_input(
    "Genome name",
    "Escherichia coli sample"
)

taxon_id = st.number_input(
    "Taxon ID",
    value=562
)

genome_id = st.number_input(
    "Genome ID",
    value=562.123456
)

measurement = st.number_input(
    "Measurement value (optional)",
    value=1.0
)


if st.button("Predict"):

    sample = pd.DataFrame({
        "Taxon ID": [taxon_id],
        "Genome ID": [genome_id],
        "Genome Name": [genome_name],
        "Measurement Value": [measurement]
    })


    probability = model.predict_proba(sample)[0][1]


    if probability >= 0.7:
        prediction = "Likely to fail"
        confidence = probability

    elif probability <= 0.3:
        prediction = "Likely to work"
        confidence = 1 - probability

    else:
        prediction = "No-call"
        confidence = 0.5


    st.success(prediction)

    st.metric(
        "Confidence",
        f"{confidence:.1%}"
    )


    st.write(
        "Prediction probability of resistance:",
        f"{probability:.1%}"
    )
