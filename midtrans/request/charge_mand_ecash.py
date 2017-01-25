from .core_charge_req import CoreChargeReq
from ..paysource import *


class ChargeMandiriEcash(CoreChargeReq):
    """
    Charge request object for Mandiri ECash
    """

    def __init__(self, gross_amount, order_id, desc):
        CoreChargeReq.__init__(
            self,
            payment_type=MANDIRI_ECASH,
            gross_amount=gross_amount,
            order_id=order_id
        )

        self.description = desc
