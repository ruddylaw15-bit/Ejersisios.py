#Validador  de password
#Verificar que la clave tenga 8 caracteres o más
cl=input("Ingrese la contraseña: ")
if len(cl)>=8:
    print("Contraseña valida")
else:
    print("Error:la contraseña debe tener más de 8 caracteres")