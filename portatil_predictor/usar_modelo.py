import joblib

# Cargamos el modelo ya entrenado (sin datos, sin fit)
modelo = joblib.load("modelo_clientes.pkl")


def predecir(edad, minutos):
    """Devuelve un texto legible según la predicción del modelo."""
    prediccion = modelo.predict([[edad, minutos]])
    return "SÍ comprará" if prediccion[0] == 1 else "NO comprará"


# Ejemplos de uso
print(f"Cliente de 42 años, 13 min: {predecir(42, 13)}")
print(f"Cliente de 56 años, 20 min: {predecir(56, 20)}")
print(f"Cliente de 22 años,  5 min: {predecir(22, 5)}")
print(f"Cliente de 65 años, 10 min: {predecir(65, 10)}")