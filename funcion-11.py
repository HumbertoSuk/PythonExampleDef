Bowie1 = ("Space Oddity", "Life on Mars", "Heroes")
Bowie2 = ("Rebel Rebel", "Starman", "Changes")

def concatenar_tuplas(tupla1, tupla2):
    nueva_tupla = tupla1 + tupla2
    return nueva_tupla

#Imprimir tupla
def printFormat(tupla):
    for elemento in tupla:
        print(f"- {elemento}")


tupla_concatenada = concatenar_tuplas(Bowie1, Bowie2)

print("Tupla 1:")
printFormat(Bowie1)
print("\n")
print("Tupla 2:")
printFormat(Bowie2)
print("\n")
print("Tupla concatenada:")
printFormat(tupla_concatenada)
