Dic={
    "nombre":"Armando",
    "sueldo":"10550",
    "vehículo":"Camaro"
}

res=Dic.keys()
print("Método 'KEYS':", res)

res1=Dic.get("sueldo")
print("Método 'GET': ",res1)

res2=Dic.items()
print(res2)

res3=Dic.pop("nombre")
print("Eliminando con 'POP': ",Dic)

Dic.clear()
print("Eliminando todos los elementos con 'CLEAR': ",Dic)
