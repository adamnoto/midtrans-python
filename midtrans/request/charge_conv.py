from .core_charge_req import CoreChargeReq
from ..paysource import CONV_STORE


class ChargeConvStore(CoreChargeReq):
    def __init__(self,
                 order_id,
                 gross_amount,
                 store=None,
                 message=None):

        CoreChargeReq.__init__(
            self,
            payment_type=CONV_STORE,
            order_id=order_id,
            gross_amount=gross_amount,
        )

        self.cstore = dict()
        self.store = store
        self.message = message

    @property
    def store(self):
        return self.cstore["store"]

    @store.setter
    def store(self, value):
        self.cstore["store"] = value

    @property
    def message(self):
        return self.cstore["message"]

    @message.setter
    def message(self, value):
        self.cstore["message"] = value


class ChargeIndomaretConvStore(ChargeConvStore):
    def __init__(self,
                 order_id,
                 gross_amount,
                 message=None):

        ChargeConvStore.__init__(
            self,
            order_id=order_id,
            gross_amount=gross_amount,
            store="Indomaret",
            message=message
        )


class ChargeKiosonConvStore(ChargeConvStore):
    def __init__(self,
                 order_id,
                 gross_amount,
                 message=None):

        ChargeConvStore.__init__(
            self,
            order_id=order_id,
            gross_amount=gross_amount,
            store="kioson",
            message=message
        )