import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z     
        
    def __sub__(self, no):
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)
        
    def dot(self, no):
        #a*b=x1*x2+y1*y2+z1*z2
        #скалярное произведение
        return self.x * no.x + self.y * no.y + self.z * no.z
        
    def cross(self, no):
        #векторное произведение
        print(Point(self.y * no.z - self.z * no.y, self.z * no.x - self.x * no.z, self.x * no.y - self.y * no.x))
        return Point(self.y * no.z - self.z * no.y, self.z * no.x - self.x * no.z, self.x * no.y - self.y * no.x)
        
    def absolute(self):
        #длина вектора
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
def plane_angle(a, b, c, d):
    ab = b - a
    bc = c - b
    cd = d - c
    #векторное произведение 1. X
    x = ab.cross(bc)
    #векторное произведение 2. Y
    y = bc.cross(cd)
    
    abs_x = x.absolute()
    abs_y = y.absolute()
    
    if abs_x == 0 or abs_y == 0:
        return 0  
        
    cos_phi = x.dot(y) / (abs_x * abs_y)
    phi = math.acos(cos_phi)
    
    return math.degrees(phi)

if __name__ == '__main__':

    a = Point(int(input()), int(input()), int(input()))
    b = Point(int(input()), int(input()), int(input()))
    c = Point(int(input()), int(input()), int(input()))
    d = Point(int(input()), int(input()), int(input()))
    
    print(plane_angle(a, b, c, d))
