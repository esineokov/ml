class MovingError(Exception):
    def __init__(self, message=None):
        self.message = message if message is not None else "Failed to move"

    def __str__(self):
        return self.message


class WareHouse:
    def __init__(self):
        self._storage = dict()
        print("Welcome to WareHouse")

    def add(self, *args):
        for equipment in args:
            self._storage[type(equipment)] = self._storage.get(type(equipment), [])
            equipment.position = 'WareHouse'
            print(f"{equipment} with barcode {equipment.barcode} was added to warehouse")
            self._storage[type(equipment)].append(equipment)

    def move_to(self, barcode, position):
        for eq_type, eq_list in self._storage.items():
            for equipment in eq_list:
                if equipment.barcode == barcode:
                    equipment.move_to(position)
                    print(f"{equipment} with barcode {equipment.barcode} was moved to {position}")
                    return
            else:
                raise MovingError()

    @property
    def common_weight_in_storage(self):
        return sum(
            [float(eq.weight)
             for eq_type, eq_list in self._storage.items()
             for eq in eq_list if eq.position == "WareHouse"]
        )


class OfficeEquipment:
    def __init__(self, weight, height, width, length, barcode):
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length
        self.barcode = barcode
        self.position = None

    def move_to(self, position):
        self.position = position

    def __str__(self):
        return self.__class__.__name__


class Printer(OfficeEquipment):
    def __init__(self, print_speed, is_color, is_wifi, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.print_speed = print_speed
        self.is_color = is_color
        self.is_wifi = is_wifi


class Scanner(OfficeEquipment):
    def __init__(self, dpi, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dpi = dpi


class Xerox(OfficeEquipment):
    def __init__(self, dpi, copy_speed, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dpi = dpi
        self.copy_speed = copy_speed


p1 = Printer(
    weight=15, height=20, width=19, length=17, barcode=3456789765, print_speed=15, is_color=True, is_wifi=True
)
p2 = Printer(
    weight=20, height=25, width=16, length=37, barcode=8768722222, print_speed=10, is_color=False, is_wifi=True
)
p3 = Printer(
    weight=11, height=21, width=14, length=66, barcode=9287398273, print_speed=55, is_color=False, is_wifi=False
)
s1 = Scanner(weight=33, height=22, width=9, length=66, barcode=1112232323, dpi=250)
s2 = Scanner(weight=29, height=25, width=19, length=77, barcode=9887878788, dpi=300)

x = Xerox(weight=65, height=34, width=17, length=65, barcode=7783534536, dpi=300, copy_speed=150)

wh = WareHouse()
wh.add(p1, p2, p3)
wh.add(s1, s2)
wh.add(x)

print(f"Total weight equipment in warehouse: {wh.common_weight_in_storage}")

wh.move_to(barcode=3456789765, position="new_office")
print(f"Total weight equipment in warehouse now: {wh.common_weight_in_storage}")

try:
    wh.move_to(1, "unknown")
except MovingError as e:
    print(e)

