'''
@classmethod:裝飾的類方法
@staticmethod:裝飾的靜態方法
'''


class A(object):
    def m1(self,n):
        print("self:",self)
        self.m2(n)

    @classmethod
    def m2(cls,n):
        print("cls:",cls)

    @staticmethod
    def m3(n):
        pass





