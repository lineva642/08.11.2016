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

n=int(input())
a=[]
m=0
im=0
for i in range(n):
    a.append(Vector(input()))
    if float(abs(a[i])) > m:
        m=abs(a[i])
        im=i
print('Наибольшее расстояние:',a[im])


def cm(a):
    sum=Vector('0,0')
    for k in a:
        sum +=k
    return (sum/n)
print('Центр масс:',cm(a))
