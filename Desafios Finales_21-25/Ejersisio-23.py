#IMC
#Calcular IMC y categoriza
ps=float(input("Ingrese su peso en kg:" ))
at=float(input("Ingrese su altura en metros:" ))
imc=ps/(at*at)
print("Tu IMC es de :",imc)
if imc<=18.5:
    print("Categoria: bajo peso")
elif imc<=25:
    print("categoria: Normal")
else:
    print("Categoria: sobrepeso")    
if imc>=30:
    print("Cateoria: obesidad")