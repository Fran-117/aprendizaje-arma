Frutas=["Manzana", "Platano","Pera","Sandía","Maracuyá"]
Cadena="Hola mundo"
numeros=[1,3,49,10]

#Usamos el "if" y el "continue" para saltar un elemento de la lista
for comer in Frutas:
    if comer=="Pera":
        continue
    print(f"Tengo hambre y comeré {comer}")

#Usamos igualmente "if" y "break" para parar el bucle
for comida in Frutas:
    if comida=="Pera":
        break
    print(f"Comeré {comida} y a lo mejor uno más")
print("Ya me llené")

#Recorremos una cadena de texto o string
for letra in Cadena:
    print(letra)

#Una sola línea de código para cosas simples
nuemrosx2=[x*3 for x in numeros]
print(nuemrosx2)
