string = input('Введите свои слова: ')
string = string.split()
n = 0
q = 1
while n != len(string):
 print(f'{q}: {string[n]}')
 n += 1
 q += 1

