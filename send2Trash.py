import send2trash

baconFile = open('bacon.txt', 'a+')
baconFile.write('Bekon nie jest warzywem')
baconFile.close()

send2trash.send2trash('bacon.txt')