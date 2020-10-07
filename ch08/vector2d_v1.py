
from array import array

import math

class Vector2d:
    typecode = 'd'  #double

    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        #__iter__讓Vector2d變成可迭代;這是讓它可以拆解的原因
        return (i for i in (self.x,self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)
    def __str__(self):
        return str(tuple(self))
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode,self)))
    def __eq__(self,other):
        return tuple(self) == tuple(other)
    def __abs__(self):
        return math.hypot(self.x,self.y)
    def __bool__(self):
        return bool(abs(self))
    @classmethod #
    def frombytes(cls,octets):
        typecode = char(octets[0])    
        memv = memoryview(octect[1:]).cast(typecode)
        return cls(*memv0) 



