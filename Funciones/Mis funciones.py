#Usamos "DEF" para definir la nueva función
#def saludar()
#    print("Hola, ¿cómo has estado?")

#saludar()


#Parámetros
def saludo(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "Amor"
    elif (sexo == "hombre"):
        adjetivo= "Bro"
    else :
        adjetivo = "Transformer"
    
    print(f"Hey como has estado {nombre}, mi {adjetivo}")

saludo("Armando", "MUjer")
saludo("Homa", "Puto")


#crear funciones que devuelve valores
def crear_contraseña(num):
    caracteres_posibles ="abeudodcbcQQ@ecweAA"
    num = str(num)
    num= int(num[0])
    c1 = num - 2
    c2 = num
    c3 = num + 5
    contraseña= f"{caracteres_posibles[c1]}{caracteres_posibles[c2]}{caracteres_posibles[c3]}{num*3}"
    return contraseña

password = crear_contraseña(9495403)
#print(password) 

