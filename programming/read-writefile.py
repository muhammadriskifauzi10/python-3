import os


os.system('cls')

f = open('assets/data1.txt', 'a')
f.write('\nI am learning to python opencv!')

f = open('assets/data1.txt', 'r')
print(f.read())