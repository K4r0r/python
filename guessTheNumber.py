#To jest gra typu "Odgarnij liczbę"
import random

secretNumber = random.randint(1,20)
print('Mam na myśli pewną liczbę z zakresu od 1 do 20.')

#Sześciokrotnie prosimy gracza o odgadnięcie liczby
for guessTaken in range(1,7):
    guess = int(input('Odgadnij liczbę w sześciu próbach: \n'))

    if guess < secretNumber:
        print('Podana liczba jest zbyt mała')
    elif guess > secretNumber:
        print('Podana liczba jest zbyt duża')
    else:
        break #Jeśli gracz odgadnie liczbę

if guess == secretNumber:
    print('Brawo zuchu! Odgadłeś liczbę w ciągu {} prób!'.format(guessTaken))
else:
    print('Nie udało się. Liczba, którą miałem na myśli to '+str(secretNumber))