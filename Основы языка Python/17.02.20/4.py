number = int(input('Введите число - '))
biggest = 0
while number != 0:
    num = number % 10
    if num > biggest:
        biggest = num
    number //= 10
print(biggest)
