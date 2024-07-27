print("! Bienvenidos a la pizzeria Bella Napoli ¡")
name = input("Regalame tu nombre para tener el gusto de atenderte .")
print(f"ok! {name} , selecciona una opcion por favor : \n 1. Pizza vegetariana \n 2. Pizza NO vegetariana ")

opcion = int(input())

if (opcion == 1):
    print("Los ingredientes de pizzas vegetarianas es el siguiente : \n - Pimiento \n - Tofu")

elif (opcion == 2):
    print("Los ingredientes de las pizzas no vegetarianas son : \n - Peperoni \n - Jamon \n - Salmon")
