# ============================
# Introducción a los índices en Python
# ============================

# Una lista es una colección ordenada de elementos
numeros = [10, 20, 30, 40, 50]

# ---------------------------------
# Índices positivos (comienzan en 0)
# ---------------------------------
#  0 -> 10
#  1 -> 20
#  2 -> 30
#  3 -> 40
#  4 -> 50

print(numeros[0])  # Accede al primer elemento -> 10
print(numeros[2])  # Accede al tercer elemento -> 30


# ---------------------------------
# Índices negativos (desde el final)
# ---------------------------------
# -1 -> 50
# -2 -> 40
# -3 -> 30

print(numeros[-1])  # Último elemento -> 50
print(numeros[-3])  # Tercer elemento desde el final -> 30


# =============================
# Recorrer una lista con índices
# =============================
print("\nRecorriendo la lista con índices:")
for i in range(len(numeros)):   # range(5) -> 0,1,2,3,4
    print(f"Índice {i} contiene: {numeros[i]}")


# =============================
# Buscar elementos en la lista
# =============================

# count() -> cuántas veces aparece un valor
veces = numeros.count(20)
print(f"\nEl número 20 aparece {veces} vez/veces.")

# index() -> primera posición donde aparece un valor
posicion = numeros.index(40)
print(f"El número 40 se encuentra en el índice: {posicion}")


# =============================
# Slice: cortar una parte de la lista
# Sintaxis: lista[inicio:fin:paso]
# =============================
fraccion = numeros[1:4]  # Toma desde índice 1 hasta 3 (4 NO se incluye)
print("\nSlice 1:4 =", fraccion)

salto = numeros[0:5:2]   # Del inicio al final, de dos en dos
print("Slice 0:5:2 =", salto)




# =============================
# Declaracion de listas para cumplir con la actividad
a = [5, 1, 4, 9, 0]                               # lista de números


#b = range(3, 10) + range(20, 23) 
b = list(range(3, 10)) + list(range(20, 23))      # unir dos rangos en una lista
                                                   # [3,4,5,6,7,8,9] + [20,21,22]

c = [[1, 2], [3, 4, 5], [6, 7]]                   # lista de listas
d = ["Perro", "Gato", "Jirafa", "Elefante"]       # lista de animales

e = ["e", a, 2 * a]                               # e contiene un string, la lista a, y a repetida dos veces

print(a[2])                                        # índice 2 -> 4
print(b[9])                                        # índice 9 -> 22
print(c[1][2])                                     # sublista 1, índice 2 -> 5
print(e[0] == e[1])                                # compara "e" con lista a -> False

print(len(c))                                      # cantidad de sublistas -> 3
print(len(c[0]))                                   # largo de la primera sublista -> 2
print(len(e))                                      # largo de e -> 3

print(c[-1])                                       # última sublista -> [6, 7]
print(c[-1][+1])                                   # índice 1 de la última sublista -> 7

print(c[2:] + d[2:])                               # concatenar slices -> [[6,7],"Jirafa","Elefante"]

# Slices: lista[inicio:fin:paso]

print(a[3:10])                                     # desde índice 3 hasta antes del 10 -> [9, 0]
print(a[3:10:2])                                   # desde 3 hasta 10, cada 2 -> [9]

print(d.index("Elefante"))                         # posición de "Elefante" -> 3

print(e[c[0][1]])                                  # c[0][1] = 2 -> e[2] -> lista a repetida
print(e[c[0][1]].count(5))                         # cuenta cuántos "5" hay en esa lista -> 2

print(sorted(a)[2])                                # tercer elemento de la lista a ordenada -> 4

print(complex(b[0]))                               # número complejo con parte real b[0] -> (3+0j)
print(complex(b[1]))                               # complejo con b[1] -> (4+0j)
print(complex(b[0], b[1]))                         # complejo (real=b[0], imag=b[1]) -> (3+4j)
