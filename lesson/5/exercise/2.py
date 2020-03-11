with open("2.txt", "r") as file:
    lines = file.readlines()
    print(f"File contains {len(lines)} lines")
    for i, line in enumerate(lines, 1):
        print(f"{i} line: {len(line.split())} word(s)")

