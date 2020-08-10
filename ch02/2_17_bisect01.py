#2-17  bitsect在已排序的序列中尋找項目的插入點
#bisect:Array bisection algorithm(陣列二分演算法)

import bisect
import sys

HAYSTACK = [1,4,5,6,8,12,15,20,21,23,,23,26,29,30]
NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]

ROW_FMT = '{0:2d}@{1:2d}  {2}{0:<2d}'
                
                
def demo(bisect_fn):
