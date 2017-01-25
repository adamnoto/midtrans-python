from .core_charge_req import CoreChargeReq


class ChargeConvStoreDetail(CoreChargeReq):
    """
    Charge request object for convenient store
    """

    def __init__(self, gross_amount, order_id, store, message):
        CoreChargeReq.__init__(
            self,
            payment_type=CONV_STORE,
            gross_amount=gross_amount,
            order_id=order_id
        )

        self.store = store
        self.message = message