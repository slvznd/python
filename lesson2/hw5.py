my_list = [9, 7, 5, 5, 3]
new_item = int(input("Введите новое число: "))
print(my_list)
for i in range(len(my_list)):
    if new_item > my_list[i]:
        my_list.insert(i, new_item)
        break
    elif new_item == my_list[i]:
        my_list.insert(i + my_list.count(new_item), new_item)
        break
    elif i == len(my_list) - 1:
        my_list.append(new_item)
print(my_list)
