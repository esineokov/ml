import json

average = 0
data = []
firm_with_profit = 0
profit = 0
with open("7.txt", "r") as file_source, open("7.json", "w+") as file_target:
    for line in file_source:
        name, form, revenue, expenses = line.split()
        result = float(revenue)-float(expenses)
        data.append({name: result})
        if result > 0:
            firm_with_profit += 1
            profit += result
    data.append({'average_profit': profit/firm_with_profit})
    json.dump(data, file_target)

