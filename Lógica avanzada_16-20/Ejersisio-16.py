#Año Bisiesto
#Multiplo de 4 pero no de 100
ab=int(input("Ingrese el año que solicita: "))
if ab %4==0 and ab %100 !=0:
    print("El año ingresado es bisiesto")
else:
    print("El año ingresado no es bisiesto")

