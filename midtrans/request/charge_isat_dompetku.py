from .core_charge_req import CoreChargeReq
from ..paysource import INDOSAT_DOMPETKU


class ChargeIndosatDompetku(CoreChargeReq):
    """
    Charge request object for Indosat Dompetku
    """

    def __init__(self, gross_amount, order_id, msisdn=None):
        CoreChargeReq.__init__(
            self,
            payment_type=INDOSAT_DOMPETKU,
            gross_amount=gross_amount,
            order_id=order_id
        )

        self.indosat_dompetku = dict()

        if msisdn is not None:
            self.msisdn = msisdn

    @property
    def msisdn(self):
        return self.indosat_dompetku["msisdn"]

    @msisdn.setter
    def msisdn(self, value):
        self.indosat_dompetku["msisdn"] = value
