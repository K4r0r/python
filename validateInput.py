while True:
    print('Podaj swój wiek: ')
    age = input()
    if age.isdecimal():
        break
    print('Wymagana liczba')

while True:
    print('Wprowadź nowe hasło (wyłącznik litery oraz cyfry): ')
    password = input()
    if password.isalnum():
        break
    print("Wymagane wyłącznie litery oraz cyfry")

