
from array import array
import reprlib
import math
import numbers



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
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv  = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    def __len__(self):
        return len(self._components)
    def __getitem__(self,index):
        cls = type(index)
        if isinstance(index,slice):
            return cls(self._components[index])
        elif isinstance(index,numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))





















