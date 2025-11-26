# contador regresivo

numero = int(input("Ingrese un numero (negativo para salir): "))

while numero >= 0:     # mientras sea positivo o cero
    descuento = 0
    contador_regresivo = numero
    
    # contador regresivo
    while descuento <= numero:
        print(f"Contador regresivo: {contador_regresivo}")
        descuento += 1
        contador_regresivo -= 1

    # pedir otro número
    numero = int(input("Ingrese otro número (negativo para salir): "))
