
# magic methods

# Typy

class Point2:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    #override
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
        # return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash([self.x, self.y])


def Point3(Point2):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self):
        return self._z

    def __eq__(self, other):
        pass

    def __hash_(self):
        pass


pa = Point2(1, 2)
pb = Point2(1, 1)


print(pa == pb)

pa.x = 'blbost'
pa.y = 'blbost'
print(pa.x)

#print(pa)
#print(dir(pa))


# operace 

def vector2_plus(lhs, rhs):
    """
    lhs/rhs jsou n-tice
    """
    (lhs[0] + rhs[0], lhs[1] + rhs[1])


