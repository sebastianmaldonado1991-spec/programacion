nombre = input("ingrese nombre de empleado:")
años = int(input(" ingrese años trabajados"))

while años <0:
    print("el numero debe ser mayor que 0")
    años = int(input("ingrese años trabajados"))

if años <=5:
    bono = 5000
elif años < 20:
    bono = 10000
else:
    bono = 15000

print(nombre, "tiene un bono de:", bono)