from .core_charge_req import CoreChargeReq
from ..paysource import BRI_EPAY


class ChargeEpayBri(CoreChargeReq):
    """
    Charge request object for Epay of BRI
    """

    def __init__(self,
                 order_id,
                 gross_amount):

        CoreChargeReq.__init__(
            self,
            payment_type=BRI_EPAY,
            order_id=order_id,
            gross_amount=gross_amount
        )

