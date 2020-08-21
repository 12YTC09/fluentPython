#-*- : coding: utf-8 -*-


class Order:
    def __init__(self,customer,cart,promotion=None):
        self.customer = customer
        self.cart  = list(cart)
        self.promotion = promotion

    def total(self)
