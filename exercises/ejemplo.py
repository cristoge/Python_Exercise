# Límite de peso de la mochila
backpack_weight_limit = 15

# Lista de objetos
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


def backpack(weight_limit, objects):
    # 1. Filtramos para quedarnos solo con pesos/valores enteros
    clean_objects = [
        {"weight": obj["weight"], "value": obj["value"]}
        for obj in objects
        if isinstance(obj["weight"], int) and isinstance(obj["value"], int)
    ]

    # 2. Función recursiva para calcular la mejor combinación
    def calc_best(weight_limit, items):
        # Caso base: no queda peso o no hay objetos que quepan
        if weight_limit == 0 or not any(obj["weight"] <= weight_limit for obj in items):
            return 0, []

        best_value = 0
        best_combo = []

        # Probar cada objeto posible
        for i, obj in enumerate(items):
            if obj["weight"] <= weight_limit:
                # Hacer una copia de los objetos sin este
                remaining = items[:i] + items[i + 1 :]

                # Calcular mejor combinación si lo incluyo
                val, combo = calc_best(weight_limit - obj["weight"], remaining)
                val += obj["value"]

                # Guardar si es la mejor opción
                if val > best_value:
                    best_value = val
                    best_combo = [obj] + combo

        return best_value, best_combo

    # 3. Llamar a la recursión inicial
    return calc_best(weight_limit, clean_objects)


# Ejecutar la función y mostrar resultados
best_value, best_objects = backpack(backpack_weight_limit, objects)

print("El mayor valor obtenido es:", best_value)
print("La selección de objetos sería:")
for obj in best_objects:
    print(obj)
