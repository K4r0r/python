def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number//2
            print(number)
        elif number % 2 == 1:
            number = 3*number+1
            print(number)
        if number == 1:
            print("Koniec")


try:
    firstNumber = int(input("Proszę podać początkową wartość: \n"))
    collatz(firstNumber)
except ValueError:
    print('Proszę podać prawidłową wartość')
