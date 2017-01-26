from .core_charge_req import CoreChargeReq
from ..paysource import CIMB_CLICKS


class ChargeCimbClicks(CoreChargeReq):
    """
    Charge request object for Epay of BRI
    """

    def __init__(self,
                 order_id,
                 gross_amount):

        CoreChargeReq.__init__(
            self,
            payment_type=CIMB_CLICKS,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.cimb_clicks = {}

    @property
    def description(self):
        return self.cimb_clicks["description"]

    @description.setter
    def description(self, value):
        self.cimb_clicks["description"] = value

