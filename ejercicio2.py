# Define una función "bus_stops" que:
#
# *   Acepte una lista de diccionarios con una serie de coordenadas ("x" e "y") con números enteros
# *   Verifique que todo son números enteros (en caso de no ser así que elimine las coordenadas que no lo cumplan)
# *   Calcule el orden que optimice la distancia mínima a recorrer si tenemos que pasar por todos los puntos.
# *   Muestre por pantalla la distancia mínima obtenida y devuelva un diccionario con el orden correcto de los puntos.
#
# Llama a la función con el diccionario "bs_data" e imprime su resultado por pantalla:
import math
from types import coroutine

bs_data = [
    {"x": 1, "y": 1},
    {"x": "some", "y": 12},
    {"x": 3, "y": 9},
    {"x": 9, "y": 4},
    {"x": 1, "y": 1},
    {"x": 1, "y": 5},
    {"x": 5, "y": 2},
    {"x": 4, "y": 10},
    {"x": 8, "y": 8},
    {"x": -3, "y": 2.3},
]


def only_ints(data: list):
    verify_data = list(
        filter(
            lambda coords: isinstance(coords["x"], int)
            and isinstance(coords["y"], int),
            data,
        )
    )
    return verify_data


def calculate_distance(coords1: dict, coords2: dict):
    distance = math.dist([coords1["x"], coords1["y"]], [coords2["x"], coords2["y"]])
    pass


def best_road(paradas: list):
    # i+1;
    ejemplo = math.dist(
        [paradas[0]["x"], paradas[0]["y"]], [paradas[1]["x"], paradas[1]["y"]]
    )
    print(ejemplo)


data = only_ints(bs_data)

print(best_road(data))
