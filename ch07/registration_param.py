
# -*- coding : utf-8 -*-
# 7-23 為了接受參數,新的register修飾器必須被當成函式來呼叫

registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active=%s) -> decorate(%s)' %(active,func))
        if active:
            registry.add(func)
        else:   
            registry.discard(func)
        return func
    return decorate #因為decorate是修飾器,所以它必須回傳一個函式

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')















