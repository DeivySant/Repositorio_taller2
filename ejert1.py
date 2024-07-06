print("Vamos a evaluar unas edades y la vamos a clasificar")
edad = int(input("Dame tu edad por favor : "))

if ( edad >= 0 and edad <=5):
    print("Tu edad esta en primera infancia :) ")

elif(edad >= 6 and edad <= 11 ):
    print("Tu edad esta en infancia :)")

elif(edad >= 12 and edad <= 14 ):
    print("Tu edad esta en adolecencia :)")

elif(edad >= 15 and edad <= 26 ):
    print("Tu edad esta en juventud :)")

elif(edad >= 27 and edad <= 59 ):
    print("Tu edad esta en adultez :)")

elif(edad >= 60 and edad <= 100):
    print("tu edad es la de una persona mayor")