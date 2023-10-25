#Las tuplas son inmutables 

def agregar_elemento_a_tupla(tupla, elemento):
    nueva_tupla = tupla + (elemento,)
    return nueva_tupla

#Imprimir tupla
def printFormat(tupla):
    for elemento in tupla:
        print(f"- {elemento}")


mi_tupla = ("Space Oddity", "Life on Mars", "Heroes")
nueva = agregar_elemento_a_tupla(mi_tupla, "Rebel Rebel")

print("Tupla Original:")
printFormat(mi_tupla)
print("Nueva tupla con el elemento agregado:")
printFormat(nueva)
