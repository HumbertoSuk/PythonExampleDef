# Crear conjuntos de canciones de David Bowie y Pink Floyd
canciones_david_bowie = {"Space Oddity", "Life on Mars", "Heroes"}
canciones_pink_floyd = {"Comfortably Numb", "Wish You Were Here", "Time"}

# Función para imprimir un conjunto con formato
def printFormat(conjunto, nombre):
    print(f"Conjunto de canciones de {nombre}:")
    for cancion in conjunto:
        print(f"- {cancion}")


# Función para agregar elemento
def agregar_elemento(conjunto, elemento):
    if elemento not in conjunto:
        conjunto.add(elemento)
        return True
    else:
        return False

# Intentar agregar canciones a los conjuntos
resultado_david_bowie = agregar_elemento(canciones_david_bowie, "Ashes to Ashes")
resultado_pink_floyd = agregar_elemento(canciones_pink_floyd, "Wish You Were Here")  # Intentando agregar una canción que ya existe

# Imprimir los conjuntos con formato y los resultados
printFormat(canciones_david_bowie, "David Bowie")
printFormat(canciones_pink_floyd, "Pink Floyd")
print("¿Se pudo agregar 'Ashes to Ashes' a las canciones de David Bowie?", resultado_david_bowie)
print("¿Se pudo agregar 'Wish You Were Here' a las canciones de Pink Floyd?", resultado_pink_floyd)
