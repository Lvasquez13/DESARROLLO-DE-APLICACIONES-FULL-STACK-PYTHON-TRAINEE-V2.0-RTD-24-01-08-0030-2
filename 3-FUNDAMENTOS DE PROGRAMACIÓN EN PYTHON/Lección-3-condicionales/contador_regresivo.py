#  contador regresivo
numero=int(input("Ingrese un numero:"))
descuento=0
contador_regresivo=numero

while descuento<numero:
  print(f"Contador regresivo {contador_regresivo}")
  descuento=descuento+1
  contador_regresivo=contador_regresivo-1

print(f"Contador regresivo {contador_regresivo}")