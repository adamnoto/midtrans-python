from .core_charge_req import CoreChargeReq
from ..paysource import XL_TUNAI


class ChargeXlTunai(CoreChargeReq):
    """
    Charge request object for Mandiri Clickpay
    """

    def __init__(self,
                 order_id,
                 gross_amount):

        CoreChargeReq.__init__(
            self,
            payment_type=XL_TUNAI,
            order_id=order_id,
            gross_amount=gross_amount
        )
