class Car:
    _directions = ("straight", "left", "right", "back")

    def __init__(self, speed, name, color, is_police=False):
        if type(speed) != int:
            raise ValueError("Please be careful on the road. Try again.")
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        self._move = False
        self._direction = "straight"

    def go(self):
        self._move = True

    def stop(self):
        self._move = False
        self.speed = 0

    def turn(self, direction):
        if direction not in self._directions:
            raise IndexError("It seems you are doing something wrong. You better call a taxi.")
        self._direction = direction

    def show_speed(self):
        print(self.speed)

    def set_speed(self, speed):
        if not self._move:
            raise Exception(f"Turn on your {self.__class__.__name__}")
        if type(speed) != int:
            raise ValueError("It seems you are doing something wrong. You better call a taxi.")
        self.speed = speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Over speed!")
        print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Over speed!")
        print(self.speed)


class SportCar(Car):
    def turbo(self):
        self.set_speed(999)


class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_police = True


tc = TownCar(60, "Ford Focus", "black")
wc = WorkCar(40, "Renault Logan", "white")
sc = SportCar(150, "BMW M4", "red")
pc = PoliceCar(100, "Subaru Forester", "golden")

print(f"{tc.name} {tc.color}")
tc.go()
tc.show_speed()
tc.set_speed(100)
tc.show_speed()
print("---------------------")

print(f"{wc.name} {wc.color}")
try:
    wc.set_speed(100)
except Exception as e:
    print(e)
print("---------------------")

sc.go()
sc.turbo()
sc.turn("right")
sc.stop()
print(f"{sc.name} speed is {sc.speed}")
print(f"{sc.name} is {'police' if sc.is_police else 'civilian'} car")
print("---------------------")

print(f"{pc.name} is {'police' if pc.is_police else 'civilian'} car")