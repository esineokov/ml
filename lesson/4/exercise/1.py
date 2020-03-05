from sys import argv


def my_func(hours, rate, bonus=None):
    salary = hours*rate
    bonus = salary*0.3 if bonus is None else bonus
    return salary + bonus


if len(argv) < 3:
    print("Please enter the number of hours, rate and bonus (optional. 30% by default)")
else:
    try:
        print("Salary: {}".format(my_func(
            hours=float(argv[1]),
            rate=float(argv[2]),
            bonus=float(argv[3]) if len(argv) > 3 else None
        )))
    except:
        print("Please enter only digit params. Example: program.py 160 800 10000")