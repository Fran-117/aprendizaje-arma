nombre="Celeste"
lista=["HOLA", "Armando", 45, False,{nombre}]
print(lista)

list=["Mango","Manzana","Sandía"]
print(list[0])

tuple=("Mango","Manzana","Sandía") 
    #tuple="ADIOS".   La tupla no se puede modificar post definirla
print(tuple[1])

conjunto={"Azul","Naranja","Morado","Verde"} 
    #conjunto={"Azul","Naranja","Morado","Verde", "Azul"}. No podemos repeitr valores. como Azul
    #conjunto="Hola". Se puede redifinir la variable
print(conjunto)
    #print(conjunto[2]). NO se puede mostrar un solo elemento
    
dict={ #Es key:value y se separa con coma ,
    'Apellido':"Ávila",
    'Color_fav': "Azul",
    'Nivel_estudios':"Preparatoria",
}
print(dict["Apellido"]) #Muestra el vealor del elemento asignado
