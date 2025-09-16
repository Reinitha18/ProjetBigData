from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import pandas as pd

# Charge les données
df = pd.read_csv("data/raw/sales.csv")   # adapte le chemin si besoin
print(df.head())  # aperçu des premières lignes


# Série de données
series = df['sales']

# ARIMA(p,d,q) = (5,1,0) ici pour test simple
model = ARIMA(series, order=(5,1,0))
model_fit = model.fit()

# Prévoir 30 jours
forecast = model_fit.get_forecast(30)
pred = forecast.predicted_mean
ci = forecast.conf_int()

# Visualiser
plt.figure(figsize=(10,5))
plt.plot(series, label='Historique')
plt.plot(pred.index, pred, label='Prévision', color='red')
plt.fill_between(ci.index, ci.iloc[:,0], ci.iloc[:,1], color='pink', alpha=0.3)
plt.legend()
plt.show()
