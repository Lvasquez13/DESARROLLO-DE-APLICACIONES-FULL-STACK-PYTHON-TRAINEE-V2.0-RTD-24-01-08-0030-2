# Suma acumulativa pedir un unumero al usuario y sumar y cuanodo el usuario ingrese 0 se debe imprimir la suma acumulativa
num=int(input("Ingrese un numero: "))
sum=0 
while num!=0:
  sum=sum+num
  num=int(input("Ingrese un numero: "))
print("La suma acumulativa es: " + str(sum))