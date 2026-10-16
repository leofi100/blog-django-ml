

import joblib

modelo = joblib.load("modelo_clientes.pkl")

prediccion1 = modelo.predict([[42, 13]])
prediccion2 = modelo.predict([[56, 20]])
prediccion3 = modelo.predict([[22, 5]])

#print(prediccion1)
#print(prediccion2)
#print(prediccion3)

resultado1 = "SÍ comprará" if prediccion1[0] == 1 else "NO comprará"
print(f"Un cliente de 42 años que pasó 13 minutos en la web: {resultado1}")

resultado2 = "SÍ comprará" if prediccion2[0] == 1 else "NO comprará"
print(f"Un cliente de 56 años que pasó 20 minutos en la web: {resultado2}")

resultado3 = "SÍ comprará" if prediccion3[0] == 1 else "NO comprará"
print(f"Un cliente de 22 años que pasó 5 minutos en la web: {resultado3}")

