print("Vamos a calcular la diferencia entre el año actual y uno que tu me entregues ")
año = int(input("Dame un año : "))

if (año < 2024 ):
    dif = 2024 - año
    print(f"Desde ese año han pasado { dif} años")

elif (año > 2024 ) :
    dif = año - 2024
    print(f"Para llegar a tu año faltan { dif} años")

else:
    print("Tu año es el actual")
