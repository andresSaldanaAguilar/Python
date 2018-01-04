def saludar():
    print("hola k tal")

#una observacion con el uso de variables es que una variable a ser usada en la funcion
#debe ser definida no necesariamente antes de la definicion de la funcion pero si antes de
#su llamada

#el tipo de retorno es de aquel objeto retornado 
# def suma():
#     lista=[1,2,3,4]
#     return lista

#print(suma())

#podemos hacer cosas como las siguiente
# def arreglo():
#     return "cadena", 1,[1,2,3]

# c,n,l=arreglo()
# print(c, n,l)

#para mandar parametros hacemos los siguiente:
#los valores nulos son valores por default cuando no se mandan argumentos
# def suma(a=None,b=None): 
#     return a[0]+b

# print(suma([1,2,3],3))
# print(suma(b=4,a=[5,2]))

#las listas son llamadas a las funciones por referencia, es decir, su valor original si es modificado
# a diferencia de una variable simple, que su valor no es modificado al ser llamado a una funcion, se pasa por valor a la funcion

#una lista puede recibir parametros infdefinidos haciendo uso de la palabra "args", guardandolos en una tupla
# def arg_indeterminados(*args):
#     for arg in args:
#         print(arg)

# arg_indeterminados(1,"hola",[1,2,3])

#una numero indeterminado de argumentos tambien puede ser guardado en un diccionario
# def arg_indeterminados(*args,**kwargs):
#         print(args,kwargs)

# arg_indeterminados(1,"hola",[1,2,3],n=1,s="hola",l=[1,2,3])

#factorial

# def factorial(n):
#     if n==1 or n==0 :
#         return 1
#     else:
#         return n*factorial(n-1)

# num=int(input("ingrese el numero a encontrar su factorial:"))
# print(factorial(num))

#------------------------------------------------------funciones integradoras
c="esto es una texto" + str(10) + str(2.333)
#convierte de decimal a binario
binario=bin(9)
#convierte de decimal a hexadecimal
hexa=hex(21)
#convierte de una base a decimal
# print(int('1110', 2))
# print(int('0XA', 16))
#encuentra el valor absoluto
#print(abs(-4))

import math 

#Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
#print(math.ceil(3.33))

#Return x factorial. Raises ValueError if x is not integral or is negative.
#print(math.factorial(5))

#Return the floor of x as a float, the largest integer value less than or equal to x.
#print(math.floor(5.99))

#si se pone el tipo "global" antes de una variable en una funcion, significa que le haremos referencia
#a una variable fuera de la funcion, pasando asi su valor por referencia

def ordenar(lista):
    lpar=[]
    limpar=[]
    for elemento in lista:
        if elemento%2 == 0:
            lpar.append(elemento)
        else:
            limpar.append(elemento)
    return lpar,limpar

l1,l2=ordenar([1,2,3,4,5,6,7,8,9])
 
print(l1)
print(l2)