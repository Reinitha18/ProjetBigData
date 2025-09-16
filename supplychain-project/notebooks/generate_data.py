# notebooks/generate_data.py
import pandas as pd
import numpy as np
dates = pd.date_range('2024-01-01', periods=365, freq='D')
np.random.seed(42)
season = 20 * np.sin(2 * np.pi * dates.dayofyear / 365)
trend = np.linspace(0,5,len(dates))
noise = np.random.normal(0,5,len(dates))
sales = (100 + season + trend + noise).round().astype(int)
df = pd.DataFrame({'date': dates, 'sales': sales})
df.to_csv('data/raw/sales.csv', index=False)
print("Fichier créé : data/raw/sales.csv")
