 # Solicitar al usuario su edad y mostrar si es mayor de edad o no
edad=int(input("Ingrese su edad: "))
if(edad>=18):
  print("Usted es mayor de edad")
else:
  print("Usted es menor de edad")
  
  
# Desicion multiple con elif solicita al usuario una nota entre 1 y 7 y imprime el resultado avaluativo de la nota
nota=int(input("Ingrese una nota entre 1 y 7: "))
if(nota==1):
  print("Muy deficiente")
elif(nota==2):
  print("Insuficiente")
elif(nota==3):
  print("Suficiente")
elif(nota==4):
  print("Bien")
elif(nota==5):
  print("Notable")
elif(nota==6):
  print("Sobresaliente")
elif(nota==7):
  print("Muy sobresaliente")
else:
  print("Nota no valida")
  
  
#Condiciones anidadas ,solicita un numero entero.
num=int(input("Ingrese un numero entero: "))
if(num>0):
  print("El numero es positivo")
  if(num%2==0):
    print("El numero es par")
  else:
    print("El numero es impar")
else:
  print("El numero es negativo")
  
  
# Condiciones de borde 
num=int(input("Ingrese un numero entre 1 y 100: "))
if(num==1 or num==100):
  print("Estas en un limite permitido")
elif(num>2 and num<98):
  print("Dentro del rango")
else:
  print("Fuera de rango")
