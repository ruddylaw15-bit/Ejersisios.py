#Juego de adivinar
#Define un número secreto y deja 
#que el usuario intente una vez
srt=8
intento=int(input("Adivina el número del 1 al 10: "))
if intento==srt:
    print ("Adivinaste el número secreto")
else:
    print("El número ingresado es incorrecto")
