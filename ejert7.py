print("Vamos a comparar 3 numero y a verificar cuantos son iguales")
num1 = int(input("Dame tu primer numero : "))
num2 = int(input("Dame tu segundo numero : "))
num3 = int(input("Dame tu tercer numero : "))

if (num1 == num2):
    if(num1 == num3):
        print("Los tres numeros son iguales")
    else:
        print("Solo hay dos numeros iguales")
elif (num1 == num3):
    print("Solo hay 2 numeros iguales")
else:
    print("Todos los numeros son distintos :)")