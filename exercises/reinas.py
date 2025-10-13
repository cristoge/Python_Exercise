# completa el problema de las 8 reinas.
#
# Utilitzant programació genetica, crea un algorisme que trobi una possible solució del problema de les 8 reinas
#
# (https://en.wikipedia.org/wiki/Eight_queens_puzzle) generalitzada per taules d’escacs de NxN.
#
# Hi ha moltes maneres d’aproximar aquest problema. intenta establir el Gen de l'individu solució de manera adient.
#
# I utilitza un fitness score de manera que la millor solució tingui un valor 0.
#
# Utilitza els apunts de classe per tal de realitzar tots els passos d’un algoritme genetic:
# 	reproducció, mutació, selecció…
# consejos, diversity score,
# usar una seed
# consejos: aplicar comprehension list

import random

"""
Generacion de poblacion
"""


def generar_individuo(medida: int) -> list:
    nuevo_individuo = list(range(medida))
    random.shuffle(nuevo_individuo)
    return nuevo_individuo


def generar_poblacion(medida_tablero: int, medida_poblacion: int) -> list:
    poblacion = [generar_individuo(medida_tablero) for _ in range(medida_poblacion)]
    return poblacion


"""
Funcion para buscar los mejores,
en este caso quien menos collisiones tenga es mejor
"""


def fitness(individuo: list):
    colision = 0
    for i in range(len(individuo)):
        for j in range(i + 1, len(individuo)):
            if abs(i - j) == abs(individuo[i] - individuo[j]):
                colision += 1
    return colision


"""
Aqui llamamos a la funcion de fitness para seleccionar a los mejores individuos y ordenamos.
"""


def evolucion(poblacion: list):
    fitness_poblacion = [(i, fitness(i)) for i in poblacion]
    fitness_poblacion.sort(key=lambda x: x[1])
    return [x for x, _ in fitness_poblacion]


"""
coger todos los padres y de dos en dos van teniendo hijos
"""


def crossover(padre1: list, padre2: list, mutation_chance=0.1):
    punto_medio = len(padre1) // 2
    hijo1 = padre1[:punto_medio]
    hijo2 = padre2[:punto_medio]
    for i in padre2:
        if i not in hijo1:
            hijo1.append(i)
    for i in padre1:
        if i not in hijo2:
            hijo2.append(i)

    return mutacion(hijo1, mutation_chance), mutacion(hijo2, mutation_chance)


def reproducir_todos_padres(poblacion: list, padre2: list):
    random.shuffle(poblacion)
    hijos = []
    for i in range(0, len(poblacion), 2):
        hijo1, hijo2 = crossover(poblacion[i], poblacion[i + 1])
        hijos.append(hijo1)
        hijos.append(hijo2)
    return hijos


"""
Funcion de mutacion
"""


def mutacion(individuo: list, mutation_chance=0.1) -> list:
    if random.random() < mutation_chance:
        pos1 = random.randint(0, len(individuo) - 1)
        pos2 = random.randint(0, len(individuo) - 1)
        individuo[pos1], individuo[pos2] = individuo[pos2], individuo[pos1]
    return individuo


def main():
    medida_poblacion = 10
    medida_tablero = 8
    random.seed(
        12
    )  # esto es para obtener los mismos resultados aleatorios en cada ejecucion
    poblacion_inicial = generar_poblacion(medida_tablero, medida_poblacion)

    # while
    # :
    # Falta hacer el bucle principal
    # hijos = crossover(padres)
    #
    # poblacion = padres + hijos
    #
    # # ya estan ordenados ahora quitamos la tupla
    #
    # poblacion[:] = poblacion[:medida_poblacion]
    #
    # padre1, padre2 = random.sample(ordenados_en_lista, 2)
    # print(padre1, padre2)
    # crossover(padre1, padre2)


main()
