average = 0
print("List of employees whose salaries are more than 20000: ")
with open("3.txt", "r") as file:
    persons = []
    for line in file:
        first_name, last_name, salary = line.split()
        persons.append(f"{first_name} {last_name}")
        if float(salary) > 20000:
            print(f"{first_name} {last_name}")
        average += float(salary)
print(f"Average income for all employees: {average/len(persons)}")