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
    # generando la poblacion mediante la comprension de listas
    poblacion = [generar_individuo(medida_tablero) for _ in range(medida_poblacion)]
    return poblacion


"""
Funcion para buscar los mejores,
en este caso quien menos collisiones tenga es mejor
"""


def fitness(individuo: list):
    """
    En este caso calculamos las colisiones que haya,
    si una reuna esta en la misma diagonal se añade una colision a la lista
    Al final devuelve la cantidad de colisiones que haya
    """
    colision = 0
    for i in range(len(individuo)):
        for j in range(i + 1, len(individuo)):
            if abs(i - j) == abs(individuo[i] - individuo[j]):
                colision += 1
    return colision


def evolucion(poblacion: list):
    """
    Aqui clasificamos a la poblacion por el numero de colisiones que tenga
    y devolvemos la poblacion ordenada
    """
    fitness_poblacion = [(i, fitness(i)) for i in poblacion]
    fitness_poblacion.sort(key=lambda x: x[1])
    return [x for x, _ in fitness_poblacion]


def crossover(padre1: list, padre2: list, mutation_chance=0.1):
    """
    Esta es la funcion para mezclar padres, en este caso
    pasamos por parametro los 2 padres y el chance de mutacion para poder
    tener individuos mas variados, en este caso los hijos siempre seran
    la mitad de cada padre
    """
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


def reproducir_todos_padres(poblacion: list):
    """
    Aqui llamamos a la funcion que definimos antes para mezclar,
    en este caso es para reproducir todos los padres, primero los mezcla con el shuffle
    y por ultimo llama al crossover y devuelve una lista de hijos nueva
    """
    random.shuffle(poblacion)
    hijos = []
    for i in range(0, len(poblacion) - 1, 2):
        # -1 para que no se me vaya de posicion
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
    poblacion = generar_poblacion(medida_tablero, medida_poblacion)
    """
    creamos un total de generaciones maximas para que no pete 
    en este caso lo fijamos en 100k
    """
    generaciones_maximas = 100000
    for i in range(generaciones_maximas):
        poblacion = evolucion(
            poblacion
        )  # aqui hacemos que la poblacion se ordene por los mejores que tienen menos colisiones
        mejor = poblacion[
            0
        ]  # en este caso al estar ordenado la posicion 0 es la que tiene menos colisiones
        mejor_fitness = fitness(
            mejor
        )  # aqui volvemos a llamar a la funcion de fitness para que nos de las colisones
        if (
            mejor_fitness == 0
        ):  # y si da la casualidad de que el fitness es 0 significa que encontramos nuestro resultado
            print(
                f"solucion encontrada en la generacion {i} y {mejor}"
            )  # imprimimos la solucion
            break  # rompemos el bucle
        padres = poblacion[
            : medida_poblacion // 2
        ]  ## aqui divido mi poblacion a la mitad para ir variando la poblacion en este caso en la funcion reoordena a los mejores para la variedad
        hijos = reproducir_todos_padres(
            padres
        )  # ahora mezclo a todos los padres para que me den individuos nuevos
        poblacion = padres + hijos  # y los mezclo aqui para volver a empezar el bucle


main()
