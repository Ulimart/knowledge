from multiprocessing.context import assert_spawning


edad = int(input('Escribe tu edad: '))
# siempre tiene que haber cuatro espacios despues de los dos puntos (:)
if edad >= 18:
    print('puedes pasar por chelas')
else:
    print('no puedes pasar por cheves')

numero = int(input('Escribe un numero: '))

if numero < 5:
    print('Es mayor a 5')
elif numero == 5:
    print('Es ingual a 5')
else:
    print('Es menor a 5')


