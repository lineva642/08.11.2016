class Vector:
    def __init__(self, x, y):
            self.x=x
            self.y=y
    def __str__(self):
        return str(self.x)+', ' + str(self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y + other.y)
a = Vector(2, 5)
b = Vector(3, 4)

print(str(a+b))
print(str(a-b))
