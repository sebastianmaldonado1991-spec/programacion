# Descuentos por cantidad de producto.

while True:
    try:
        cantidad=int(input("ingrese cantidad"))

        if cantidad <=0:
            print("error, la cantidad debe ser mayor que 0")
        else:
            break

    except:
        print("error, no se permiten letras")

precio = 325

if cantidad >= 20:
    total= cantidad*precio*0.70
elif cantidad >= 10:
    total= cantidad*precio*0.83
elif cantidad >=5:
    total= cantidad*precio*0.90
else:
    total= cantidad*precio

print(f"Total a pagar:${total}")
    