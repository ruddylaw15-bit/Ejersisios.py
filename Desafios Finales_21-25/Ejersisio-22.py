#Calificador de notas
#Convertir una nota de 0-100 en letras (A, B, C, D o F)
nt=float(input("Ingres una nota: "))
if nt>= 90:
    print("Nota A")
elif nt>= 80:
    print("Nota B")
elif nt>= 70:
    print("Nota C")
elif nt>= 60:
    print("Nota D")
elif nt>= 1:
    print("Nota F")
else:
    print("No es valido nota 0")                