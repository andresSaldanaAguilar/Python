#---------------------------------------------cadenas
var1="hola mundote"
#imprime un caracter de el arreglo
#print(var1[0]) #indices positivos basados en cero
#print(var1[-1]) #puedes ocupar indices negativos, que inician en menos uno
#imprime dado un limite superior o inferior, (tecnica de ""SLICING"")
#print(var1[1:])
#print(var1[1:6])
#print(var1[-12:])
#las cadenas son inmutables (no se puede cambiar el valor de un caracter por su indice)
#pero podemos hacer trucos:
#var1= "joj" + var1[1:]
#print(var1)

#----------------------------------------------listas
#las listas son muy flexibles
lista=["una cadena", 12, 3.4, "mas cadenas"]
#print(lista[0])
#print(lista[-1])
#print(lista[1:])
#lista+=[2,3,4,5]
#a diferencia de las cadenas, las listas son mutables
#lista[2]=45
#se puede agregar elementos a la lista, usamos el metodo append()
#lista.append(9)
#lista[:3]= ['D','D','D','A','B','C']
#lista[:3]= []
#para conocer el tamaño de las listas se usa len()
#print(len(lista))
#anidacion de listas
#l1=[1,2,3]
#l2=[4,5,6]
#l3=[7,8,9]
#l4=[l1,l2,l3]
#para acceder a un indice en especifico
#l4[-1][-1]

#-----------------------------------------------inputs
#varx= input("introduce una cadena: ");
#print("mi nombre es el"+varx);

#-----------------------------------------------ciclos
#se usa "break" para que, en un ciclo while se interrumpa su ejecucion
#se usa "continue" si se quiere solamente saltar un ciclo del while

#equivalente al foreach

#cadena="hola a todos"
#for caracter in cadena:
#    print(caracter)

#para listas: 
# lista=['h','o','l','a','s']
# for i,l in enumerate(lista):
#     print(lista[i])

#equivalente al for de otros lenguajes 
#donde 10 es el valor asintotico superior
#for i in range(3,10):
#    print(i)

#my_range(start, end, step)

#-----------------------------------------------------tuplas
tupla=(1,2,3,"sup")
#las tuplas son inmutables al igual que las cadenas, pero podemos hacer slicing e indexar
#como en una lista
#la funcion index(elemento) nos retorna el indice de un elemento
#print(tupla.index(3))
#la funcion count(elemento) nos retorna el no. de veces que se repite el elemento en la tupla

#------------------------------------------------------conjuntos
#con los conjuntos podemos operar con teoria de conjuntos
# conjunto=set()
conjunto={1,2,3}
# conjunto.add(0)
# conjunto.add('A')
# conjunto.add('Z')
# conjunto.add('abelardo')
# conjunto.add('acacio')
# print(conjunto)
#los conjuntos son colecciones desordenadas, no permite elementos duplicados ni indexacion
#usando list(), 
#se puede borrar un elemento de un conjunto usando .discard()

# usuarios=set()
# usuarios={'marta','david','elvira','juan','marcos'}
# administradores=set()
# administradores={'marta','marcos'}

# for usuario in usuarios:
#     if usuario in administradores:
#         print(usuario, "es administrador")
#     else:
#         print(usuario)

#-----------------------------------------------------diccionarios
#son colecciones desordenadas, mutables
diccionario={'palabra_clave':'definicion'}
#se selecciona o borra un elemento por su palabra clave
#print(diccionario['palabra_clave'])
#del(diccionario['palabra_clave'])
# dicc={1:'uno',2:'dos',3:'tres',4:'cuatro'}
# for clave in dicc:
#     print(clave ,dicc[clave])

# caballero={'vida':2,'ataque':2,'defensa':2,'alcance':2}
# guerrero={'vida':2,'ataque':2,'defensa':2,'alcance':2}
# arquero={'vida':2,'ataque':2,'defensa':2,'alcance':2}
# personajes=[caballero,guerrero,arquero]

# caballero['vida']=guerrero['vida']*2
# caballero['defensa']=guerrero['defensa']*2
# guerrero['ataque']=caballero['ataque']*2
# guerrero['alcance']=caballero['alcance']*2
# arquero['vida']=guerrero['vida']
# arquero['ataque']=guerrero['ataque']
# arquero['defensa']=guerrero['defensa']/2
# arquero['alcance']=guerrero['alcance']*2

# for personaje in personajes:
#     print(personaje)


#------------------------------------------------------pilas
#las listas pueden eleminar el ultimo elemento de la lista usando el metodo pop()
#para agregar un elemento recordar append()

#-----------------------------------------------------cola
from collections import deque
#cola=deque(['1','2','3'])
#se ocupa el metodo append para agregar el elemenyo a la cola
#para eliminar un elemento se usa cola.popleft()

# tareas= [
#     [6, 'Distribucion'],
#     [2, 'Diseño'],
#     [1, 'Concepcion'],
#     [7, 'Mantenimiento'],
#     [4, 'Produccion'],
#     [3, 'Planificacion'],
#     [5, 'Pruebas']
# ]
# tareas.sort()
# cola=deque()

# for tarea in tareas:
#     cola.append(tarea[1])

# print(cola)

#------------------------------------------------------scripts
#en el archivo debe ir algo como:
#python3 archivo.py "1er arg" 3
# para recibir los argumentos y ser usado en scripts

import sys
# texto=sys.argv[1]
# numero=int(sys.argv[2])

# validacion=['1','2','3','4','5','6','7','8','9']

# if len(sys.argv) == 3:
#     if sys.argv[1] in validacion and sys.argv[2] in validacion:
#         x=int(sys.argv[1])
#         y=int(sys.argv[2])
#         for i in range(x):
#             for j in range(y):
#                 print("* ",end='')
#             print()
#     else:
#         print("numeros fuera de los posibles")
# else:
#     print("faltan argumentos (dos en total)")
#     sys.exit()

if len(sys.argv) == 2:
    if len(sys.argv[1]) <= 4:
        x=sys.argv[1]
        for i in range(4-len(sys.argv[1])):
            x="0"+x
        print(x[0]+"000")
        print("0"+x[1]+"00")
        print("00"+x[2]+"0")
        print("000"+x[3])
    else: 
        print("El nuemero no puede exceder las 4 cifras.")
else:
    print("faltan argumentos (dos en total)")
    sys.exit()

#-------------------------------------------------------formato de texto
# nombre="andres"
# edad=20
# altura=176
# print("hola mi nombre es {} tengo {} anios y mi altura es {}".format(nombre,edad,altura))
# print("hola mi nombre es {2} tengo {0} anios y mi altura es {1}".format(nombre,edad,altura))
#print("hola mi nombre es {cadena} tengo {numero} anios y mi altura es {numerote}".format(cadena=nombre,numero=edad,numerote=altura))


#notas---------------------------------------------------
#podemos ocupar slicing en tres indices:
# arreglo(a:b:c) donde a es el inicio, b la cota superior y c el tamaño del brinco

#podemos buscar un valor en una lista,conjunto o tupla con la siguiente sintaxis
# if elemento in lista: devuelve true si esta en la lista
# if elemento not in lista

#se puede crear una lista y llenarla con la funcion list()
#se puede ordenar una lista con el metodo sort() 

#podemos modificar una list(), set() a diferente tipo usando los metodos set() list()
# se le puede pasar a set() y list() cadenas para crear una coleccion de caracteres 