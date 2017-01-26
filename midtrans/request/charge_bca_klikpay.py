from .core_charge_req import CoreChargeReq
from ..paysource import BCA_KLIKPAY


class ChargeBcaKlikpay(CoreChargeReq):
    """
    Charge request object for BCA Klikpay
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 klikpay_type=None,
                 description=None,
                 misc_fee=None):

        CoreChargeReq.__init__(
            self,
            payment_type=BCA_KLIKPAY,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.bca_klikpay = dict(description=description, type=klikpay_type)

        if misc_fee:
            self.misc_fee = int(misc_fee)

    @property
    def klikpay_type(self):
        return self.bca_klikpay["type"]

    @klikpay_type.setter
    def klikpay_type(self, value):
        self.bca_klikpay["type"] = value

    @property
    def description(self):
        return self.bca_klikpay["description"]

    @description.setter
    def description(self, value):
        self.bca_klikpay["description"] = value