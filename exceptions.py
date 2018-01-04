#en un try catch, se puede utilizar un else en el caso de que el try se haya ejecutado de manera correcta
#el finally se ejecutara se cumpla o no el try catch
# while (True) :
#     try:
#         n=float(input("Ingrese el numero a operar:"))
#     except:
#         print("Ese no es un numero >:(. ")
#     else:
#         print("gracias UuUr")
#         break
#     finally:
#         print("fin del la iteracion")


# try:
#     n=float(input("Ingrese el numero a operar:"))
# except:
#     print("Ese no es un numero >:(. ")
# else:
#     print('to bien')

# try:
#     n=float(input("Ingrese el numero a operar:"))
# except ValueError:
#     print("El valor no es un numero")
# except TypeError:
#     print("No es del tipo esperado")
# except Exception as e:
#     print(type(e).__name__)
# else:
#     print('to bien')

#podemos usar la palabra raise para levantar una excepcion
# def agregar_una_vez(l,elemento):
#     try:
#         if elemento not in lista:
#             l.append(elemento)
#         else:
#             raise ValueError
#     except ValueError:
#         print("no se pueden repetir elementos en la lista")

