numeroInicial = int(input('Número inicial: '))
numeroFinal = int(input('Número final: '))
numeroFinal=+1
positivo=0
negativo=0
for numero in range(numeroInicial,numeroFinal):
    if numero%2==0:
     positivo=+1
    else:
       negativo+=1


       
print(f"cantidad Positivo",{positivo})
print(f"cantidad Positivo",{negativo})

