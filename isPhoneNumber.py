def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# print('111-222-3333 to jest numer telefonu:')
# print(isPhoneNumber('111-222-3333'))
# print('Moshi moshi to jest numer telefonu:')
# print(isPhoneNumber('Moshi moshi'))

message = 'Zadzwoń pod numer 111-222-3333 po przerwie. 111-333-4444\
to moje biuro.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Znaleziono numer telefonu: ' + chunk)
print('Gotowe!')
