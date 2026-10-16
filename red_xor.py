import tensorflow as tf
import numpy as np

# Problema XOR: la respuesta es 1 cuando las entradas son DIFERENTES
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 1, 1, 0], dtype=float)

# Red con una CAPA OCULTA de 8 neuronas
modelo = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    
    tf.keras.layers.Dense(16, activation="relu"),
    #tf.keras.layers.Dense(8, activation="relu"),     # capa oculta
    tf.keras.layers.Dense(1, activation="sigmoid"),  # capa de salida
])

modelo.compile(optimizer="adam",
               loss="binary_crossentropy",
               metrics=["accuracy"])

print("Entrenando...")

modelo.fit(X, y, epochs=2000, verbose=0)
#modelo.fit(X, y, epochs=1000, verbose=0)
print("¡Listo!\n")

# Probamos las 4 combinaciones
for entrada in X:
    pred = modelo.predict(np.array([entrada]), verbose=0)[0][0]
    print(f"{entrada} -> {pred:.2f}  (respuesta: {round(pred)})")