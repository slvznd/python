userlist = input("Введите элементы через пробел: ").split()
indexcount = 1
print(f"Текущий список: {userlist}")
for i in range(len(userlist) // 2):
    userlist[indexcount], userlist[indexcount - 1] = userlist[indexcount - 1], userlist[indexcount]
    indexcount += 2
print(f"Новый список: {userlist}")
