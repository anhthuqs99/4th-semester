from rotation import *

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
FOG_COLOR = (239, 255, 227)
RAIN_COLOR = (102, 178, 255)

WIDTH = 800
HEIGHT = 600


class vertex:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def show(self):
        print(self.x, self.y, self.z)
    def scale(self, zoom):
        self.x *= zoom
        self.y *= zomm
        self.z *= zoom
    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz
    def rotate(self,tetaX, tetaY, tetaZ):
        self.x, self.y, self.z = rotate_vertex(self.x, self.y, self.z, tetaX, tetaY, tetaZ)

class vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def length(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    def show(self):
        print(self.x, self.y, self.z)
# Scalar product 2 vector
def scalar_mul(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
#Get cross product 2 vector (vector multiplication)
def vector_mul(v1, v2):
    res = vector()
    res.x = v1.y * v2.z - v1.z * v2.y
    res.y = v1.z * v2.x - v1.x * v2.z
    res.z = v1.x * v2.y - v1.y * v2.x
    return res
# Get normal of surface
def get_normal(v, num):
    a, b, c = 0, 0, 0
    for i in range(-1, num - 1):
        a += (v[i].y - v[i + 1].y) * (v[i].z + v[i + 1].z)
        b += (v[i].z - v[i + 1].z) * (v[i].x + v[i + 1].x)
        c += (v[i].x - v[i + 1].x) * (v[i].y + v[i + 1].y)
    
    return vector(a, b, c)
def cos_vector(v1, v2):
    return abs(scalar_mul(v1, v2) / (v1.length() * v2.length()))

class polygon:
    def __init__(self, vertexs, locaiton, color):
        self.vertexs = vertexs
        self.location = location
        self.color = color
    def show(self):
        for ver in self.vertexs:
            ver.show()

class object:
    def __init__(self, polygons, location, color):
        # for polygon in polygons:
        #     for ver in polygon:
        #         ver.x += location[0]
        #         ver.y += location[1]
        #         ver.z += location[2]
        res = []
        for polygon in polygons:
            sur = []
            for ver in polygon:
                x, y, z = ver.x + location[0], ver.y + location[1], ver.z + location[2]
                sur.append(vertex(x, y, z))
            res.append(sur)
        self.polygons = res
        self.location = location
        self.color = color

    def show(self):
        for polygon in self.polygons:
            for ver in polygon:
                ver.show()
    def rotate(self, xc, yc, zc, tetaX, tetaY, tetaZ):
        res = []
        for polygon in self.polygons:
            sur = []
            for ver in polygon:
                x, y, z = rotate_vertex(ver.x, ver.y, ver.z, xc, yc, zc, tetaX, tetaY, tetaZ)
                sur.append(vertex(x, y, z))
            res.append(sur)
        self.polygons = res
