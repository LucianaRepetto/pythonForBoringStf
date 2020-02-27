def hello():
     print("Hola")
     print("como estas?")
     print("hola hola")

hello()
hello() 
# sirven para armar funciones que ejecuten 
#codigo que necesitamo ejecutar varias veces
#sin tener q hace copy paste del mismo codigo varias veces
#hay q intentar nunca repetir codigo para poder mantenerlo facilmente
# y que sea mas fácil para q otros lo lean

def hello(name):
     print("Hola " + name)
     
hello("Alice")
hello("Bob") 

####

def plusOne(number):
     return number + 1

newNumber = plusOne(5)
print(newNumber)


#las funciones son como mini programas dentro de mi programa
#su funcion principal es eliminar codigo repetido
#el input de las funciones son argumentos, el output es el valor de return
#los parametros son las variables entre los parentesis de las funciones 
# en el def statement
# toda funcion tiene un valor de return. si no se la especifica, su valor default es None
# 