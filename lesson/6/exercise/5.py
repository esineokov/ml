class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером")


pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()