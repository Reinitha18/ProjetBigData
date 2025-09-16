# dashboards/app.py
import streamlit as st
import pandas as pd

df = pd.read_csv("data/clean/sales_clean.csv", parse_dates=["date"])

st.title("Dashboard logistique")
st.line_chart(df.set_index("date")["sales"])
st.write("Prévisions, stocks et itinéraires viendront ici...")
