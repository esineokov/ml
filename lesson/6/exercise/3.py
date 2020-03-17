class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        if type(wage) != int or type(bonus) != int:
            raise Exception("wage and bonus should be integer")

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


hr = Position(name="Ivan", surname="Ivanov", position="hr", wage=50000, bonus=10000)
print(hr.get_full_name())
print(hr.position)
print(hr.get_total_income())

