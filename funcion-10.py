mi_tupla = ("Space Oddity", "Life on Mars", "Heroes", "Rebel Rebel")

#Imprimir tupla
def printFormat(tupla):
    for elemento in tupla:
        print(f"- {elemento}")

#Eliminar tupla
def eliminar_item(tupla, elemento_a_eliminar):
    nueva = tuple(item for item in tupla if item != elemento_a_eliminar)
    return nueva

eliminar = "Life on Mars"
nueva_tupla = eliminar_item(mi_tupla, eliminar)

print("Tupla original:", mi_tupla)
printFormat(mi_tupla)
print("Tupla con: ", eliminar," eliminado" )
printFormat(nueva_tupla)