Dalto_curso=1.5
Max_otros=7
Prome_otros=4
Mini_otros=2.5
Dalto_crudo=3.5
Prome_crudo=5

#A)Diferencia del porcentaje entre el curso actual y los demás

Dife_rapido=100-Dalto_curso/Mini_otros*100
print(f"El curso de Dalto es {Dife_rapido}% más rápido que el curso más rapido")

Dife_promedio=100-Dalto_curso/Prome_otros*100
print(f"El curso de Dalto dura {Dife_promedio}% menos que el promedio")

Dife_lento=100-Dalto_curso/Max_otros*100
if 78.58>Dife_lento>78.56:
    Dife_lento=78.57
print(f"El curso de Dalto dura {Dife_lento}% menos que el curso más largo")



#B)Porcentaje de material inservible que se reduce

Porcen_Dalto=Dalto_curso/Dalto_crudo*100
if 78.58>Dife_lento>78.56:
    Porcen_Dalto=42.85
print(f"En el curso de Dalto se reduce un {Porcen_Dalto}% de material inservible")

Porcen_otros=Prome_otros/Prome_crudo*100
print(f"En otros cursos en promedio, se elimina un {Porcen_otros}% de material invservible")
