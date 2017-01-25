from .core_charge_req import CoreChargeReq
from ..paysource import BANK_TRANSFER
from ..banks import *


class ChargeBankTransfer(CoreChargeReq):
    """
    Charge request object for all Bank Transfers (BCA, Permata, Mandiri Bill)
    """

    def __init__(self,
                 order_id,
                 gross_amount,

                 # permata and bca use this
                 bank = None):

        CoreChargeReq.__init__(
            self,
            payment_type=BANK_TRANSFER,
            gross_amount=gross_amount,
            order_id=order_id
        )

        if bank == BCA or bank == PERMATA:
            self.bank_transfer = dict(bank=bank)

        # for bca va
        self._va_number = None

    @property
    def va_number(self):
        return self._va_number

    @va_number.setter
    def va_number(self, value):
        if self.bank_transfer is None:
            self.bank_transfer = dict()
        self.bank_transfer["va_number"] = value

    def add_bca_inquiry_texts(self, indonesian_text, english_text):
        if self.bank_transfer is None:
            self.bank_transfer = dict()

        if self.bank_transfer.has_key("free_text") is False:
            self.bank_transfer["free_text"] = dict()

        self.bank_transfer["free_text"]["inquiry"] = [dict(id=indonesian_text, en=english_text)]

    def add_bca_payment_text(self, indonesian_text, english_text):
        if self.bank_transfer is None:
            self.bank_transfer = dict()

        if self.bank_transfer.has_key("free_text") is None:
            self.bank_transfer["free_text"] = dict()

        self.bank_transfer["free_text"]["payment"] = [dict(id=indonesian_text, en=english_text)]