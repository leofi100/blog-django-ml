import tensorflow as tf
import numpy as np

# Datos: grados Celsius y su equivalente real en Fahrenheit
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Construimos la red: UNA sola neurona, UNA entrada
modelo = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1),
])

# Le decimos CÓMO aprender
modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1),
               loss="mean_squared_error")

# La entrenamos (500 pasadas sobre los datos)
print("Entrenando la red...")
modelo.fit(celsius, fahrenheit, epochs=1000, verbose=0)
#modelo.fit(celsius, fahrenheit, epochs=500, verbose=0)
print("¡Entrenamiento terminado!")

# Le pedimos una predicción para un valor que NO estaba en los datos
grados = 100.0
prediccion = modelo.predict(np.array([[grados]]))
print(f"{grados} °C son aproximadamente {prediccion[0][0]:.1f} °F")

# Vemos lo que la red aprendió por su cuenta
peso, sesgo = modelo.get_weights()
print(f"La red aprendió -> peso: {peso[0][0]:.2f}, sesgo: {sesgo[0]:.2f}")