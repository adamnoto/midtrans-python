from .core_charge_req import CoreChargeReq
from ..paysource import CREDIT_CARD


class ChargeCreditCard(object):
    """
    Charge request object for credit card
    """

    def __init__(self,
                 order_id,
                 gross_amount,
                 token_id):

        CoreChargeReq.__init__(
            self,
            payment_type=CREDIT_CARD,
            order_id=order_id,
            gross_amount=gross_amount
        )

        self.credit_card = {
            token_id: token_id
        }

    def set_bin_promo(self, bank, bins):
        self.credit_card["bank"] = bank
        self.credit_card["bins"] = bins

    def set_installment(self, installment_term):
        self.credit_card["installment_term"] = installment_term

    def set_preauth(self, bank, type):
        self.credit_card["bank"] = bank
        self.credit_card["type"] = type

    def set_one_click(self, use_one_click):
        if use_one_click:
            self.credit_card["save_token_id"] = True
        else:
            self.credit_card.pop("save_token_id", None)

    def set_channel(self, channel):
        self.credit_card["channel"] = channel