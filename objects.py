# class Galleta:
#     pass

# una_galleta= Galleta()
# otra_galleta= Galleta()

# una_galleta.sabor="dulce"
# una_galleta.color="blanca"

# print(type(una_galleta))
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
#         print("galleta creada y es {} {} ".format(sabor,color))
    
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


#podemos redefinir metodos que ya existen para un objeto, y crear tanto constructores como destructores
class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento

    #destructor, se ejecuta al momento de borrar el objeto
    def __str__(self):
        return "{} lanzada en el {} con una duracion de {}".format(self.titulo,self.lanzamiento,self.duracion)
    def __del__(self):
        print("Se ha borrado la pelicula ",self.titulo)
    def __len__(self):
        print("la peli tiene una duracion de ",self.duracion)
    
class Catalogo:
    catalogo=[]
    def __init__(self,catalogo=[]):
        self.catalogo=catalogo
    def agregar(self,l):
        self.catalogo.append(l)
        print("agregada")
    def mostrar(self):
        for p in self.catalogo:
            print(p)


peli=Pelicula("Totoro","160 minutos","2003")
pel=Pelicula("IT","170 minutos","2005")

catalog=Catalogo()
catalog.agregar(peli)
catalog.agregar(pel)
catalog.mostrar()