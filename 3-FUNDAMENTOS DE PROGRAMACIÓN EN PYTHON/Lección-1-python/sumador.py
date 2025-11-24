print("Ingrese la cantidad de numero que desea sumar")
n = int(input())

print("Ingrese los " + str(n) + " numeros que desea sumar , respectivamente.") 

sum = 0

for i in range(n):
  num = int(input("Ingrese el numero " + str(i + 1) + ": "))
  sum = sum + num

print("La suma de los " + str(n) + " numeros es: " + str(sum))
