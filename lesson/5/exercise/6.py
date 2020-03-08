lessons = dict()
with open("6.txt", "r") as file:
    for line in file:
        name, data = line.split(": ")
        for d in data.split():
            if d != "—":
                lessons[name] = lessons.get(name, 0) + int(d.split("(")[0])
print(lessons)

