import sys
import os
import using_name

print ('Аргументы командной строки:')
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
for i in sys.argv:
    print(i)
    
print(sys.path,'\n')

print(os.getcwd())