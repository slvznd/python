counts = int(input("Сколько позиций хотим ввести? "))
data_container = list()
data_lib = dict()

for i in range(counts):
    print(f"Введите данные для {i + 1} позиции")
    data_lib.update({
        "название": input("Название: "),
        "цена": int(input("Цена: ")),
        "количество": int(input("Количество: ")),
        "ед": input("Единицы хранения: "),
    })
    data_container.append((i + 1, data_lib))
    data_lib = {}

print(f"Текущий склад: {data_container}")

data_lab = ["название", "цена", "количество", "ед"]
data_new = {}
temp = []
for k in range(len(data_lab)):
    for i in range(len(data_container)):
        temp += [data_container[i][1].get(data_lab[k])]
    data_new.update({data_lab[k]: temp})
    temp = []
print(f"Результат анализа: {data_new}")
