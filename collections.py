from collections import *

#----------------------------------------------------------Counter
l=[1,2,3,4,4,5,6,1,2,5]
#print(Counter(l))
p="rojo azul rojo azul rojo amarillo "
#print(Counter(p))
mc=Counter(p.split())
#print(mc) #al convertir la cadena en una lista con cadenas, entonces ahora contara cadenas

#print(mc.most_common(1)) #con el uno le indicamos que solo queremos conocer el mas comun

lc=Counter(l)
#print(lc.items())
#print(lc.keys())
#print(lc.values())
#print(sum(lc.keys())) #al pasarle el total de cada uno de los items, nos da el total de la lista

li=list(lc)
#print(li) #al convertirlo de nuevo en una lista, guardara los elementos originales pero sin repeticion


#---------------------------------------------------------defaultdict
#le da un valor por default a una llave, lo cual no es posible en uno convecnional, pero no tiene orden
df=defaultdict(int)
df['something']
print(df)
df=defaultdict(str)
df['something']
df['cadena']='hola k ase' #la declaracion de un elemento es diferente a la de un diccionario convencional
print(df)

#--------------------------------------------------------OrderedDict
#guarda los elementos en el orden en el que son agregados
od=OrderedDict()
od['uno']='one'
od['dos']='two'
print(od)
#notas
#para ocupar funciones mas especificas, se debe convertir la lista en un COUNTER
