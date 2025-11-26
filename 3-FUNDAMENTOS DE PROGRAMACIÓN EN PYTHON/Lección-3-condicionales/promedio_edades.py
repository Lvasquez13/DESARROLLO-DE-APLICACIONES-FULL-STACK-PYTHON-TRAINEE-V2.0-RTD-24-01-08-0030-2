#  pedir ingresar edades hasta que se ingrese 0 y mostrar el promedio de edades ingresadas
edad = int(input("Ingrese una edad: ")) # inicialmente se muetras este input ya que luego se cae en el while 
acumulador = 0 # esta variable se utiliza para almacenar la suma de las edades
contador = 0 # esta variable se utiliza para contar el total de edades ingresadas
while edad != 0:
  acumulador = acumulador + edad
  contador = contador + 1
  edad = int(input("Ingrese una edad: "))

promedio = acumulador / contador
print("El promedio de las edades es: " + str(promedio))