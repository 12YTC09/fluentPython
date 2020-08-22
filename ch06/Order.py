# -*-  coding: utf-8 -*-

#6-1實做Order類別

from abc import ABC,abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer','name fidelity')

class LineItem:

    def __init__(self,product,quantity,price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order: #context
    def __init__(self,customer,cart,promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion 
    def total(self):
        if not hasattr(self,'__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount 
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(),self.due())

class Promotion(ABC):  #Strategy: 一個抽象基礎類別
    @abstractmethod
    def discount(self,order):
        """Return discount as a positive dollar amount"""

class FidelityPromo(Promotion): #第一個Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""
    def discount(self,order):
        return order.total() *.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion): #第二個Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""
    def discount(self,order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total *.1
        return discount

class LargeOrderPromo(Promotion):  #第三個Concrete Strategy
    """"""
    def discount(self,order):
        discount_items = {item.product for item in order.cart}
        if len(discount_items) >= 10:
            return order.total() * .07
        return 0












