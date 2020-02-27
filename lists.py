spam = ['cat', 'bat', 'rat'] #es una lista con valores.
#para ingresar a un valor, tenemos q usar el indice entre brackets
spam[0]#cat

#las listas tmp pueden tener listas como valores.
#se ingresa a los valores con multiples indices
variable = [['cat', 'bat'], [1,2,3,4,5]]

variable[0] #['cat', 'bat']
variable[0][1] #'bat'
variable[1] #[1,2,3,4,5]
variable[1][3]# '4'

#slice nos trae una parte de una lista, pero como una lista nueva
#no incluye el indice del numero final. 
#se puede almacenar en otra variable para tener una nueva lsta
animales = ['cat', 'bat', 'rat','elephant']
animales[1:3] # ['bat','rat']

#puedo utilizar los indices para asignar un nuevo valor
numeros = [10,20,30]
numeros[1]="Hola" #[10, 'Hola', 30]
#con slice tmb puedo cambiar los valores

#puedo borrar elementos
animal = ['cat', 'bat', 'rat','elephant']
del animal[2] #['cat', 'bat', elephant']