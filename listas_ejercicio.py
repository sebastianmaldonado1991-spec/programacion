#juego para adivinar paises segun alguna caracteristica.

paises=["ARGENTINA", "CHILE", "BRASIL", "MEXICO", "VENEZUELA"]

caracteristicas=["campeón del mundo", "observatorios", "pan de azucar", "estadio Azteca","Petroleo robado"]
contar=2


print("Tenes 3 vidas")
    
for contador in range(5):
        
        print("pista:", caracteristicas[contador])
        intento=input("¿A qué pais corresponde?: ")
        intento=intento.upper()
    
   
        if intento == paises[contador]:
            print("Es correcto")

        else:
            print("Incorrecto")
            print("Respuesta:", paises[contador])
            print(f"Te quedan {contar} vidas")
            contar-=1

        if contar == -1:
          print("Perdiste")
          break

print("Fin del juego")
    
    