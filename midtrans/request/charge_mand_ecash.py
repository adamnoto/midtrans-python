from .core_charge_req import CoreChargeReq
from ..paysource import *


class ChargeMandiriEcash(CoreChargeReq):
    """
    Charge request object for Mandiri ECash
    """

    def __init__(self, gross_amount, order_id, description=None):
        CoreChargeReq.__init__(
            self,
            payment_type=MANDIRI_ECASH,
            gross_amount=gross_amount,
            order_id=order_id
        )

        self.mandiri_ecash = dict()

        if description is not None:
            self.description = description

    @property
    def description(self):
        return self.mandiri_ecash["description"]

    @description.setter
    def description(self, value):
        self.mandiri_ecash["description"] = value
