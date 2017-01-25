from .core_charge_req import CoreChargeReq
from ..paysource import BCA_KLIKPAY


class ChargeBcaKlikpay(CoreChargeReq):
    """
    Charge request object for BCA Klikpay
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 type = None,
                 description = None,
                 misc_fee=None):

        CoreChargeReq.__init__(
            self,
            payment_type=BCA_KLIKPAY,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.type = type
        self.description = description

        if misc_fee:
            self.misc_fee = int(misc_fee)