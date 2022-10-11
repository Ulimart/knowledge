pesos = input('¿Cuantos pesos Mexicanos tienes?: ')
pesos = float(pesos)
valor_dolar = 20.21
dolar = pesos / valor_dolar
dolares = round(dolar, 2)
dolares = str(dolar)
print('Tienes $' + dolares + ' dolares')