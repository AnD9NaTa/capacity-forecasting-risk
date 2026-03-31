import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range("2020-01-01", periods=300)
trend = np.linspace(100, 200, 300)
seasonality = 10*np.sin(np.linspace(0, 20, 300))
noise = np.random.normal(0, 5, 300)

df = pd.DataFrame({
    "date": dates,
    "demand": trend + seasonality + noise
})

df.to_csv("data/demand.csv", index=False)