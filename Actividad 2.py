bandera=True
import random
total=0
contador= int(input("ingrese la cantidad de tiradas"))
while(bandera):
    if contador>0:
        dado1= random.randint(1,6)
        dado2= random.randint(1,6)
        suma= dado1+dado2
        print("la tirada dio",suma)
        total += suma
        contador=contador-1
    else:
     print("la suma total de las tiradas es",total)
     bandera=False




