import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean.csv")
f = pd.read_csv("data/forecasts.csv")
c = pd.read_csv("data/correlation.csv", index_col=0)

st.title("Car Sales Forecast")

kpi = st.selectbox("Choose KPI", df["english_name"].unique())
hist = df[df["english_name"] == kpi]
fc = f[f["kpi"] == kpi]

plt.plot(hist["date"], hist["monthly_value"], label="history")
plt.plot(fc["date"], fc["forecast"], "--", label="forecast")
plt.legend()
st.pyplot(plt)

st.subheader("KPI Correlation")
st.dataframe(c.round(2))
