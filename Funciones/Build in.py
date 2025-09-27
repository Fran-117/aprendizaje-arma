#Son las funciones que ya fueron creadas e incorporadas en Phyton
numeros=[2,3,10,54,32,29,49]
print("El numero mas alto es:",max(numeros))
print("El numero mas bajo es:",min(numeros))

#Podemos decidir como redondear con decimales si usamos "ROUND"
numero=34.638204
print("El resultado es:",round(numero,2))

#"BOOL" Nos devuelve "falso" sí le damos-> 0, vacio, False, none/ Devuelve "True"-> num/=/0 o string
resultado=bool({})
res=bool(0)
res1=bool(-1)
res2=bool("HOLA")
print(resultado)
print(res)
print(res1)
print(res2)

#"ALL" nos devuelve "true" si todos los elementos son verdaderos
list=[236,True,[3740,12,9,-1]]
lista=[349, 45, 0]
print("Respuesta de 'ALL':",all(list))
print("Respuesta de 'ALL':",all(lista))

