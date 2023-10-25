# Conjunto de canciones de David Bowie
canciones_david_bowie = {"Space Oddity", "Life on Mars", "Heroes","Starman"}

def eliminar_elemento(conjunto, elemento):
    if elemento in conjunto:
        conjunto.remove(elemento)
        return True
    else:
        return False

# Función para imprimir un conjunto con formato
def printFormat(conjunto, nombre):
    print(f"Conjunto de canciones de {nombre}:")
    for cancion in conjunto:
        print(f"- {cancion}")
        


# Intentar eliminar una canción del conjunto
resultado = eliminar_elemento(canciones_david_bowie, "Space Oddity")

# Intentar eliminar una canción del conjunto
resultado2 = eliminar_elemento(canciones_david_bowie, "Let's dance")

# Imprimir el conjunto y el resultado
printFormat(canciones_david_bowie, "David Bowie")
print("¿Se pudo eliminar 'Space Oddity' del conjunto de canciones de David Bowie?", resultado)
print("¿Se pudo eliminar 'Let's dance' del conjunto de canciones de David Bowie?", resultado2)