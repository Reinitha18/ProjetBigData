import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data/clean/sales_clean.csv', parse_dates=['date']).set_index('date')
df['sales'].rolling(7).mean().plot(title='Ventes (MA7)')
plt.show()
