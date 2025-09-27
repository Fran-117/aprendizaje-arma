lista= ["Hola", "Mango", "Cilantro", "Cebolla", "Cilantro", 27]
resultado= len(lista)

print(len(lista))

lista1=["Armando","Celeste","Valentina","Homa","Litzy"]
res=lista1.append("JAJAJAJ")
print(lista1)

lista2=["telefono","computadora","television","reloj"]
res1=lista2.insert(2,456)
print(lista2)

lista3=["México","Eu","Canada"]
res2=lista3.extend([2027,"27 de agosto"])
print(lista3)

lista4=["Tangamandapio","Recorcholis","Birolo"]
res3=lista4.pop(0) #Si ponemos "-1" como indice, eliminamos el último elemento de la lista y posterior
print(lista4)

lista5=["DORITOS","RUFLES","SABRITAS","CHETOS"]
res4=lista5.remove("DORITOS")
print(lista5)

lista6=["CTM","LA TUYA","PUTA","PUTO"]
lista6.clear()
print(lista6)

lista7=[True,12,False,7,8,10,3,1, False, True,5]
res5=lista7.sort() #Si agregamos al () "reverse=True", hara que los elementos vayan en descendente
print(lista7)

lista8=[1,2,3,4,5,6,7,8,9,10]
res6=lista8.reverse()
print(lista8)
