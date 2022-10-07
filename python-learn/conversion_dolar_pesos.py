def conversor(tipo_moneda, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_moneda + " tienes?: ")
    pesos = float(pesos)
    dolar = pesos / valor_dolar
    dolares = round(dolar, 2)
    dolares = str(dolar)
    print('Tienes $' + dolares + ' dolares')


menu = """
Bienvenido al conversor de monedas 😎
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """
opcion = int(input(menu))
if opcion == 1:
    conversor("colombianos", 3040)
elif opcion == 2:
    conversor("Argeninos", 68)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opcion correcta")

