from io import open

# arch = open('archivo.txt','w') #creamos el archivo exista o no (sobreescribe), en modo escritura
# arch.write("sup dude, what's going on")
# arch.close()


# arch = open('archivo.txt','r') #abrimos el archivo en modo lectura
# print(arch.read()) #guarda el archivo leido como una cadena
# arch.close()


# arch = open('archivo.txt','r') #abrimos el archivo en modo lectura
# print(arch.readlines()) #guarda el archivo leido como una lista
# arch.close()


# arch = open('archivo.txt','a') #append al archivo, no se sobreescribe
# arch.write("\nsee ya!")
# arch.close()


# arch = open('archivo.txt','r') #abrimos el archivo en modo lectura
# print(arch.readline()) #guarda una linea (cadena), el puntero empieza en la primer linea
# print(arch.readline()) 
# arch.close()


# arch = open('archivo.txt','r') #abrimos el archivo en modo lectura
# arch.seek(2) #cambia el puntero al indice 2
# print(arch.read()) 
# arch.seek(0) #cambia el puntero al inicio 
# print(arch.read()) 
# print(arch.read(20)) 
# print(arch.read()) 
# arch.close()


# arch = open('archivo.txt','r+') #abrimos el archivo en modo lectura y escritura
# print(arch.read()) 
# arch.close()

