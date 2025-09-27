dic=dict(Apellido="Ávila", 
        Nombre="Armando",
        Profesión="Ing.Mecatrónico")

#Así solo nos mostrara las "keys" del diccionario 
for datos in dic:
    print(datos)

#Para que nos muestre el valor podemos usar el metodo ".items()"
for data in dic.items():
    print(data)

#Usamos [0] y [1] para mostrar las keys y su respectivo valor
for info in dic.items():
    key=info[0]
    value=info[1]
    print(f"La llave es '{key}' y su valor es '{value}'")
