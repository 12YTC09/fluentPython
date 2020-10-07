'''
特性1：
將class(類)的方法轉換為只能讀取的屬性

'''


class Bank_account1:
    @property
    def password(self):
        return '密碼:123'


'''
特性2：
重新實現一個屬性的setter,getter和deleter的使用範例
'''


class Bank_account2:
    def __init__(self):
        self._password = '預設密碼 0000'

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,value):
        self._password = value
    @password.deleter
        del self._password
        print('del complete')
