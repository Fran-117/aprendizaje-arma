#Lo primero será crear una lista
Animales=["Perro","Gato","Jaguar","Huajolote"]
personas=["Celeste", "Sofía","Armando","Homa"]
numeros=(1,2,3,4)

#Usamos la función "FOR IN", hará que psae por cada elemento de la lista
for animal in Animales:
    print(f"El animal es ahora: {animal}")

for num in numeros:
    resultado=num*15
    print(resultado)

#Para iterar dos bucles al mismo tiempo se usa "ZIP"
for num,animal in zip(numeros,Animales):
    print(f"El animal {num} es el {animal}")

#Para que nos devuelva el valor de la lista y su indice o lugar dentro de ella se usa "enumerate"
for numal in enumerate(Animales):
    print(numal)

#Usamos el "else" para hacer algo cuando termine el bucle

for person in personas:
    print(person)
else:
    print("Hemos terminado la lsita")

#TODO FUNCIONA EXACTAMENTE IGUAL PARA TUPLAS
