#Triángulo
#Pedir 3 lados y decide si se puede formarse un
#triángulo (a+b>c)
print("Ingrese los siguientes datos")
ld1=float(input("Ingrese primer lado del triangulo: "))
ld2=float(input("Ingrese segundo lado del triangulo: "))
ld3=float(input("Ingrese tercer lado del triangulo: "))
if ld1+ld2>ld3 and ld2+ld3>ld1 and ld3+ld1>ld2:
    print("Es un triángulo valido")
else:
    print("No es un triángulo valido")