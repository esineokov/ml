class OnlyNum(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Only numbers!"

    def __str__(self):
        return self.message


def check(text):
    try:
        return float(text) if "." in text else int(text)
    except Exception:
        raise OnlyNum()


data = []


while True:
    text = input("Next number: ")
    if text == "stop":
        break

    try:
        data.append(check(text))
    except OnlyNum as e:
        print(e)

print(f"Your numbers: {data}")

