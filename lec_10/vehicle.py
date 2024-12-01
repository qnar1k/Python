class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def describe(self):
        return f"{self.name} travels at a speed of {self.speed} km/h."
