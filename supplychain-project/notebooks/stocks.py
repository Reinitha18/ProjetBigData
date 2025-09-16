import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Exemple de prévisions (tu peux remplacer par ton modèle ARIMA/Prophet)
dates = pd.date_range("2025-01-01", periods=30)
forecast = np.random.normal(100, 10, size=30)  # ventes prévues
df_forecast = pd.DataFrame({"date": dates, "demand_forecast": forecast})

# Politique de stock : on garde 10% de marge de sécurité
df_forecast["stock_needed"] = df_forecast["demand_forecast"] * 1.1

print(df_forecast.head())

# Visualisation
plt.figure(figsize=(10,5))
plt.plot(df_forecast["date"], df_forecast["demand_forecast"], label="Prévision de demande")
plt.plot(df_forecast["date"], df_forecast["stock_needed"], label="Stock recommandé", linestyle="--")
plt.legend()
plt.title("Optimisation des stocks avec marge de sécurité")
plt.show()
