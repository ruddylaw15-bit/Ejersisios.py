#Crear calculadora
x=float(input("Ingrese primer valor númerico: "))
y=float(input("Ingrese segundo valor númerico: "))
op=input("Operación que deseada +, -, *, /: ")
#Suma
if op=="+":
 print("Suma:", x+y)
#Resta
elif op=="-":
 print("Resta:",x-y)
#Multiplicacion
elif op=="*":
 print("Multiplicacion:",x*y)
#Division
elif op=="/":
 print("Division:", x/y)
else:
 print("Error: No se puede divir por 0")
print("El resultado de la operacion marcada es:",op) 