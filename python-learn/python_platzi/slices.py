# Slices o rebanadas en español basicamente es cuando tienes una cadena de texto y la puedes dividir
nombre = "Francisco"

"""Arranca desde el primer índice hasta llegar antes del 3° índice.
El resultado sería
("Fra")"""
print(nombre[0 : 3])

"""Va desde el principio hasta antes de llegar del 3° índice. Como no hay ningún parámetro en el primer lugar, se interpreta que arranca desde el principio. Recordemos que empezamos a contar desde cero como primer dígito.
El resultado sería
("Fra")"""
print (nombre[:3])

"""Arranca desde el índice 1 hasta llegar antes del 7.
El resultado sería
"rancis"
"""
print(nombre[1:7])

"""Arranca desde el índice 1 hasta llegar antes del 7, pero pasos de 2 en 2, ya que eso es lo que nos indica el 3er parámetro, el cual es 2.
El resultado sería
"rni"
"""
print(nombre[1:7:2])

"""Arranca desde el índice 1 hasta el final del string (al no haber ningún 2° parámetro, significa que va hasta el final), pero en pasos de 3 en 3.
El resultado sería
"rcc"
"""
print(nombre[1::3])

"""Al no haber parámetro en las 2 primeras posiciones, se interpreta que se arranca desde el inicio hasta el final, pero en pasos de 1 en 1 con la palabra al revés, porque es -1.
El resultado sería
"ocsicnarF"
"""
print(nombre[::-1])
