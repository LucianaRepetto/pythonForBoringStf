print('Cuantos gatos tenes?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('Tenes demasiados gatos')
    else:
        print('No son tantos gatos')
except ValueError:
    print('No ingresaste un numero')  

#esto se hace porque en el if, passamos el valor texto del
#input a numero, por lo q si escriben "seis" va a saltar un
#error de valor. lo que hacemos es prevenir el error y alertar 
# a la persona q esta escribiendo validacion del input