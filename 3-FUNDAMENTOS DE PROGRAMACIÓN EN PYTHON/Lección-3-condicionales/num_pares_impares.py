#  Pide numeros hasta que ingrese cero y contar cuantos son pares y cuantos impares
num = int(input("Ingrese un numero: "))
pares = 0 
impares = 0
while num != 0:
  if num % 2 == 0:
    pares = pares + 1
    
  else:
    impares = impares + 1
  num = int(input("Ingrese un numero: "))
print("La cantidad de numeros pares es: " + str(pares))
print("La cantidad de numeros impares es: " + str(impares))