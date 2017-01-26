from .core_charge_req import CoreChargeReq
from ..paysource import TELKOMSEL_CASH


class ChargeTelkomselCash(CoreChargeReq):
    """
    Charge request object for Telkomsel Cash
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 promo=None,
                 is_reversal=None,
                 customer=None):

        CoreChargeReq.__init__(
            self,
            payment_type=TELKOMSEL_CASH,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.telkomsel_cash = dict()

        self.promo = promo
        self.is_reversal = is_reversal
        self.customer = customer

    @property
    def promo(self):
        return self.telkomsel_cash["promo"]

    @promo.setter
    def promo(self, value):
        self.telkomsel_cash["promo"] = value

    @property
    def is_reversal(self):
        return self.telkomsel_cash["is_reversal"]

    @is_reversal.setter
    def is_reversal(self, value):
        self.telkomsel_cash["is_reversal"] = int(value)

    @property
    def customer(self):
        return self.telkomsel_cash["customer"]

    @customer.setter
    def customer(self, value):
        self.telkomsel_cash["customer"] = value