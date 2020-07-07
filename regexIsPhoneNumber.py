import re

phoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNum.search('Mój numer telefonu to 123-321-1234.')
print('Znaleziono numer telefonu ' + mo.group())
