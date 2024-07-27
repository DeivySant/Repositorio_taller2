añoactual = int(input("Por favor ingresa el año actual : "))
print("Vamos a calcular la diferencia entre el año actual y uno que tu me entregues ")
año = int(input("Dame un año : "))

if (año < añoactual ):
    dif = añoactual - año
    print(f"Desde ese año han pasado { dif} años")

elif (año > añoactual ) :
    dif = año - añoactual
    print(f"Para llegar a tu año faltan { dif} años")

else:
    print("Tu año es el actual")
