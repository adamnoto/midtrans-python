from .core_charge_req import CoreChargeReq
from ..paysource import CIMB_CLICKS


class CimbClickDetail(CoreChargeReq):
    """
    Charge request object for CIMB click
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 description=None):

        CoreChargeReq.__init__(
            self,
            payment_type=CIMB_CLICKS,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.description = description