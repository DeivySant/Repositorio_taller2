print("Vamos a comparar 3 numero y a verificar cuantos son iguales")
num1 = int(input("Dame tu primer numero : "))
num2 = int(input("Dame tu segundo numero : "))
num3 = int(input("Dame tu tercer numero : "))

if (num1 == num2 and num2 == num3):
    print("Los tres numeros son iguales")
elif (num1 == num2 or num2 == num3 or num1 == num3 ):
    print("Hay dos numeros que son iguales")  
else:
    print("Todos los numeros son distintos :)")