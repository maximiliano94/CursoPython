numeroInicial=int(input("ingrese el numero incial.."))
numeroFinal=int(input("ingrese el numero final.."))
i = 0
contador = 0


i = numeroInicial + 1
while i < numeroFinal:
    contador += 1
    i += 1
    
print(f'CANTIDAD: {contador}')