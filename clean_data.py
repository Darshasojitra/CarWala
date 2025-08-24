pip install -r requirements.txt
python clean_data.py
python forecast.py
python correlation.py
streamlit run app.py


import pandas as pd

df = pd.read_csv("data/raw.csv")
df = df[["account_id", "english_name", "year", "month", "monthly_value"]]
df["date"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str) + "-01")
df = df.sort_values(["english_name", "date"])
df.to_csv("data/clean.csv", index=False)
print("data cleaned and saved")
