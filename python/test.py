
print("hello World!")

my_list = []
for square in range(1, 11):
    squa = square ** 2
    my_list.append(squa)
print(my_list)

my_list.clear()

for square in range(1, 11):
    my_list.append(square ** 2)
print(my_list)

my_list.clear()

my_list = [square for square in range(1, 13, 2)]
print(my_list)

my_list.clear()

my_list = [square ** 2 for square in range(1, 13, 2)]
print(my_list)
