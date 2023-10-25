# Conjuntos de canciones de David Bowie y Pink Floyd
canciones1 = {"Space Oddity", "Life on Mars", "Heroes"}
canciones2 = {"Comfortably Numb", "Wish You Were Here", "Space Oddity"}

def diferencia_de_conjuntos(conjunto1, conjunto2):
    resultado = conjunto1 - conjunto2
    return resultado

# Función para imprimir un conjunto con formato
def printFormat(conjunto, nombre):
    print(f"Conjunto de canciones de {nombre}:")
    for cancion in conjunto:
        print(f"- {cancion}")
        


# Llamamos a la función para obtener la diferencia
diferencia = diferencia_de_conjuntos(canciones1, canciones2)

# Imprimimos la diferencia
print("Diferencia entre canciones ")
printFormat(diferencia, "Diferencia")
