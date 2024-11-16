#Taller Listas Python
#Juan Esteban Hoyos    
#14/11/2024
#El taller está diseñado para guiar a los estudiantes, que tradicionalmente han trabajado con Java, a adaptarse rápidamente a la sintaxis y el estilo de programación con listas en Python.

# 1. Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
# Definimos una lista llamada 'frutas' con 5 frutas típicas de Colombia
frutas = ["Mango", "Guanábana", "Lulo", "Maracuyá", "Borojó"]
# Usamos la función print() para mostrar el contenido de la lista en pantalla
print(frutas)


# 2.Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
# Accedemos al segundo elemento de la lista 'frutas' usando el índice 1 (los índices empiezan en 0)
segundo_elemento = frutas[1]
# Accedemos al cuarto elemento de la lista 'frutas' usando el índice 3
cuarto_elemento = frutas[3]
# Imprimimos el segundo y el cuarto elemento
print(segundo_elemento)
print(cuarto_elemento)


# 3. Crear una lista con los números del 1 al 10 y mostrar su longitud.
# Definimos una lista llamada 'numeros' que contiene los números del 1 al 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Usamos la función len() para obtener la longitud de la lista 'numeros'
longitud = len(numeros)
# Imprimimos la longitud de la lista
print(longitud)


# 4. Concatenar las dos listas creadas en los ejercicios 1 y 3.
# Concatenamos la lista 'frutas' con la lista 'numeros' usando el operador +
lista_concatenada = frutas + numeros
# Imprimimos la lista concatenada
print(lista_concatenada)


# 5. Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
# Cambiamos el tercer elemento de 'lista_concatenada' (índice 2) al valor 100
lista_concatenada[2] = 100
# Imprimimos la lista actualizada
print(lista_concatenada)


# 6. Borrar el último elemento de la lista del ejercicio 4.
# Eliminamos el último elemento de 'lista_concatenada' usando el método pop()
lista_concatenada.pop()
# Imprimimos la lista después de borrar el último elemento
print(lista_concatenada)


# 7. Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
# Definimos una lista 'numeros_enteros' con 3 números enteros
numeros_enteros = [1, 2, 3]
# Usamos una comprensión de lista para multiplicar cada elemento por 5
numeros_multiplicados = [x * 5 for x in numeros_enteros]
# Imprimimos la lista con los números multiplicados
print(numeros_multiplicados)


# 8. Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes de ambas listas
# Definimos dos listas con 5 números enteros cada una
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]
# Usamos una comprensión de lista para multiplicar los elementos correspondientes de ambas listas
resultados_multiplicados = [a * b for a, b in zip(lista1, lista2)]
# Imprimimos la lista con los resultados de la multiplicación
print(resultados_multiplicados)


# 9. Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista
# Definimos una lista de listas anidadas
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accedemos al segundo elemento de la segunda lista usando índices
segundo_elemento_segunda_lista = lista_anidada[1][1]
# Imprimimos el segundo elemento de la segunda lista
print(segundo_elemento_segunda_lista)


# 10. Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6
# Usamos el slicing para tomar los elementos del índice 2 al 6 de la lista 'numeros'
sub_lista = numeros[2:7]
# Imprimimos la sublista creada
print(sub_lista)


# 11. Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1
# Usamos el método .append() para agregar un nuevo elemento a la lista 'frutas'
frutas.append("Papaya")
# Imprimimos la lista después de agregar el nuevo elemento
print(frutas)


# 12. Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3
# Usamos el método .insert() para agregar un nuevo elemento en la posición 2 de la lista 'numeros'
numeros.insert(2, 25)
# Imprimimos la lista después de insertar el nuevo elemento
print(numeros)


# 13. Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7
# Usamos el método .remove() para eliminar el elemento 15 de la lista 'numeros_multiplicados'
numeros_multiplicados.remove(15)
# Imprimimos la lista después de eliminar el elemento
print(numeros_multiplicados)


# 14. Usar el método .reverse() para invertir el orden de la lista del ejercicio 4
# Usamos el método .reverse() para invertir el orden de la lista 'lista_concatenada'
lista_concatenada.reverse()
# Imprimimos la lista después de invertir su orden
print(lista_concatenada)


# 15. Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7
# Usamos el método .sort() para ordenar la lista 'numeros_multiplicados' de forma ascendente
numeros_multiplicados.sort()
# Imprimimos la lista después de ordenarla
print(numeros_multiplicados)


# 16. Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4
# Usamos el método .pop() para eliminar y obtener el último elemento de 'lista_concatenada'
ultimo_elemento = lista_concatenada.pop()
# Imprimimos el elemento eliminado
print(ultimo_elemento)
# Imprimimos la lista después de eliminar el último elemento
print(lista_concatenada)


# 17. Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7
# Usamos el método .count() para contar cuántas veces aparece el elemento 20 en 'numeros_multiplicados'
conteo = numeros_multiplicados.count(20)
# Imprimimos el resultado del conteo
print(conteo)


# 18. Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4
# Usamos el método .index() para obtener el índice del elemento 100 en 'lista_concatenada'
indice = lista_concatenada.index(100)
# Imprimimos el índice del elemento encontrado
print(indice)

# 19. Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1
# Usamos el método .clear() para eliminar todos los elementos de la lista 'frutas'
frutas.clear()
# Imprimimos la lista después de eliminar todos los elementos
print(frutas)


# 20. Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10
# Creamos una lista vacía llamada 'numeross'
numeross = []
# Usamos un bucle for para agregar los números del 1 al 10 a la lista
for i in range(1, 11):
    numeross.append(i)
# Imprimimos la lista con los números del 1 al 10
print(numeross)


# 21. Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares
# Creamos una lista de números enteros
numeros_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Usamos un bucle while para eliminar los elementos impares
i = 0
while i < len(numeros_enteros):
    if numeros_enteros[i] % 2 != 0:
        numeros_enteros.remove(numeros_enteros[i])
    else:
        i += 1
# Imprimimos la lista después de eliminar los números impares
print(numeros_enteros)


# 22. Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente  
# Creamos una lista con los nombres de 5 materias favoritas
materias = ["Matemáticas", "Física", "Química", "Historia", "Inglés"]
# Usamos el método .sort() para ordenar la lista 'materias' alfabéticamente
materias.sort()
# Imprimimos la lista ordenada alfabéticamente
print(materias)


# 23. Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3
# Creamos una lista con los números del 1 al 15
numeros2 = list(range(1, 16))
# Usamos una comprensión de lista para obtener solo los múltiplos de 3
multiplos_de_3 = [x for x in numeros2 if x % 3 == 0]
# Imprimimos la lista de los múltiplos de 3
print(multiplos_de_3)


# 24. Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas
# Creamos una lista con los nombres de 10 artistas favoritos
artistas = ["Shakira", "Carlos Vives", "Juanes", "Maluma", "Sofía Vergara", "J Balvin", "Karol G", "Aventuras", "Drake", "Rihanna"]
# Usamos un bucle for para imprimir cada nombre en mayúsculas
for artista in artistas:
    print(artista.upper())


# 25. Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares
# Creamos una lista con los números del 1 al 20
numeros1 = list(range(1, 21))
# Usamos una comprensión de listas para obtener solo los números pares
numeros_pares = [x for x in numeros1 if x % 2 == 0]
# Imprimimos la lista de números pares
print(numeros_pares)


# 26. Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso
# Creamos una lista con los nombres de los municipios del departamento de Arauca
municipios = ["Arauca", "Arauquita", "Cravo Norte", "Fortul", "Tame", "Puerto Rondón", "Saravena", "Cubará", "La Salina", "Puerto Nariño"]
# Usamos un bucle for para imprimir cada nombre en orden inverso
for municipio in reversed(municipios):
    print(municipio)


# 27. Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número
# Creamos una lista con los números del 1 al 12
numeros3 = list(range(1, 13))
# Usamos una comprensión de listas para obtener los cuadrados de cada número
cuadrados = [x ** 2 for x in numeros3]
# Imprimimos la lista de los cuadrados de los números
print(cuadrados)


# 28. Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio"
# Creamos una lista con los meses del año
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
# Usamos el método .index() para obtener el índice del mes "Junio"
indice_junio = meses.index("Junio")
# Imprimimos el índice de "Junio"
print(indice_junio)


# 29. Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista
# Creamos una lista con los nombres de las mascotas
mascotas = ["Rex", "Bella", "Luna", "Max", "Rocky", "Chester"]
# Usamos el método .remove() para eliminar una mascota de la lista, por ejemplo "Max"
mascotas.remove("Max")
# Imprimimos la lista después de eliminar la mascota
print(mascotas)


# 30. Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente
# Creamos una lista con los números del 1 al 20
numeros4 = list(range(1, 21))
# Usamos el método .sort(reverse=True) para ordenar la lista de forma descendente
numeros4.sort(reverse=True)
# Imprimimos la lista ordenada de forma descendente
print(numeros4)


# 31. Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista
# Creamos una lista con los nombres de 4 libros favoritos
libros = ["Cien años de soledad", "1984", "Don Quijote de la Mancha", "Fahrenheit 451"]
# Usamos el método .append() para agregar un nuevo libro al final de la lista
libros.append("El principito")
# Imprimimos la lista después de agregar el nuevo libro
print(libros)


# 32. Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares
# Creamos una lista con los números del 1 al 15
numeros5 = list(range(1, 16))
# Usamos una comprensión de listas para obtener los números impares
numeros_impares = [x for x in numeros5 if x % 2 != 0]
# Imprimimos la lista de números impares
print(numeros_impares)


# 33. Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3
# Creamos una lista con los nombres de 7 comidas favoritas
comidas = ["Pizza", "Hamburguesa", "Tacos", "Sushi", "Pasta", "Ensalada", "Huevos"]
# Usamos el método .insert() para agregar una nueva comida en la posición 3
comidas.insert(3, "Arepa")
# Imprimimos la lista después de agregar la nueva comida
print(comidas)


# 34. Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15
# Creamos una lista con los números del 1 al 10
numeros_1_10 = list(range(1, 11))
# Creamos una segunda lista con los números del 11 al 15
numeros_11_15 = list(range(11, 16))
# Usamos el método .extend() para agregar la segunda lista a la primera
numeros_1_10.extend(numeros_11_15)
# Imprimimos la lista extendida
print(numeros_1_10)


# 35. Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista
# Creamos una lista con los nombres de 6 compañeros
companeros = ["Daniel", "Esteban", "Jose", "Daniel", "Luis", "Juliana"]
# Usamos el método .count() para contar cuántas veces aparece el nombre "Daniel"
conteo_daniel = companeros.count("Daniel")
# Imprimimos el conteo de cuántas veces aparece el nombre "Daniel"
print(conteo_daniel)


# 36. Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3
# Creamos una lista con los números del 1 al 12
numeros6 = list(range(1, 13))
# Usamos una comprensión de listas para obtener los números divisibles por 3
divisibles_por_3 = [x for x in numeros6 if x % 3 == 0]
# Imprimimos la lista de números divisibles por 3
print(divisibles_por_3)


# 37. Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista
# Creamos una lista con los nombres de 5 artistas musicales favoritos
artistas1 = ["Shakira", "Luis Fonsi", "Bad Bunny", "J Balvin", "Maluma"]
# Usamos el método .reverse() para invertir el orden de la lista
artistas1.reverse()
# Imprimimos la lista invertida
print(artistas1)


# 38. Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente
# Creamos una lista con los números del 1 al 20
numeros7 = list(range(1, 21))
# Usamos una función lambda y el método .sort() para ordenar la lista de forma descendente
numeros7.sort(key=lambda x: -x)
# Imprimimos la lista ordenada de forma descendente
print(numeros7)


# 39. Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista
# Creamos una lista con las materias de la universidad
materias1 = ["Cálculo", "Programación", "Bases de Datos", "Física", "Formulación"]
# Usamos el método .pop() para eliminar y obtener el último elemento de la lista
ultimo_elemento = materias1.pop()
# Imprimimos el elemento eliminado y la lista después de la eliminación
print("Elemento eliminado:", ultimo_elemento)
print("Lista después de la eliminación:", materias1)


# 40. Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5
# Creamos una lista con los números del 1 al 25
numeros8 = list(range(1, 26))
# Usamos una comprensión de listas para obtener los números múltiplos de 5
multiplos_de_5 = [x for x in numeros8 if x % 5 == 0]
# Imprimimos la lista de múltiplos de 5
print(multiplos_de_5)


# 41. Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método .sort() para ordenar la lista
# Creamos una lista con los nombres de 8 deportes
deportes = ["Fútbol", "Baloncesto", "Tenis", "Natación", "Voleibol", "Béisbol", "Golf", "Ciclismo"]
# Usamos una función anónima (lambda) y el método .sort() para ordenar la lista
deportes.sort(key=lambda x: x.lower())  # Ordenamos de forma alfabética sin distinguir mayúsculas
# Imprimimos la lista ordenada
print(deportes)


# 42. Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista
# Creamos una lista con los números del 1 al 15
numeros9 = list(range(1, 16))
# Usamos el método .clear() para eliminar todos los elementos de la lista
numeros9.clear()
# Imprimimos la lista después de eliminar todos sus elementos
print(numeros9)


# 43. Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas
# Creamos una lista con los nombres de 6 países
paises = ["Colombia", "México", "Argentina", "España", "Francia", "Brasil"]
# Usamos un bucle for para imprimir cada nombre en minúsculas
for pais in paises:
    print(pais.lower())


# 44. Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares
# Creamos una lista con los números del 1 al 20
numeros10 = list(range(1, 21))
# Usamos una comprensión de listas para obtener los cuadrados de los números pares
cuadrados_pares = [x**2 for x in numeros10 if x % 2 == 0]
# Imprimimos la lista de los cuadrados de los números pares
print(cuadrados_pares)


# 45. Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico
# Creamos una lista con los nombres de 10 videojuegos
videojuegos = ["The Last of Us", "Minecraft", "Fortnite", "Call of Duty", "GTA V", "Apex Legends", "FIFA 21", "Zelda: Breath of the Wild", "Red Dead Redemption 2", "Overwatch"]
# Usamos el método .index() para obtener el índice de un videojuego específico
indice_juego = videojuegos.index("GTA V")
# Imprimimos el índice del juego específico
print("El índice de 'GTA V' es:", indice_juego)


# 46. Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista
# Creamos una lista con los números del 1 al 12
numeros11 = list(range(1, 13))
# Usamos el método .remove() para eliminar el número 5 de la lista
numeros11.remove(5)
# Imprimimos la lista después de eliminar el número específico
print(numeros11)


# 47. Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre
# Creamos una lista con los nombres de 7 monumentos colombianos
monumentos = ["Monumento a los Héroes", "Castillo de San Felipe de Barajas", "La Ciudad Perdida", "Torre del Reloj", "Monumento a la Madre", "Santuario de Las Lajas", "Monumento a Bolívar"]
# Usamos una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre
monumentos.sort(key=lambda x: len(x))
# Imprimimos la lista ordenada por longitud de nombre
print(monumentos)


# 48. Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5
# Creamos una lista con los números del 1 al 18
numeros12 = list(range(1, 19))
# Usamos una comprensión de listas para obtener los números múltiplos de 3 y 5
multiplos_3_y_5 = [x for x in numeros12 if x % 3 == 0 or x % 5 == 0]
# Imprimimos la lista de múltiplos de 3 y 5
print(multiplos_3_y_5)


# 49. Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista
# Creamos una lista con los nombres de 6 asignaturas interesantes
asignaturas = ["Algoritmos", "Bases de Datos", "Redes de Computadoras", "Desarrollo Web", "Ingeniería de Software", "Sistemas Operativos"]
# Usamos el método .append() para agregar una nueva asignatura al final de la lista
asignaturas.append("Inteligencia Artificial")
# Imprimimos la lista después de agregar el nuevo nombre
print(asignaturas)


# 50. Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7
# Creamos una lista con los números del 1 al 25
numeros13 = list(range(1, 26))
# Usamos el método .pop() para eliminar y obtener el elemento de la posición 7 (índice 6)
elemento_eliminado = numeros13.pop(6)
# Imprimimos el elemento eliminado y la lista actualizada
print("Elemento eliminado:", elemento_eliminado)
print("Lista actualizada:", numeros13)

