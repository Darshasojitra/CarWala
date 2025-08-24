import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv("data/clean.csv")
out = []

for name, g in df.groupby("english_name"):
    s = g.set_index("date")["monthly_value"]
    try:
        m = ExponentialSmoothing(s, trend="add", seasonal="add", seasonal_periods=12).fit()
        f = m.forecast(3)
    except:
        f = pd.Series([s.iloc[-1]]*3, index=pd.date_range(s.index[-1], periods=3, freq="M"))
    for d, v in f.items():
        out.append([name, d.strftime("%Y-%m"), v])

pd.DataFrame(out, columns=["kpi", "date", "forecast"]).to_csv("data/forecasts.csv", index=False)
print("forecast done")
