import random
bandera=True
Jugador1=0
Jugador2=0
def sumar_tiradas(contador):
    total=0
    for i in range(contador):
        dado1= random.randint(1,6)
        print("tirada",i+1,":",dado1)
        total += dado1
    return total
while (bandera):
    contador= int(input("Ingrese la cantidad de veces que tirara los dados"))
    Jugador1 += sumar_tiradas(contador)
    print("Jugador1 hizo",Jugador1, "puntos")
    Jugador2 += sumar_tiradas(contador)
    print("Jugador2 hizo",Jugador2, "puntos")

    if Jugador1 > 100 and Jugador1 > Jugador2:
        print("Gana Jugador1")
        bandera=False
    elif Jugador2 >100 and Jugador2 > Jugador1:
        print("Gana Jugador2")
        bandera=False
    elif Jugador1 > 100 and Jugador2 >100 and Jugador1==Jugador2:
        print("Empate")
        bandera=False
