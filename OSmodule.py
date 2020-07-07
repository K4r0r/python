import os

os.path.join('usr', 'bin', 'spam')

os.getcwd()

print(os.path.abspath('.'))

print(os.path.abspath('.\\Scripts'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows', 'C:\\'))

print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

path = 'C:\\Users\\Karor\\Documents\\python\\boringstuff\\pw.py'
print(os.path.basename(path))
print(os.path.dirname(path))

print(os.path.split(path))

print(os.path.getsize(path))

print(os.listdir('C:\\Users\\Karor\\Documents\\python\\boringstuff'))

print(os.path.exists(path))

print(os.path.isdir(path))
print(os.path.isdir('C:\\Users\\Karor\\Documents\\python\\boringstuff'))

print(os.path.isfile(path))
print(os.path.isfile('C:\\Users\\Karor\\Documents\\python\\boringstuff'))

#CD-ROM
print(os.path.exists('G:\\'))