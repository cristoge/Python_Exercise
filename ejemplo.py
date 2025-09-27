import itertools
import math


bs_data = [
    {"x": 1, "y": 1},
    {"x": 3, "y": 9},
    {"x": 9, "y": 4},
    {"x": 1, "y": 1},
    {"x": 1, "y": 5},
    {"x": 5, "y": 2},
    {"x": 4, "y": 10},
    {"x": 8, "y": 8},
]


# Función para calcular la distancia entre dos puntos
def calculate_distance(p1, p2):
    return math.dist([p1["x"], p1["y"]], [p2["x"], p2["y"]])


# Generar todas las permutaciones posibles de los puntos
permutations = itertools.permutations(bs_data)

# Inicializar variables para la mejor ruta y la distancia mínima
min_distance = float("inf")
best_route = None

# Evaluar cada permutación
for perm in permutations:
    # Calcular la distancia total de la ruta
    total_distance = 0
    for i in range(len(perm) - 1):
        total_distance += calculate_distance(perm[i], perm[i + 1])
    # Añadir la distancia de vuelta al punto de inicio
    total_distance += calculate_distance(perm[-1], perm[0])

    # Actualizar la mejor ruta si se encuentra una más corta
    if total_distance < min_distance:
        min_distance = total_distance
        best_route = perm

# Mostrar la mejor ruta y la distancia mínima
print("Mejor ruta:", best_route)
print("Distancia mínima:", min_distance)
