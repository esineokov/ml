offers = []
result = dict()

while True:
    name = str(input("название: "))
    price = int(input("цена: "))
    amount = int(input("количество: "))
    units = str(input("ед: "))

    offers.append((len(offers)+1, {"название": name, "цена": price, "количество": amount, "ед": units}))

    if input("Добавить еще? (y/n): ") == "y":
        continue
    else:
        break

for item in offers:
    for key, value in item[1].items():
        if key not in result:
            result[key] = set()
        result[key].add(value)

print(result)
