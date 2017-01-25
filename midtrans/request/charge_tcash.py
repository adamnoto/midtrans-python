from .core_charge_req import CoreChargeReq
from ..paysource import TELKOMSEL_CASH


class ChargeTelkomselCash(CoreChargeReq):
    """
    Charge request object for Telkomsel Cash
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 promo,
                 is_reversal,
                 customer):

        CoreChargeReq.__init__(
            self,
            payment_type=TELKOMSEL_CASH,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.promo = promo
        self.is_reveral = int(is_reversal)
        self.customer = customer