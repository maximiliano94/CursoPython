#Enunciado: dado el valor de venta de productos, 
# hallar el IGV (18%) y el precio de venta.

print("--REALIZA UNA VENTA--")
VV=float(input("ingrese el valor de la venta"))
#operacioenes
igv=VV*0.18
pv=VV+igv

#salida
print("="*25)
print("--FACTURA VENTA--")
print("="*25)
print("valor del producto es ..",VV)
print("el IGV del producto es..",igv)
print("el PV del producto es..",pv)
print("="*25)
