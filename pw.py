#! python3
#Menedżer haseł

import sys, pyperclip

PASSWORD = {'email': 'fFGhhrjrtj6H3dedfF',
            'blog': 'wr344hhw34vfWWf4',
            'facebook': 'f32f23ghhfdsDFDgg5g3gsdv'}

if len(sys.argv) < 2:
    print('Użycie: python pw.py [konto] - skopiowanie hasła wskazanego konta.')
    sys.exit()

account = sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Hasło do konta '+account+' zostało skopiowane do schowka.')
else:
    print('Nie istnieje konto o nazwie '+account+'.')