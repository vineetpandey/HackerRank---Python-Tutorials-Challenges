# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x = self.x - no.x
        y = self.y - no.y
        z = self.z - no.z
        return Points(x, y, z)

    def dot(self, no):
        x = self.x * no.x
        y = self.y * no.y
        z = self.z * no.z
        return x + y + z

    def cross(self, no):
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Points(x, y, z)

    def absolute_scale(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), .5)


def solve(A, B, C, D):
    A, B, C, D = Points(*A), Points(*B), Points(*C), Points(*D)
    X = (B - A).cross(C - B)
    Y = (C - B).cross(D - C)
    angle = math.acos(X.dot(Y) / (X.absolute_scale() * Y.absolute_scale()))
    print "%.2f" % math.degrees(angle)

points = list()
for i in range(4):
    a = map(float, raw_input().split())
    points.append(a)
solve(*points)