from .core_charge_req import CoreChargeReq
from ..paysource import MANDIRI_CLICKPAY


class MandiriClickpayDetail(CoreChargeReq):
    """
    Charge request object for Mandiri Clickpay
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 card_number,
                 input1,
                 input2,
                 input3,
                 token=None):

        CoreChargeReq.__init__(
            self,
            payment_type=MANDIRI_CLICKPAY,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.card_number = card_number
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
        self.token = token