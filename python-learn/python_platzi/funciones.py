# Cuando tienes que repetir el mismo codigo muchas veces tienes que comenzar a usar funciones para poder evitar la repeticion de codigo

# print("Hola")
# print("Como estas?")
# print("Elegiste la opcion 1")
# print("Adios")

# print("Hola")
# print("Como estas?")
# print("Elegiste la opcion 2")
# print("Adios")

# print("Hola")
# print("Como estas?")
# print("Elegiste la opcion 3")
# print("Adios")

# Ejemplo 1
# def imprimir_mensaje():
#     print("Mesanje especial")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

####################################### Ejemplo 2
 #Este codigo a un que es funcional no es bueno trabajarlo asi porque estas repitiendo mucho codigo DRY

# opcion = int(input("Elige una opcion (1, 2, 3): "))
# if opcion == 1:
#     print("Hola")
#     print("Como estas?")
#     print("Elegiste la opcion 1")
#     print("Adios")
# elif opcion == 2:
#     print("Hola")
#     print("Como estas?")
#     print("Elegiste la opcion 2")
#     print("Adios")
# elif opcion == 3:
#     print("Hola")
#     print("Como estas?")
#     print("Elegiste la opcion 3")
#     print("Adios")

# Como los mensajes se parecen podemos usar funciones tambien 

# def conversacion(mensaje):
#     print("Hola")
#     print("Como estas?")
#     print(mensaje)
#     print("Adios")

# opcion = int(input("Elige una opcion (1, 2, 3): "))
# if opcion == 1:
#     conversacion("Elegiste la opcion 1")
# elif opcion == 2:
#     conversacion("Elegiste la opcion 2")
# elif opcion == 3:
#     conversacion("Elegiste la opcion 3")



# Ejemplo 3 
## Haciendo uso de Return, basicamente return puede regresar el valor de lo que estes trabajando en la funcion por ejemplo:

def suma(a, b):
    print("Sumatoria de dos numberos")
    resultado = a + b
    return resultado

sumatoria = suma(1,4)

print(sumatoria)
