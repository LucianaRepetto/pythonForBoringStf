import random

print('Hola! como te llamas?')
name = input()
secretNumber = random.randint(0,20)
print('Hola, '+ name + ' estoy pensando en un numero entre 0 y 20')

#puede adivinar solo hasta 6 veces

for guessesTaken in range(1 ,7):
    print('Adivina...')
    guess = int(input())

    if guess < secretNumber:
        print('Muy bajo')
    elif guess > secretNumber:
        print('Muy alto')
    else:
        break #quiere decir q adivino correctamente
if guess == secretNumber:
    print('Bien '+ name+ '! Adivinaste mi numero en '+ str(guessesTaken) + ' partidas')
else: 
    print('No, el numero que pensaba era '+ str(secretNumber))