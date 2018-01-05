# class Galleta:
#     pass

# una_galleta= Galleta()
# otra_galleta= Galleta()

# una_galleta.sabor="dulce"
# una_galleta.color="blanca"

# print(ty1pe(una_galleta))
# print(una_galleta.sabor

# class Galleta:
#     chocolate=False

# ga=Galleta()
# ga.chocolate=True

#------------el metodo init es el metodo constructor

# class Galleta:
#     chocolate=False

#     def __init__(self,color,sabor):
#         self.color=color
#         self.sabor=sabor
#         print("galleta creada y1 es {} {} ".format(sabor,color))
    
#     def __init__(self):
#             print("galleta creada.")

#     def chocolatear(self):
#         self.chocolate= True
#     def tiene_chocolate(self):
#         if self.chocolate:
#             print("La galletina tiene chocolatini")
#         else:
#             print("La galletina no tiene chocolatini")


# oreo=Galleta()
# oreo.tiene_chocolate()
# oreo.chocolatear()
# oreo.tiene_chocolate()


#podemos redefinir metodos que y1a ex1isten para un objeto, y1 crear tanto constructores como destructores
# class Pelicula:
#     def __init__(self,titulo,duracion,lanzamiento):
#         self.titulo=titulo
#         self.duracion=duracion
#         self.lanzamiento=lanzamiento
#     def __len__(self):
#         print("la peli tiene una duracion de ",self.duracion)
    
# class Catalogo:
#     catalogo=[]
#     def __init__(self,catalogo=[]):
#         self.catalogo=catalogo
#     def agregar(self,l):
#         self.catalogo.append(l)
#         print("agregada")
#     def mostrar(self):
#         for p in self.catalogo:
#             print(p)


# peli=Pelicula("Totoro","160 minutos","2003")
# pel=Pelicula("IT","170 minutos","2005")

# catalog=Catalogo()
# catalog.agregar(peli)
# catalog.mostrar()
# catalog.agregar(pel)
# catalog.mostrar()
import math

class Punto:
    x1=0
    y1=0
    x2=0
    y2=0
    def __init__(self,x1=0,y1=0):
        self.x1=x1
        self.y1=y1
    def __str__(self):
        return "({},{})".format(self.x1,self.y1)
    def  cuadrante(self):
        if self.x1 > 0 and self.y1 > 0:
            print("1er cuadrante")
        elif self.x1 < 0 and self.y1 > 0:
            print("2o cuadrante")
        elif self.x1 < 0 and self.y1 < 0:
            print("3er cuadrante")
        elif self.x1 > 0 and self.y1 < 0:
            print("4o cuadrante")
        else:
            print("Sobre el origen")
    def vector(self):
        self.x2=int(input("Introduce la coordenada x2: "))
        self.y2=int(input("Introduce la coordenada y2: "))
        print("El vector resultante es ({},{})".format(self.x2-self.x1,self.y2-self.y1))
    def distancia(self):
        self.x2=int(input("Introduce la coordenada x2: "))
        self.y2=int(input("Introduce la coordenada y2: "))
        print("El vector resultante es ({})".format(math.sqrt(math.pow(self.x2-self.x1,2)+math.pow(self.y2-self.y1,2))))

class Rectangulo:
    p1=Punto(0,0)
    p2=Punto(0,0)
    def __init__(self,p1=Punto(0,0),p2=Punto(0,0)):
        self.p1=p1
        self.p2=p2
    def base(self):
        print("La base del rectangulo es: {}".format(math.sqrt(math.pow(p2.x1-p1.x1,2)+math.pow(p2.y1-p2.y1,2))))
        return math.sqrt(math.pow(p2.x1-p1.x1,2)+math.pow(p2.y1-p2.y1,2))
    def altura(self):
        print("La altura del rectangulo es: {}".format(math.sqrt(math.pow(p2.x1-p2.x1,2)+math.pow(p2.y1-p1.y1,2))))
        return math.sqrt(math.pow(p2.x1-p2.x1,2)+math.pow(p2.y1-p1.y1,2))
    def area(self):
        print("El area es: {}".format(self.base()*self.altura()))

# x1=int(input("Introduce la coordenada x: "))
# y1=int(input("Introduce la coordenada y: "))      
p1=Punto(2,3)
p2=Punto(-1,-2)
p1.cuadrante()
p2.cuadrante()
rec=Rectangulo(p1,p2)
rec.base()
rec.altura()
rec.area()


        