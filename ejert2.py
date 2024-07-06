print("Vamos a realizar un calculo de multiplicacion y verificar si su resultado es par o impar")
num1 = int(input("Dame tu primer numero : "))
num2 = int(input("Dame tu segundo numero : "))

resm = num1 * num2

if (resm % 2 > 0):
    print(f"el resultado es {resm} por lo tanto es impar")
elif (resm % 2 == 0):
    print(f"El resultado es {resm} por lo tanto es par ")