s = 0
stop = False
while True:
    a = input("Enter number(s) or 'q' for exit: ")
    for i in a.split():
        try:
            i = int(i)
            s += i
        except:
            if i == "q":
                stop = True
                break
            else:
                print(f"{i} is not number")
    print(s)
    if stop:
        print("Good bye!")
        break

