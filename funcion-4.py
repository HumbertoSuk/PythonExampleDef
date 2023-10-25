# Diccionario de música
canciones = {
    "cancion1": {
        "titulo": "Bohemian Rhapsody",
        "artista": "Queen",
        "año": 1975
    },
    "cancion2": {
        "titulo": "Space Oddity",
        "artista": "David Bowie",
        "año": 1971
    },
    "cancion3": {
        "titulo": "Five Years",
        "artista": "David Bowie",
        "año": 1976
    },
    "cancion4": {
        "titulo": "Yesterday",
        "artista": "The Beatles",
        "año": 1965
    }
}

# Diccionario de música 2
canciones2 = {
    "cancion5": {
        "titulo": "Killer Queen",
        "artista": "Queen",
        "año": 1975
    },
    "cancion6": {
        "titulo": "the man who sold the world",
        "artista": "David Bowie",
        "año": 1971
    }
}

# Función para imprimir el diccionario con formato
def print_dict_with_length_format(diccionario):
    max_key_length = max(len(key) for key in diccionario)
    max_value_length = max(len(str(value)) for value in diccionario.values())
    for key, value in diccionario.items():
        print(f"{key.ljust(max_key_length)}: {str(value).ljust(max_value_length)}")
        


def combinar_diccionarios(diccionario1, diccionario2):
    resultado = diccionario1.copy()  # Copiamos el primer diccionario para no modificarlo directamente
    resultado.update(diccionario2)  # Agregamos los elementos del segundo diccionario al primero
    return resultado


# Llamamos a la función para combinar los diccionarios
diccionario_combinado = combinar_diccionarios(canciones, canciones2)

# Imprimir el diccionario con formato
print_dict_with_length_format(diccionario_combinado)
