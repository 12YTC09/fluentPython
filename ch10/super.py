
# -*- coding: UTF-8 -*-

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')
    def bar(self,message):
        parent("%s from Parent" %message)

class FooChild(FooParent):
    def __init__(self):
        #super(FooChild,self)首先找到FooChild的父類(FooParent),然後把類FooChild的對象轉換為類FooParent的對象
        super(FooChild,self).__init__()
        print('Child')
    def bar(self,message):
        super(FooChild,self).bar(message)
        print('Child bar function')
        print(self.parent)


if __name__ == '__main__':
    FooChild = FooChild()
    FooChild.bar('HelloWorld')




