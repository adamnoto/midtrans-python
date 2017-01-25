from .core_charge_req import CoreChargeReq
from ..paysource import BANK_TRANSFER


class ChargeBcaKlik(CoreChargeReq):
    """
    Charge request object for BCA Klikbca
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 desc=None,
                 user_id=None):

        CoreChargeReq.__init__(
            self,
            payment_type=BANK_TRANSFER,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.desc = desc
        self.user_id = user_id
