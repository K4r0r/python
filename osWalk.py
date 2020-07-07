import os

for folderName, subfolders, filenames in os.walk('C:\\folderTestowy'):
    print('Katalog bieżący:' + folderName)

    for subfolder in subfolders:
        print('PODKATALOG KATALOGU ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('PLIK KATALOGU ' + folderName + ': ' + filename)
    print('')