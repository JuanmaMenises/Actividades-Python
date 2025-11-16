for i in range(5):
 bandera=True
 vidas= int(input("Ingrese el numero de vidas que desee"))
 while(bandera):
    if vidas>=5:
        print("haz seleccionado la dificultad facil")
        bandera=False
    elif vidas>=3:
        print("haz seleccionado la dificultad media")
        bandera=False
    else:
        print("haz seleccionado la dificultad dificil")
        bandera=False