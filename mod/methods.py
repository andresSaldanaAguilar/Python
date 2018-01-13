# #------------------------------------------------cadenas
# print("hola mundo".upper())
# print("HOLA MUNDO".lower())
# print("hola MUndo".capitalize())
# print("holA mUndo".title())
# print("Hola Mundo".count('a'))
# print("hola mundo".find('o'))
# print("hola mundo".rfind('o')) #busqueda invertida de caracter

# n="12c"
# print(n.isdigit()) #comprueba si solamente contiene digitos la cadena

# n1="12abcd"
# print(n1.isalnum()) #comprueba si es alfanumerico
# print(n1.isalpha()) #comprueba si es alfabetico
# print(n1.startswith('1'))
# print(n1.endswith('1'))

# l="hola como estas".split()
# print(l)

# l="hola como estas".split()[1:]
# print(l)

# l="hola,como,estas".split(',')
# print(l)

# print(".".join("dayanne"))

# print("      hola k tal        ".strip())

# print("me nombre es efi".replace('e','i'))

# print("mono l l l l".replace('l','',3).replace(' ',''))
# #otros metodos:
# #islower()
# #isupper()
# #istitle

# #-----------------------------------------listas
# lista=[1,2,3,4,5]
# lista.append(6)
# lista.clear()

# l1=[1,2,3,3]
# l2=[4,5,6]
# l1.extend(l2)
# print(l1)
# print(l1.count(3))
# print(l1.index(3))

# l1.insert(0,9)
# l1.insert(-1,0)
# print(l1)
# l1.pop(0) #remover elemento de indice
# print(l1)
# l1.remove(5) #remover elemento en especifico, solo removera un elemento a la vez
# l1.reverse()

# li=list("anita lava la tina")
# li.reverse()
# c="".join(li)
# c.replace(' ','')
# print(c)

#---------------------------------conjuntos
# c={3,4,6}
# c.add(1)
# c.add(2)
# c.discard(2)
# print(c)
# #se utiliza el metodo copy para crear una copia exacta de un conjunto, ya que si lo hacemos
# #asigmandolo de manera directa se copiara por referencia y no por valor
# c1=c.copy()
# c1.add(6)
# print(c)
# print(c1)

# c2={1,2,3}
# c3={3,4,5}
# c4={-1,99}
# c5={1,2,3,4,5}

# print(c2.isdisjoint(c3)) #el c2 tiene algo en comun con el c3?
# print(c2.isdisjoint(c4)) #el c2 tiene algo en comun con el c4?
# print(c2.issubset(c5)) #el c2 es subconjunto de c5?
# print(c5.issuperset(c2)) #el c5 contiene a c2?

# print(c2.union(c3)) #realiza la union, no modifica ningun conjunto
# print(c2)
# #c2.update(c3) #realiza la union y actualiza el conjunto
# print(c2)

# print(c2.difference(c3)) #diferencia de c2 con c3
# #c2.difference_update(c3)
# print(c2)

# c2.intersection(c3) #interseccion de conjuntos
# #c2.intersection_update(c3)
# print(c2)

# print(c2.symmetric_difference(c3)) #todos los elementos que no concuerdan

#----------------------------------------------------diccionario

# colores={"amarillo":"yellow","rojo":"red","azul":"blue"}
# print(colores['amarillo'])
# print(colores.get('negro','no se encuentra'))
# print('negro' in colores)

# print(list(colores.keys()))
# print(list(colores.items()))

# for c in colores:
#     print(colores[c])

# for c in colores.values():
#     print(c)

# for c,v in colores.items():
#     print(c,v)

# print(colores.pop('negreo','no se encontro'))

#--------------------------------------------------ejercicios
# c="un dia el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo el monje#lo que se mueve es el viento -respondio el monje"
# c=c.split('#')
# for i in range(len(c)):
#     c[i]=c[i].capitalize()
#     if i==0:
#         c[i]=c[i]+"..."
#     else:
#         c[i]='-'+c[i]+'.'

# cad=""
# for ce in c:
#     cad+=ce
#     cad+='\n'

# print(cad)

lista=[29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]

def modificar(lista):
    num=0
    li=[]
    for el in lista:
        if abs(el)%2 == 0 and el not in li:
            li.append(el)

    num=sum(li)
    li.sort(reverse=True)
    li.insert(0,num)
    print(li)

modificar(lista)
print(lista)

class Objeto:
    def __init__(self):
        print("hola soy un objeto :D")
