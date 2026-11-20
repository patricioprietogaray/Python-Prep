# 🏠 Enunciado del Ejercicio: 
# Predicción de Precios de Viviendas
# Imagina que trabajas como analista de datos 
# y tienes un conjunto de datos con información de 100 viviendas. 
# Los datos vienen en tres arrays de NumPy independientes:
# * metros_cuadrados: 
#   superficie de la casa.
# * habitaciones: 
#   número de habitaciones.
# * precio: 
#   precio real de venta en miles de dólares ($k).
# 
# Tus objetivos son:
#   * Análisis Exploratorio Básico: 
#   Calcular la media, el valor máximo, 
#   el valor mínimo y la desviación estándar de los precios 
#   y de los metros cuadrados.
#   * Filtrado: 
#   Filtrar el dataset para trabajar únicamente con 
#   las casas que tengan un precio menor o igual al percentil 90 
#   (eliminando posibles valores atípicos caros).
#   * Modelado (Regresión Lineal Múltiple): 
#   Ajustar un modelo de regresión lineal utilizando 
#   la fórmula matricial de mínimos cuadrados ordinarios (OLS):
#       theta = (X^T * X)^{-1} * X^T * y
#       Para predecir el precio utilizando como variables independientes (X) 
#       los metros cuadrados y las habitaciones.
#   * Evaluación: 
#   Calcular el Error Cuadrático Medio (MSE) de las 
#   predicciones del modelo sobre los datos filtrados.

# RESOLUCION DEL EJERCICIO

import numpy as np 

# semilla para generar numeros aleatorios
# reproducibilidad de los datos simulados
np.random.seed(42)

# 0 -- Generacion del conjunto de datos simulados ---
# Predicción de Precios de 100 Viviendas

# cantidad de viviendas
n_muestras = 100

# generar aleatoriamente los metros cuadrados de 100 viviendas
# rango de las viviendas como minimo 50 m2 hasta 250m2
metros_cuadrados = np.random.uniform(50,250,n_muestras)

# generar habitaciones acorde a la cantidad de metros cuadrados de la casa
# Por ejemplo: base de 1 habitación + 1 extra por cada ~50 m² + algo de variación aleatoria
habitaciones = 1 + (metros_cuadrados // 50) + np.random.choice([0, 1], n_muestras, p=[0.6, 0.4])
habitaciones = habitaciones.astype(int)  # Convertir a números enteros

# generar aleatoriamente la cantidad de habitaciones entre 1 y 5
# habitaciones = np.random.randint(1,6,n_muestras)

baños = np.random.randint(1, 3, n_muestras)  # Entre 1 y 2 baños

# print(n_muestras)
# print(metros_cuadrados)
# print(habitaciones)

# for i in range(15):
#     print(f"Casa {i+1}: {metros_cuadrados[i]:.1f} m² | {habitaciones[i]} habitaciones | {baños[i]} baño(s)")

# # Precio simulado: base + factor por metro + factor por habitación + ruido aleatorio
precio = 50 + (2.5 * metros_cuadrados) + (15 * habitaciones) + np.random.normal(0, 10, n_muestras)

print(precio)
print("=== 1. ANÁLISIS EXPLORATORIO BÁSICO ===")

# print(f"Precio medio: ${np.mean(precio):.2f}k | Desviación estándar: ${np.std(precio):.2f}k")
# print(f"Metros cuadrados medios: {np.mean(metros_cuadrados):.2f} m² (Mín: {np.min(metros_cuadrados):.2f}, Máx: {np.max(metros_cuadrados):.2f})")

# # --- 2. FILTRADO DE DATOS (Eliminar outliers por percentil 90 de precio) ---
# limite_precio = np.percentile(precio, 90)
# mascara_filtro = precio <= limite_precio

# # Aplicamos la máscara para filtrar
# metros_filtrados = metros_cuadrados[mascara_filtro]
# habitaciones_filtradas = habitaciones[mascara_filtro]
# precio_filtrado = precio[mascara_filtro]

# print(f"\nDatos iniciales: {len(precio)} casas. Tras filtrar el top 10% más caro: {len(precio_filtrado)} casas.")

# # --- 3. MODELADO: REGRESIÓN LINEAL MÚLTIPLE (Matricial) ---
# # Construimos la matriz de diseño X con una columna de 1s para el término independiente (intercepto)
# X = np.column_stack((
#     np.ones(len(metros_filtrados)), 
#     metros_filtrados, 
#     habitaciones_filtradas
# ))
# y = precio_filtrado

# # Aplicamos la ecuación normal de mínimos cuadrados: theta = (X^T * X)^(-1) * X^T * y
# # np.linalg.inv calcula la inversa de la matriz
# # np.dot o el operador @ multiplican matrices
# X_transpuesta = X.T
# theta = np.linalg.inv(X_transpuesta @ X) @ X_transpuesta @ y

# intercepto, coef_metros, coef_habitaciones = theta
# print(f"\n=== 3. COEFICIENTES DEL MODELO ===")
# print(f"Intercepto (Sesgo): {intercepto:.4f}")
# print(f"Coeficiente por m²: {coef_metros:.4f}")
# print(f"Coeficiente por habitación: {coef_habitaciones:.4f}")

# # --- 4. PREDICCIÓN Y EVALUACIÓN (MSE) ---
# # Predicciones con el modelo aprendido: y_pred = X * theta
# y_pred = X @ theta

# # Error Cuadrático Medio (Mean Squared Error)
# mse = np.mean((y_pred - y) ** 2)
# print(f"\n=== 4. EVALUACIÓN ===")
# print(f"Error Cuadrático Medio (MSE): {mse:.4f}")

# # Ejemplo de predicción para una casa de 120 m² y 3 habitaciones:
# casa_nueva = np.array([1, 120, 3])  # El 1 es por el término independiente
# precio_estimado = casa_nueva @ theta
# print(f"Predicción para una casa de 120 m² y 3 habitaciones: ${precio_estimado:.2f}k")