from decimal import *
from ..serializable import Serializable
getcontext().prec = 2


class ItemDetail(Serializable):
    """
    Represent the transaction details
    """

    def __init__(self,
                 id,
                 name,
                 price,
                 quantity):

        self.id = id
        self.name = name
        self.price = float(price)

        if quantity:
            self.quantity = int(quantity)