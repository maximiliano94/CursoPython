# dado un numero devuelve numeros en orden asendente

numero1=int(input("ingrese un  numero 1" "   "))
numero2=int(input("ingrese un  numero 2" " "))
numero3=int(input("ingrese un  numero 3" " " ))


if numero1 > numero2 and numero2 > numero3:
    print("",numero1," -",numero2,"-",numero3)
elif numero2 > numero1 and numero1 > numero3:
     print("",numero2," -",numero1,"-",numero3)
elif numero3 > numero1 and numero1 > numero2:
     print("",numero3," -",numero2,"-",numero1)
elif numero1 > numero3 and numero3 > numero2:
     print("",numero1," -",numero3,"-",numero2)
else:
      print("se ingresaron mumeros iguales")
   
