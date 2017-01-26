from .core_charge_req import CoreChargeReq
from ..paysource import MANDIRI_CLICKPAY


class ChargeMandiriClickpay(CoreChargeReq):
    """
    Charge request object for Mandiri Clickpay
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 card_number=None,
                 input1=None,
                 input2=None,
                 input3=None,
                 token=None):

        CoreChargeReq.__init__(
            self,
            payment_type=MANDIRI_CLICKPAY,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.mandiri_clickpay = dict()

        self.card_number = card_number
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
        self.token = token


    @property
    def card_number(self):
        return self.mandiri_clickpay["card_number"]

    @card_number.setter
    def card_number(self, value):
        self.mandiri_clickpay["card_number"] = str(value)

    @property
    def input1(self):
        return self.mandiri_clickpay["input1"]

    @input1.setter
    def input1(self, value):
        self.mandiri_clickpay["input1"] = str(value)

    @property
    def input2(self):
        return self.mandiri_clickpay["input2"]

    @input2.setter
    def input2(self, value):
        self.mandiri_clickpay["input2"] = str(value)

    @property
    def input3(self):
        return self.mandiri_clickpay["input3"]

    @input3.setter
    def input3(self, value):
        self.mandiri_clickpay["input3"] = str(value)

    @property
    def token(self):
        return self.mandiri_clickpay["token"]

    @token.setter
    def token(self, value):
        self.mandiri_clickpay["token"] = value
