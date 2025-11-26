# 1- Uso basico del while
i = 0
while i <= 5:
  print(i) # se imprime el valor de i
  i += 1 # se incrementa i en 1 para que cuando tome el valor 5 se salga del ciclo
  
# 2- Uso basico del for , a diferencia del whiw while, el for no necesita un contador
frutas=["manzana", "banana", "pera", "uva", "kiwi", "mango"]
for fruta in frutas:
  print(fruta)
  
# 3-Condicion de un ciclo
for i in range(11): # range(11) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
  if i % 2 == 0: # si el modulo de i es igual a 0 quieres decir que es par
    print(f"Es par {i}")
  else:
    print(f"Es impar {i}")# caso contrario es impar 


# 4-Ciclo infinito controlado con break pide numero y si ingresa 0 se sale
num = int (input("Ingrese un numero: "))
while num != 0:
  print(f"Estoy en un ciclo infinito , numero ingresado {num}.")
  num =int (input("Ingrese un numero: "))
  if num == 0:
    break  
print("Saliste del ciclo.")

# 5-ciclos anidados
for i in range(1, 4):          # tablas del 1 al 3
    print(f"\nTabla del {i}:")
    
    for j in range(1, 4):     # multiplicar del 1 al 3
        print(f"{i} x {j} = {i*j}")

    print("\n") 

# 6-Ciclo infinito controlado con continue pide numero y si ingresa 0 se sale
nombres = ["Juan", "María", "Pedro", "Lucía", "Andrés", "Carolina"]
for nombre in nombres:
  if nombre == "Juan":
    # print("El nombre es Juan y no sera listado")
    continue
  print(nombre) 

