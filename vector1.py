class Vector:
    def __init__(self, x, y):
        if type(x)== str:
            s=list(map(float(input().split(' '))))
            self.x=s[0]
            self.y=s[1]
        else:
            self.x = x
            self.y = y
    def __str__(self):
        return Vector(str(self.x),str(self.y))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __radd__(self, other):
        return Vector(self.y + other.y, self.x + other.x)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y + other.y)
    def __rsub__(self, other):
        return Vector(self.y - other.y, self.x - other.x)
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    def __rmul__(self, other):
        return Vector(self.y * other.y, self.x * other.x)
    def __abs__(self):
        return Vector(((self.x)**2+(self.y)**2)**0.5)
    def __truediv__(self, other):
        return Vector(self.x / other, self.y /other)
