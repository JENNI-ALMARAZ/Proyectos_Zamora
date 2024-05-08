# Hill_Clim_Ite.py

import math
import random

def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# Calcular la distancia correcta por una ruta
def evalua_ruta(ruta, coord):
    total = 0
    for i in range(0, len(ruta)-1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total = total + distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[-1]
    ciudad2 = ruta[0]
    total = total + distancia(coord[ciudad1], coord[ciudad2])
    return total

def i_hill_climbing(coord):  # Añadimos el argumento coord
    # Crear ruta inicial aleatoria
    ruta = list(coord.keys())
    mejor_ruta = ruta[:]
    max_iteraciones = 10
    
    while max_iteraciones > 0:
        mejora = False
        # Generar nueva ruta aleatoria
        random.shuffle(ruta)
        for i in range(len(ruta)):
            for j in range(i+1, len(ruta)):
                ruta_tmp = ruta[:]
                ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                dist = evalua_ruta(ruta_tmp, coord)  # Pasamos coord como argumento
                if dist < evalua_ruta(ruta, coord):  # Pasamos coord como argumento
                    # Se encontró un vecino que mejora el resultado
                    ruta = ruta_tmp[:]
                    mejora = True
        max_iteraciones -= 1

    return ruta
