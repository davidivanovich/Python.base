my_list = [7, 5, 3, 3, 2]
n = int(input())
b = n
while b not in my_list:
    b -= 1
x = my_list.index(b)
my_list.insert(x, n)
print(my_list)
