# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:57:56 2022

@author: GABRIELA
"""

#importar las librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importar dataset
bici = pd.read_csv('bike_train.csv', sep=';',encoding='latin-1')

#Dividir el dataset en variables independientes y dependientes
x = bici.iloc [:,2:-1].values
y = bici.iloc [:, 16].values #variable dependiente


# Uso de modelo de RLM utilzando el método de eliminación hacia atrás.
import statsmodels.api as sm
# Agregar un array de unos para poder emplear el método de eliminación.
x = np.append (arr = np.ones((11999,1)).astype(int), values = x , axis = 1)

# Seleccionar el nivel de significación SL:0.05
SL = 0.05
x_uno = x[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
regressor_OLS = sm.OLS(endog = y, exog = x_uno).fit()

# Considerar la variable predictora
print(regressor_OLS.summary())

# Eliminando variables fuera del rango SL
x_uno = x[:, [0,1,2,3,4,13,14]]
regressor_OLS = sm.OLS(endog = y, exog = x_uno).fit()
print(regressor_OLS.summary())

# Usamos las variables más estables
"""x_uno = x[:, [0,1,2,3,4,13,14]]"""

# Dividir el data set en conjunto de entrenamiento y testing (20% para el test, resto entrenamiento)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_uno,y, test_size= 0.20, random_state = 0)


# Ajustar el modelo de regresión lineal múltiple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regresion = LinearRegression().fit(x_train,y_train)

#predicción de los resultados en el conjunto de testing
y_pred = regresion.predict(x_test)


# Uso metrica RMSE
from sklearn.metrics import mean_squared_error

# RMSE train dataset
print(np.sqrt(mean_squared_error(y_train, regresion.predict(x_train))))
# RMSE test dataset
print(np.sqrt(mean_squared_error(y_test, regresion.predict(x_test))))


# Convertir prediccion a archivo CSV

predicciones = pd.DataFrame(y_pred, columns = ["pred"])
predicciones.to_csv("Gabyha.csv", index = False)















