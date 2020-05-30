class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, txt=None):
        self.txt = "Can not be divided by zero" if txt is None else txt


while True:
    try:
        first = float(input("Enter first num: "))
        second = float(input("Enter Second num: "))

        if int(second) == 0:
            raise MyZeroDivisionError()

        print(f"Result: {first/second}\n")
    except MyZeroDivisionError as e:
        print(e.txt)
    except Exception as e:
        print(e)
