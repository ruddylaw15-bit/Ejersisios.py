#Descuento
#Si compra >100 aplica 10% de descuento
#si no precio normal 
compra=int(input("Ingrese valor de compra: "))
if compra>100:
    total=compra*0.90
    print("Obtuvo un descuento del 10% y su compra es de:",total)
else:
    print("Descuento a valor de compra mayor a 100")