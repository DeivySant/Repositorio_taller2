name = input("Regalame tu nombre")
print(f"Ok! {name} Vamos a realizar una evaluacion de la declaracion de renta segun tu sueldo ")

money = int(input("Regalame tu sueldo "))

if (money < 10000 and money > 0 ): 
    print("Tu impositivo es del 5 % ")
    imp = money * (5/100)             
    print(f"{name} tu impositivo en dinero es de {imp}") 

elif (money > 10000 and money <= 20000 ): 
    print("Tu impositivo es del 15 % ")
    imp = money * (15/100)             
    print(f"{name} tu impositivo en dinero es de {imp}")  

elif (money > 20000 and money <= 35000 ): 
    print("Tu impositivo es del 20 % ")
    imp = money * (20/100)             
    print(f"{name} tu impositivo en dinero es de {imp}")       
                                                    
elif (money > 35000 and money <= 60000 ): 
    print("Tu impositivo es del 30 % ")
    imp = money * (30/100)             
    print(f"{name} tu impositivo en dinero es de {imp}") 

elif (money > 60000 ): 
    print("Tu impositivo es del 45 % ")
    imp = money * (45/100)             
    print(f"{name} tu impositivo en dinero es de {imp}")

else:
    print("Usted agrego un valor fuera de rango")