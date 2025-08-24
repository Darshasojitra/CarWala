import pandas as pd

df = pd.read_csv("data/clean.csv")
wide = df.pivot(index="date", columns="english_name", values="monthly_value")
wide.corr().to_csv("data/correlation.csv")
print("correlation saved")
