from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, name, speed, doors):
        super().__init__(name, speed)
        self.doors = doors

    def describe(self):
        return f"{super().describe()} It has {self.doors} doors."


class Plane(Vehicle):
    def __init__(self, name, speed, wingspan):
        super().__init__(name, speed)
        self.wingspan = wingspan

    def describe(self):
        return f"{super().describe()} It has a wingspan of {self.wingspan} meters."


class Boat(Vehicle):
    def __init__(self, name, speed, length):
        super().__init__(name, speed)
        self.length = length

    def describe(self):
        return f"{super().describe()} It is {self.length} meters long."


class Race(Car):
    def __init__(self, name, speed, doors, turbo_speed):
        super().__init__(name, speed, doors)
        self.turbo_speed = turbo_speed

    def describe(self):
        return f"{super().describe()} It can boost to {self.turbo_speed} km/h with turbo."
