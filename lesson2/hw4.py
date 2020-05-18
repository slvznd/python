userlist = input("Введите слова через пробел: ").split()
for i in range(len(userlist)):
    print(f"{i + 1}. {userlist[i][:10]}")
