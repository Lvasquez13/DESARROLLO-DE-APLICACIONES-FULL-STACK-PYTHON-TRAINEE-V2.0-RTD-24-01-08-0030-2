nombres = [
    "Luis",
    "María",
    "Pedro",
    "Ana",
    "Carlos",
    "Sofía",
    "Javier",
    "Valentina",
    "Ricardo",
    "Camila",
    "Andrés",
    "Fernanda",
    "Diego",
    "Josefina",
    "Mateo"
]
# contar los que empiezan con "vocales
inician_con_vocales = 0
for nombre in nombres:
    if nombre[0] in "aeiouAEIOU":
        inician_con_vocales += 1
print(inician_con_vocales)