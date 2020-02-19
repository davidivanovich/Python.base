time = int(input('Пожалуйста, введите время в секундах - '))
hours = time // 3600
min = time % 3600 // 60
sec = time % 3600 % 60
print('{}:{}:{}'.format(hours, min, sec))

