# notebooks/clean_data.ipynb (ou .py)
import pandas as pd
df = pd.read_csv('data/raw/sales.csv', parse_dates=['date'])
df = df.sort_values('date')
# vérifier valeurs manquantes
print(df.isna().sum())
# ex : interpolation simple si manquant
df['sales'] = df['sales'].interpolate()
# sauvegarder
df.to_csv('data/clean/sales_clean.csv', index=False)
