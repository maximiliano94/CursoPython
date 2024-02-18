contador=0
while contador<10:
    contador+=1
    print(contador)
    if contador==5:
        #print("pausa el mientras")
        #break
        print("salta de laiteracion")
        continue
    print("Despues del continue")
else:
    print("fin del mientras") 
