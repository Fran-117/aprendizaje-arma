frase=input("Escribe una frase y te digo cuanto tardas en decirla: ")
palabras_sep=frase.split()
Total_palabras=len(palabras_sep)

print(f"Dijiste {Total_palabras} palabras y tardarias en decirlo {Total_palabras/2}")
print(f"Dalto tardaría {Total_palabras/2*1.3}")
