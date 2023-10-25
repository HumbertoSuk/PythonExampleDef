# Conjuntos de canciones de David Bowie y Pink Floyd
canciones_david_bowie = {"Space Oddity", "Life on Mars", "Heroes"}
canciones_pink_floyd = {"Comfortably Numb", "Wish You Were Here", "Time"}


def combinar_conjuntos(conjunto1, conjunto2):
    resultado = conjunto1 | conjunto2
    return resultado

# Función para imprimir un conjunto con formato
def printFormat(conjunto, nombre):
    print(f"Conjunto de canciones de {nombre}:")
    for cancion in conjunto:
        print(f"- {cancion}")
        


# Llamamos a la función para combinar los conjuntos
conjunto_combinado = combinar_conjuntos(canciones_david_bowie, canciones_pink_floyd)

printFormat(canciones_david_bowie, "David Bowie")
print("\n")
printFormat(canciones_pink_floyd, "Pink Floyd")
print("\n \n")
# Imprimir el conjunto y el resultado
printFormat(conjunto_combinado, "David Bowie y Pink Floyd")
