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
        


# Función para eliminar un elemento de un diccionario
def eliminar_cancion(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
    return diccionario

# Solicitar al usuario la clave a eliminar
eliminar = input("Ingrese la clave de la canción que desea eliminar: ")

# Eliminar la canción del diccionario
canciones = eliminar_cancion(canciones, eliminar)

# Imprimir el diccionario con formato
print_dict_with_length_format(canciones)
