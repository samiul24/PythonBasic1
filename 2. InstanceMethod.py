# [https://pynative.com/python-class-method/]

class Vehicle:
    def __init__(self, max_speed) -> None:
        self.max_speed = max_speed


class Car(Vehicle):
    def __init__(self, engine, max_speed) -> None:
        super().__init__(max_speed)
        self.engine = engine

    def display(self):
        print(self.max_speed)

v = Vehicle('3000 Km/h')
c = Car('Toyota', '3000 Km/h')
c.display()

iv = c.__dict__
print(iv)

for key, value in iv.items():
    print(f"Key: {key}, Value: {value}")

for key_value in iv.items():
    print(f"Key: {key_value[0]}, Value: {key_value[1]}")
