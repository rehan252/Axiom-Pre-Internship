"""
Problem: Write two classes Bus, LuxuryBus that inherits from Vehicle which will have function fare. but LuxuryBus will
charge 30% extra fare than regular Bus. regular bus fare will it's capacity * 250
"""


class Vehicle:
    def __init__(self, model, mileage, capacity):
        self.model = model
        self.mileage = mileage
        self.capacity = capacity
        self.charges = 250

    def fare(self):
        return self.capacity * self.charges


class Bus(Vehicle):
    pass


regular_bus = Bus('Hino', '10km/l', 45)
print(regular_bus.fare())

# Creating a Luxury Bus


class LuxuryBus(Vehicle):
    def fare(self):
        return self.capacity * (self.charges*30/100 + self.charges)


luxury_bus = LuxuryBus('Youtong', '8km/l', 45)
print(luxury_bus.fare())










