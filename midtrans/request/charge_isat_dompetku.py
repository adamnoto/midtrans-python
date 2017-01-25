from .core_charge_req import CoreChargeReq


class ChargeIndosatDompetku(CoreChargeReq):
    """
    Charge request object for Indosat Dompetku
    """
    def __init__(self, gross_amount, order_id, msisdn):
        CoreChargeReq.__init__(
            self,
            payment_type=INDOSAT_DOMPETKU,
            gross_amount=gross_amount,
            order_id=order_id
        )

        self.msisdn = msisdn