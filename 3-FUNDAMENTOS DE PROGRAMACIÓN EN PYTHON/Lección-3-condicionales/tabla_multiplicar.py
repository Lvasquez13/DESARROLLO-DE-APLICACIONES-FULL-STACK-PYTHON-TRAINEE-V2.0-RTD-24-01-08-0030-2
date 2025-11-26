# pide ingresar un numero y mostrar la tabla de multiplicar
num = int(input("Ingrese un numero: "))
while  num > 0:
   for i in range(1, 11):
    print(str(num) + " x " + str(i) + " = " + str(num * i))

   num = int(input("Ingrese un numero: "))