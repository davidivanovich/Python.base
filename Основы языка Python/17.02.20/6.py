a = int(input('Введите а - '))
b = int(input('Введите b - '))
day = 1
while a < b:
    a *= 1.1
    day += 1
print('На достижение таких результатов понадобится {} дней.'.format(day))

