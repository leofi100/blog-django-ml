"""
# machine learning


from sklearn.linear_model import LinearRegression

# 1. DATOS: tamaños (m²) y sus precios reales
X = [[50], [80], [100], [120], [150]]      # entrada: metros cuadrados
y = [100000, 160000, 200000, 240000, 300000]  # salida: precio real

# 2. ENTRENAR: el modelo aprende la relación tamaño→precio
modelo = LinearRegression()
modelo.fit(X, y)

# 3. PREDECIR: ¿cuánto costaría una casa de 90 m²?
prediccion = modelo.predict([[90]])
print(f"Una casa de 90 m² costaría unos {prediccion[0]:.0f} €")

"""
"""

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = [[10], [20], [30], [40], [50]]      # precio del producto
y = [102, 86, 77, 54, 43]               # unidades vendidas


modelo = LinearRegression()
modelo.fit(X, y)
print(f"Pendiente (coef_): {modelo.coef_[0]:.2f}")
print(f"Punto de partida (intercept_): {modelo.intercept_:.2f}")

precision = modelo.score(X, y)
print(f"Precisión del modelo (R²): {precision:.2f}")

precios = [25, 35, 55]
predicciones = modelo.predict([[25], [35], [55]])
#prediccion = modelo.predict([[35]])
#print(f"Con un precio de 35 €, venderia {prediccion[0]} unidades ")
#print(f"Con un precio de 25 €, vendería {predicciones[0]:.0f} unidades")
#                                                      ^^^^
#                                         :.0f = 0 decimales → 62 (redondea)
#print(f"Con un precio de 35 €, vendería {predicciones[1]:.0f} unidades")
#print(f"Con un precio de 55 €, vendería {predicciones[2]:.0f} unidades")
for precio, venta in zip(precios, predicciones):
    print(f"Con un precio de {precio} €, vendería {venta:.0f} unidades")

 """

"""


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = [[10], [15], [20], [25], [30], [35], [40], [45], [50], [55], [60], [65]]
y = [100, 94, 85, 80, 71, 65, 58, 50, 42, 38, 30, 22]

modelo = LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo.fit(X_train, y_train)              
precision = modelo.score(X_test, y_test)  
print(f"R² en prueba: {precision:.2f}")

prediccion = modelo.predict([[48]])

print(f"R² en entrenamiento: {modelo.score(X_train, y_train):.2f}")
#print(f"R² en prueba:        {modelo.score(X_test, y_test):.2f}")

print(f"Con un precio de 48 €, venderia {prediccion[0]:.0f} unidades ")

"""

"""

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Antes:  X = [[precio]]
# Ahora:  X = [[precio, publicidad]]

X = [
    [10, 100], [15, 120], [20, 110], [25, 150], [30, 130], [35, 160],
    [40, 140], [45, 180], [50, 170], [55, 200], [60, 190], [65, 210],
    [70, 220], [75, 200], [80, 230], [85, 240],
]
y = [140, 135, 130, 133, 125, 128, 112, 122, 110, 116, 103, 107, 100, 92, 90, 88]
  
modelo = LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo.fit(X_train, y_train)              
precision = modelo.score(X_test, y_test)  

print(f"Pendiente (coef_): {modelo.coef_[0]:.2f}, {modelo.coef_[1]:.2f}")

prediccion = modelo.predict([[35, 160]])   

print(f"R² en prueba: {precision:.2f}")
print(f"R² en entrenamiento: {modelo.score(X_train, y_train):.2f}")

print(f"Con un precio de 35 €, con 160 € de publicidad venderia {prediccion[0]:.0f} unidades")

"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# [edad, minutos en la web]
X = [
    [22, 2], [25, 5], [30, 3], [35, 4], [28, 7], [40, 9],
    [45, 12], [50, 15], [38, 11], [55, 20], [48, 18], [60, 14],
]
# 0 = no compró, 1 = compró
y = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

modelo = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo.fit(X_train, y_train)
prediccion = modelo.predict([[42, 13]])        # devuelve 0 o 1
exactitud = modelo.score(X_test, y_test)

print(f"Exactitud en prueba: {exactitud:.2f}")
print(f"Exactitud en entrenamiento: {modelo.score(X_train, y_train):.2f}")
# se puede mejorara la exactitud en entrenamiento igual que la otra, arriba
resultado = "SÍ comprará" if prediccion[0] == 1 else "NO comprará"
print(f"Un cliente de 42 años que pasó 13 minutos en la web: {resultado}")
#print(f"Un cliente de 42 años, que paso 13 minutos en la web comprara...{prediccion[0]:.0f}")

joblib.dump(modelo, "modelo_clientes.pkl")

