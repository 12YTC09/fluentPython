
from array import array
import reprlib
import math



class Vector:
    typecode = 'd'
    
    def __init__(self,componts):
        #_:保護屬性
        self._components = array(self.typecode,componts)
    
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        print(components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components)) 

    def __eq__(self,other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls,octets):
















