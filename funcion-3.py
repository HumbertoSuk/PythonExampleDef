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
# Función para imprimir el diccionario con formato
def print_dict_with_length_format(diccionario):
    max_key_length = max(len(key) for key in diccionario)
    max_value_length = max(len(str(value)) for value in diccionario.values())
    for key, value in diccionario.items():
        print(f"{key.ljust(max_key_length)}: {str(value).ljust(max_value_length)}")
        
        


def modificar_valor(diccionario, clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return True
    else:
        return False


# Modificar el valor de una canción
resultado = modificar_valor(canciones, "cancion9", {"titulo": "Life on Mars", "artista": "David Bowie", "año": 1971})

# Imprimir el diccionario con formato
print_dict_with_length_format(canciones)

# Imprimir si se pudo modificar o no
print("¿Se pudo modificar? ", resultado)
