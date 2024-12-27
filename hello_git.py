import b
import os

print('*** Hello, Git! ***')
print('Индексация - это важно')

ind = 0
sum = 0
s = []
while ind <= 9:
        sum += ind
        s.append(sum)
        ind += 1
print(s)
print(b.any_func(2, sum))
print(f'\nYour current directory: {os.getcwd()}')

s = 'Version Control System'
print(f'{s} - length is {len(s)} characters')

print('Hello from GitHub!')
