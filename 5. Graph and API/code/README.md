## Code Review para Graph y API

### Para el uso de la API y calculo de las variables se utilizó el siguiente extracto

```python

import requests
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots

# Realizar una solicitud a la API para obtener los datos de casos de COVID-19 en Singapur
response = requests.get("https://api.covid19api.com/country/singapore")

singapur = 5454000

# Verificar que la solicitud se haya realizado correctamente
if response.status_code == 200:
    # Obtener los datos de casos de COVID-19 en formato JSON
    data = response.json()
    
    # Data a pandas dataframe
    df = pd.DataFrame(data)

    # Fecha y hora solo a Fecha
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    
    # Eliminar columnas que redundan información
    df.drop(['ID', 'Country', 'CountryCode', 'Province', 'City', 'CityCode', 'Lat',
       'Lon', 'Recovered'], axis=1, inplace=True)
    
    # Crear diferencia entre fechas
    df = df.merge(df.rolling(window=2).apply(np.diff), left_index=True, right_index=True,
             suffixes =('', '_day'))
    
    df['Active_day'] = df['Active_day'].clip(lower=0)
    
    # ratios de dias criticos
    df = df.merge(df[['Deaths_day', 'Active_day']].rolling(window=7).apply(np.sum), left_index=True, right_index=True,
              suffixes =('', '_roll_7'))
    
    # Ratio para identificar los periodos criticos normalizado a la poblacion total
    df['Critic_days'] = (df.Deaths_day/df.Active_day_roll_7).fillna(0)*100000
    
    df.to_csv('singapur.csv')
# En caso de que la solicitud a la API haya fallado
else:
    print("Error al obtener los datos de casos de COVID-19 en Singapur")
    

```
Basicamente se conecta a la API, se transforma a pandas dataframe, se normaliza la fecha a date y se pasan a crear las nuevas variables

### Para la generación de grafico

```python

df_g = df[df.Date> pd.to_datetime('2021-08-13')]

fig = px.line(df_g, x='Date', 
              y=list(df_g.columns.drop('Date')), 
              title='Time Series with Rangeslider')

subfig = make_subplots(specs=[[{"secondary_y": True}]])

# create two independent figures with px.line each containing data from multiple columns
fig2 = px.bar(df_g, x='Date', y=df_g['Critic_days'])

fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)


# subfig.update_xaxes(rangeslider_visible=True)
subfig.write_html("file.html")


```
El grafico se realizo con Plotly express, con la finalidad de tener un html interactivo

### Para realizar el forecast con identificación de parametros optimo local y el grafico respectivo

```python

# Libraries
# ==============================================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.model_selection import backtesting_forecaster
from skforecast.model_selection import grid_search_forecaster

# Download data
# ==============================================================================

data = pd.read_csv('singapur.csv', )
data.columns
# %%
# Data preprocessing
# ==============================================================================
data['Date'] = pd.to_datetime(data['Date'], format='%Y/%m/%d')

data = data.set_index('Date')
data = data.asfreq('D')
data.fillna(0, inplace=True)
data.replace([np.inf, -np.inf], 0, inplace=True)
data = data['Active_day']
data = data.sort_index()
data = data[data.index > '2021-09-13']

# Train-test dates
# ==============================================================================
end_train = '2023-01-01 00:00:00'

print(f"Train dates : {data.index.min()} --- {data.loc[:end_train].index.max()}  (n={len(data.loc[:end_train])})")
print(f"Test dates  : {data.loc[end_train:].index.min()} --- {data.index.max()}  (n={len(data.loc[end_train:])})")

# Plot
# ==============================================================================
fig, ax = plt.subplots(figsize=(9, 4))
data.loc[:end_train].plot(ax=ax, label='train')
data.loc[end_train:].plot(ax=ax, label='test')
ax.legend()

# %%

# Create and fit Recursive multi-step forecaster (ForecasterAutoreg)
# ==============================================================================
forecaster = ForecasterAutoreg(
                 regressor = RandomForestRegressor(
                     max_depth=50, n_estimators=25, random_state=123),
                 lags      = [ 5, 6, 7, 8, 9, 10]
             )

forecaster.fit(y=data.loc[:end_train])
forecaster

# Predict
# ==============================================================================
predictions = forecaster.predict(steps=len(data.loc[end_train:])+20)
predictions.head(3)
# %%

# Plot predictions
# ==============================================================================
fig, ax = plt.subplots(figsize=(9, 4))
data.loc[:end_train].plot(ax=ax, label='train')
data.loc[end_train:].plot(ax=ax, label='test')
predictions.plot(ax=ax, label='predictions')
ax.legend();

# %%
# Grid search hyperparameter and lags
# ==============================================================================

# Regressor hyperparameters
param_grid = {'n_estimators': [5, 25, 50, 100, 150, 250],
              'max_depth': [5, 15, 25, 50]}

# Lags used as predictors
lags_grid = [3, 10, [1, 2, 3, 5, 7, 9, 15, 20, 25]]

results_grid = grid_search_forecaster(
                   forecaster         = forecaster,
                   y                  = data,
                   param_grid         = param_grid,
                   lags_grid          = lags_grid,
                   steps              = 10,
                   refit              = True,
                   metric             = 'mean_squared_error',
                   initial_train_size = len(data.loc[:end_train]),
                   fixed_train_size   = False,
                   return_best        = True,
                   verbose            = False
               )
# %%

import plotly.express as px
from plotly.subplots import make_subplots

fig = px.line(data, 
              title='Time Series with Rangeslider')

subfig = make_subplots(specs=[[{"secondary_y": True}]])

# create two independent figures with px.line each containing data from multiple columns
fig2 = px.line(predictions)
fig2.update_traces(line_color='green', line_width=5)

# fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)


# subfig.update_xaxes(rangeslider_visible=True)
subfig.write_html("graph_with_prediction.html")

```
Para el forecast se utilizó sklearn y skforecast con un autoregresor matrices para buscar optimos locales, sumado al backtest respectivo