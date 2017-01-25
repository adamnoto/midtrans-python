from .core_charge_req import CoreChargeReq
from ..paysource import MANDIRI_ECHANNEL


class ChargeMandiriBill(CoreChargeReq):
    """
    Charge request object for Mandiri Bill (E-channel
    """

    def __init__(self, gross_amount, order_id, bill_info1=None, bill_info2=None):
        CoreChargeReq.__init__(
            self,
            payment_type=MANDIRI_ECHANNEL,
            gross_amount=gross_amount,
            order_id=order_id
        )

        if bill_info1 is not None or bill_info2 is not None:
            self.echannel = dict(bill_info1=bill_info1, bill_info2=bill_info2)
        else:
            self.echannel = None

    def add_bill_info(self, bill_info1, bill_info2):
        if self.echannel is None:
            self.echannel = dict()

        self.echannel["bill_info1"] = bill_info1
        self.echannel["bill_info2"] = bill_info2
