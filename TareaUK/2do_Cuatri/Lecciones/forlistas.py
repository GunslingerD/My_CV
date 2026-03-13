#Iteración sobre listas
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
     print(fruta)

#Iteración sobre listas
mensaje = "Hola"
for caracter in mensaje:
    print(caracter)

#Iteración sobre rangos
for i in range(5):
    print(i)

#Iteración sobre listas anidadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(elemento)

#Iteracion con indices
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

#Iteración sobre diccionarios
estudiantes = {"Juan": 8.5, "Ana": 9.0, "Luis": 7.5}
for nombre, calificacion in estudiantes.items():
    print(f"Estudiante: {nombre}, Calificación: {calificacion}")

#Iteración sobre conjuntos
numeros = {1, 2, 3, 4, 5}
for numero in numeros:
    print(numero)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} es par")

#