#A-3 顯示雜湊值的各種位元模式


import sys

#'b':Binary format

MAX_BITS = len(format(sys.maxsize,'b'))
print('%s- bit Python build' %(MAX_BITS+1))


def hash_diff(o1,o2):
    h1 = '{:>0{}b}'.format(hash(o1),MAX_BITS)
    print(h1)
    h2 = '{:>0{}b}'.format(hash(o2),MAX_BITS)
    print(h2)
    #diff = ''.join('!' if b1 != b2 else ' ' for b1,b2 in zip(h1,h2))
    #count = '!={}'.format(diff.count('!'))
    



if __name__=='__main__':
    print(hash_diff(1,1.0))




