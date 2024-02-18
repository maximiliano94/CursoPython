#Crear un programa que permita convertir una 
#cantidad de segundos en horas, minutos y segundos.

print("convertidor de segundos a  horas,minutos segundos")


tiempoSegundo=input("ingrese los segundos")
hrs=3600
min=60
tiempoSegundo=int(tiempoSegundo)

h=tiempoSegundo//hrs
tiempoSegundo=tiempoSegundo%hrs
m=tiempoSegundo//min
s=tiempoSegundo%min

print("la conversion de seg")
print("horas...........","  ",h)
print("mintos..........","  ",m)
print("segundo.........","  ",s)




