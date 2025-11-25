numeros = [3, 5, 5, 2, 2]

# Recorro hasta el penúltimo índice
for i in range(len(numeros) - 1):
    
    print(numeros[i] )   # numeros[i]  → elemento actual
    print (numeros[i + 1])  # numeros[i + 1] → elemento siguiente

    if numeros[i] == numeros[i + 1]:
        print("Se repite:", numeros[i])
