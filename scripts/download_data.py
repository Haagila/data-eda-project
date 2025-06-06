import yfinance as yf
import pandas as pd

# Defino los Tickers seleccionados
tickers = ['NVDA', 'MSFT', 'GOOGL', 'BOTZ', 'ARKQ']

# Para el análisis, me enfoco en un periodo de 10 años
start_date = '2015-04-20'
end_date = '2025-04-20'

# Descargar los datos históricos de los tickers
data = yf.download(tickers, start=start_date, end=end_date)

# Guardar los datos descargados en un archivo CSV
data.to_csv('data/financial_data.csv')

# Mostrar las primeras filas de los datos
print(data.head())
