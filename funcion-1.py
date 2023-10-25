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

# Función para agregar una canción al diccionario
def agregar_cancion(diccionario, clave, valor):
    diccionario[clave] = valor
    return diccionario

# Función para imprimir el diccionario con formato
def print_dict_with_length_format(diccionario):
    max_key_length = max(len(key) for key in diccionario)
    max_value_length = max(len(str(value)) for value in diccionario.values())
    for key, value in diccionario.items():
        print(f"{key.ljust(max_key_length)}: {str(value).ljust(max_value_length)}")

# Solicitar la clave y datos al usuario para la nueva canción
nueva_clave = input("Ingrese la clave para la nueva canción: ")
nuevo_titulo = input("Ingrese el título de la nueva canción: ")
nuevo_artista = input("Ingrese el nombre del artista: ")
nuevo_año = int(input("Ingrese el año de lanzamiento: "))

# Crear un diccionario para la nueva canción
nueva_canción = {
    "titulo": nuevo_titulo,
    "artista": nuevo_artista,
    "año": nuevo_año
}

# Agregar la nueva canción al diccionario
canciones = agregar_cancion(canciones, nueva_clave, nueva_canción)

# Imprimir el diccionario con formato
print_dict_with_length_format(canciones)
