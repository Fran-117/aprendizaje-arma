Saludo="Hola ¿cómo están mundo?"
respuesta="Muy biennnnn, Te esperabamos"

#print(dir(Saludo)) #Muestra todo lo que se puede hacer con un dato, descomentar si quieres


dato1= "SOFIA".lower()
dato= Saludo.upper()
capitalize=respuesta.capitalize()
find=respuesta.find("Te")
#index=Saludo.index(5)
insumeric=respuesta.isnumeric()
isalpha= "Hola".isalpha()
count=respuesta.count("n")
len=len(respuesta)
endswith=respuesta.endswith("s")
starswith=respuesta.startswith("n")
replace=Saludo.replace("¿cómo están mundo?", "CTM")
split= "Hola,tengo,hambre,y,mucha".split(",")

print(dato)
print(dato1)
print(capitalize)
print(find)
#print(index) #Lanza error y para el programa, descomentar para ver
print(insumeric)
print(isalpha)
print(count)
print(len)
print(endswith)
print(starswith)
print(replace)
print(split)
