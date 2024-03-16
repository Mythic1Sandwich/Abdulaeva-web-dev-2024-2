import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Point(self.y * no.z - self.z * no.y, self.z * no.x - self.x * no.z, self.x * no.y - self.y * no.x)

    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


def plane_angle(a, b, c, d):
    ab = b - a
    bc = c - b
    cd = d - c

    x = ab.cross(bc)
    y = bc.cross(cd)

    abs_x = x.absolute()
    abs_y = y.absolute()

    if abs_x == 0 or abs_y == 0:
        return 0

    cos_phi = x.dot(y) / (abs_x * abs_y)
    if cos_phi > 1:
        cos_phi = 1
    elif cos_phi < -1:
        cos_phi = -1
    phi = abs(math.acos(cos_phi))  # модуль угла

    return round(math.degrees(phi),0)



if __name__ == '__main__':
    points = [list(map(int, input().split())) for i in range(4)]
    a, b, c, d = [Point(*point) for point in points]

    print(plane_angle(a, b, c, d))
