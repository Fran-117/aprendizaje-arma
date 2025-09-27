#forma no optima de sumar valores
#def suma(lista)
#   numeros-sumados = 0
#   for numero in lista
#       numeros_sumados = numeros-sumados + etc
#   return numeros_sumados

#resultado = suma([5,56,63,35,4])


#USANDO PARAMETRO ARGS

def suma(*numeros):
    return sum(numeros)

resultado = suma(4,5,62,5,32)
print(resultado)
