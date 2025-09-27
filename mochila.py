# Define una función "backpack" que:

# *   Acepte dos parámetros de entrada: un número entero que especificará el peso que es capaz de soportar la mochila y una lista de pares de elementos (definidos en diccionarios) que contenga el peso y el valor de cada objeto
# *   Verifique que todos los parámetros son números enteros (los que no sean así serán eliminados)
# *   Calcule la mejor combinación de objetos que permita la máxima ganancia limitandose al peso que soporta la mochila
# *   Muestre por pantalla el valor obtenido
# *   Devuelva una lista con los elementos escogidos

# Llama a la función con los parámetros "backpack_weight_limit" y "objects" e imprime su resultado por pantalla:
backpack_weight_limit = 15
objects = [
    {"weight": 1, "value": 1},
    {"weight": 6, "value": 4},
    {"weight": 4, "value": 7},
    {"weight": 5, "value": 6},
    {"weight": 1, "value": 3},
    {"weight": 6, "value": 8},
    {"weight": 3, "value": 6},
    {"weight": 10, "value": 11},
    {"weight": 4, "value": 4},
    {"weight": 7, "value": 3},
]

