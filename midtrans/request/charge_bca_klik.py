from .core_charge_req import CoreChargeReq
from ..paysource import BANK_TRANSFER


class ChargeBcaKlikBca(CoreChargeReq):
    """
    Charge request object for BCA Klikbca
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 desc=None,
                 user_id=None):

        CoreChargeReq.__init__(
            self,
            payment_type=BANK_TRANSFER,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.bca_klikbca = dict()

        self.desc = desc
        self.user_id = user_id

    @property
    def desc(self):
        return self.bca_klikbca["desc"]

    @desc.setter
    def desc(self, value):
        self.bca_klikbca["desc"] = value

    @property
    def user_id(self):
        return self.bca_klikbca["user_id"]

    @user_id.setter
    def user_id(self, value):
        self.bca_klikbca["user_id"] = value