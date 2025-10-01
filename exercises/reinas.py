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

import random

"""
Generacion de poblacion
"""


def generar_individuo(medida: int) -> list:
    nuevo_individuo = list(range(medida))
    random.shuffle(nuevo_individuo)
    return nuevo_individuo


def generar_poblacion(medida_tablero: int, medida_poblacion: int) -> list:
    poblacion = []
    for _ in range(medida_poblacion):
        individuo = generar_individuo(medida_tablero)
        poblacion.append(individuo)
    return poblacion


poblacion = generar_poblacion(8, 4)
print(poblacion)

"""
Funcion para buscar los mejores
"""


def fitness(poblacion: list):
    pass


"""
Aqui llamamos a la funcion de fitness para seleccionar a los mejores individuos y ordenamos.
"""


def seleccion(poblacion: list) -> list:
    pass


"""
coger todos los padres y de dos en dos van teniendo hijos
"""


def crosover(poblacion: list) -> list:
    pass


"""
Funcion para reproducir_dos_padres
"""


def reproducir_dos_padres(padre1: list, padre2: list):
    pass
