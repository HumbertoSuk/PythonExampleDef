mi_tupla = ("Space Oddity", "Life on Mars", "Heroes", "Rebel Rebel")

def revertir_tupla(tupla):
    nueva_tupla = tuple(reversed(tupla))
    return nueva_tupla

#Imprimir tupla
def printFormat(tupla):
    for elemento in tupla:
        print(f"- {elemento}")


tupla_revertida = revertir_tupla(mi_tupla)

print("Tupla original:")
printFormat(mi_tupla)
print("\n")
print("Tupla revertida:")
printFormat(tupla_revertida)
