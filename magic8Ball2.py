import random

messeges = [
    'To pewne',
    'Tak',
    'Niejasna odpowiedź. Spróbuj ponownie',
    'Zapytaj ponownie później',
    'Skoncetruj się i zapytaj ponownie',
    'Moja odpowiedź brzmi nie',
    'To nie wygląda zbyt dobrze',
    'Bardzo wątpliwe'
]

print(messeges[random.randint(0, len(messeges)-1)])