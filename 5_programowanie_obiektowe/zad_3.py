class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Dom: {self.address}, Powierzchnia: {self.area},"
                f" Pokoje: {self.rooms}, Cena: {self.price}, Działka: {self.plot}")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Mieszkanie: {self.address}, Powierzchnia: {self.area},"
                f" Pokoje: {self.rooms}, Cena: {self.price}, Piętro: {self.floor}")


house1 = House(150, 5, 850000, "ul. Lipowa 10", 600)
flat1 = Flat(60, 3, 450000, "ul. Długa 5/12", 2)

print(house1)
print(flat1)
