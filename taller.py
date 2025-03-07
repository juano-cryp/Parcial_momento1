Compra = int(input("Ingrese el monto de la compra: "))
Descuento = 0


if Compra < 50:
    Descuento = 0 
elif 50 <= Compra <=100:
    Descuento = 0.5
elif Compra > 100:
    Descuento = 0.10
Descuento = Compra * Descuento
Monto_total = Compra - Descuento


print (f"Descuento aplicado", Descuento)
print (f"Total a pagar", Monto_total)






