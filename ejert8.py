
print("Vamos a calcular el area de un triangulo o de un circulo \n responde con 'C' si es de un circulo o 'T' si es triangulo")
opcion = input("Cual es tu eleccion : ").lower()

if (opcion == "c" ):
    print("Vamos a calcular el area de un circulo \ Para comenzar regalame el radio del circulo")
    rad = int(input("Radio : "))
    area = 3.141592*rad**2
    print(f"El area de tu circulo es de : {area}")

elif (opcion == "t"):
    print("Vamos a calcular el area de un triangulo \n Regalame los soguientes datos :")
    base = int(input("Dame la base de tu triangulo : "))
    altura = int(input("Dame la altura de tu triangulo : "))
    area = (base * altura)/2
    print(f"El area de tu triangulo es de {area}")

else:
    print("La opcion que ingresaste no existe :( ")
    