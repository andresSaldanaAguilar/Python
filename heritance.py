#podemos crear herencia usando parentesis referenciando a la clase padre o superclase, y sobreescribir
#sus metodos:

# class Producto:
#     def __init__(self,referencia,nombre,pvp,descripcion):
#         self.referencia=referencia
#         self.nombre=nombre
#         self.pvp=pvp
#         self.descripcion=descripcion
#     def __str__(self):
#         return"""
#         REFERENCIA: {}
#         NOMBRE:     {}
#         PVP:        {}
#         DESCRIPCION:{}
#         """.format(self.referencia,self.nombre,self.pvp,self.descripcion)

# class Adorno (Producto):
#     pass

# class Alimento (Producto):
#     productor=""
#     distribuidor=""
#     def __str__(self):
#         return"""
#         REFERENCIA:  {}
#         NOMBRE:      {}
#         PVP:         {}
#         DESCRIPCION: {}
#         PRODUCTOR:   {}
#         DISTRIBUIDOR:{}
#         """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)
        
# class Libro (Producto):
#     isbn=""
#     autor=""
#     def __str__(self):
#         return"""
#         REFERENCIA:  {}
#         NOMBRE:      {}
#         PVP:         {}
#         DESCRIPCION: {}
#         ISBN:   {}
#         AUTOR:{}
#         """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)
        
# a= Adorno(2016,"Lego",15,"Juego para menores")  
# print(a) 
# al=Alimento(2018,"Cruton",12,"pan duro condimentado")
# al.productor="heinz"
# al.distribuidor="walmart"
# print(al)
# li= Libro(2018,"El principito",11,"libro pa nenios")
# li.isbn=23231
# li.autor="Yonas brothers"
# print(li)

# lista=[a,al,li]

# for e in lista:
#     if isinstance(e,Libro):
#         print(e.isbn,e.autor)
    
# #es importante mencionar que al hacer una copia de n objeto, si este es modificado tambien el 
# #objeto original se modificara

# #para copiar un objeto:
# import copy
# copia_li=copy.copy(li)

#en cuanto herencia multiple, un objeto hereda de dos clases siempre dando prioridad al mas a la 
#izquierda simepre

# class A:
#     def __init__(self):
#         print("Clase A")
#     def a(self):
#         print("metodo heredado de clase a")
# class B:
#     def __init__(self):
#         print("Clase B")
#     def b(self):
#         print("metodo heredado de clase b")

# class C(A,B):
#     def __init__(self):
#         print("Clase C")
#     def c(self):
#         print("metodo de clase c")
    
# num=C()
# num.a()
# num.b()
# num.c()

# class Automovil():
#     def __init__(self,color,ruedas):
#         self.color=color
#         self.ruedas=ruedas
#     def __str__(self):
#         return "Color: {}  Ruedas: {}".format(self.color,self.ruedas)

# class Coche(Automovil):
#     def __init__(self,color,ruedas,velocidad,cilindros):
#         Automovil.__init__(self,color,ruedas)
#         self.velocidad=velocidad
#         self.cilindros=cilindros
#     def __str__(self):
#         return Automovil.__str__(self) + "Velocidad: {} Cilindros: {}".format(self.velocidad,self.cilindros)

# yaris=Coche("rojo",4,200,4)
# print(yaris)

#ahora, usando super()

class Automovil():
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    def __str__(self):
        return "Color: {}  Ruedas: {}".format(self.color,self.ruedas)

class Coche(Automovil):
    def __init__(self,color,ruedas,velocidad,cilindros):
        super().__init__(color,ruedas)
        self.velocidad=velocidad
        self.cilindros=cilindros
    def __str__(self):
        return super().__str__() + " Velocidad: {} Cilindros: {}".format(self.velocidad,self.cilindros)


class Bicicleta(Automovil):
    def __init__(self,color,ruedas):
        super().__init__(color,ruedas)
        print("""
        Selecciona el tipo:
        1.-Urbana
        2.-Deportiva""")
        tipo=int(input())
        if tipo == 1:
            self.tipo="Urbana"
        elif tipo==2:
            self.tipo="Deportiva"
        else:
            self.tipo="Urbana"
    def __str__(self):
        return super().__str__() + " Tipo: {}".format(self.tipo)

class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindros,carga):
        super().__init__(color,ruedas,velocidad,cilindros)
        self.carga=carga
    def __str__(self):
        return super().__str__() + " Carga: {}".format(self.carga)

# class Motocicleta(Bicicleta, Coche):
#     def __init__(self,color,ruedas,velocidad,cilindros):
#         super(Bicicleta).__init__(color,ruedas)
#         super(Coche).__init__(color,ruedas,velocidad,cilindros)
#      def __str__(self):
#         return super(Bicicleta).__str__() + super(Coche).__str__()   

yaris=Camioneta("rojo",2,20,2,160)
print(yaris)