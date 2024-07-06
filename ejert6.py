print("Vamos a evaluar dos numeros y verificaremos si el mayor es multiplo del menor ")
num1 = int(input("Dame tu primer numero : "))
num2 = int(input("Dame tu segundo numero : "))

if (num1 > num2 ):
    if ((num1 % num2) == 0):
        print(f"{num1} es multiplo de {num2}")
    else:
        print(f"{num1} no es multiplo de {num2}")

elif (num1 < num2) :
    if ((num2 % num1) == 0):
        print(f"{num2} es multiplo de {num1}")
    else:
        print(f"{num2} no es multiplo de {num1}")

else:
    print(f"{num1} es multiplo de {num2}")