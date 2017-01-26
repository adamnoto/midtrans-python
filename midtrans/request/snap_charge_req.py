from trans_detail import TransactionDetail
from ..serializable import Serializable
from ..paysource import *
from ..banks import ALL_BANKS
from datetime import datetime


class SnapChargeReq(object, Serializable):
    """
    Construct the body for charging customers using snap
    """

    ALL_PAY_SOURCES = [
        CREDIT_CARD, MANDIRI_CLICKPAY, CIMB_CLICKS, KLIK_BCA, BCA_KLIKPAY,
        BRI_EPAY, TELKOMSEL_CASH, MANDIRI_ECHANNEL, BBM_MONEY, XL_TUNAI,
        INDOSAT_DOMPETKU, MANDIRI_ECASH, PERMATA_VA, BCA_VA, INDOMARET,
        KIOSON, GIFT_CARD_INDO
    ]

    def __init__(self,
                 order_id,
                 gross_amount,
                 enabled_payments=None,
                 customer_details=None):

        self.transaction_details = TransactionDetail(order_id=order_id, gross_amount=gross_amount)
        self.enabled_payments = enabled_payments
        self.customer_details = customer_details
        self.expiry = None
        self.credit_card = dict()
        self.item_details = None

    def add_item(self, item_detail):
        if self.item_details is None:
            self.item_details = []

        self.item_details.append(item_detail)

    def set_expiry_time(self, duration, unit, start_time=datetime.now()):
        if self.expiry is None:
            self.expiry = dict()

        if unit in ['day', 'hour', 'minute', 'days', 'hours', 'minutes']:
            self.expiry["unit"] = unit
        else:
            raise ValueError('Unacceptable unit')

        self.expiry['duration'] = int(duration)
        self.expiry['start_time'] = start_time.strftime("%Y-%m-%d %H:%M:%S")

        time_zone = start_time.strftime('%Z')
        if time_zone is not '':
            self.expiry['start_time'] += (" %{0}".format(time_zone))

    @property
    def save_card(self):
        return self.credit_card["save_card"]

    @save_card.setter
    def save_card(self, value):
        if value not in [True, False]:
            raise ValueError('Value must be boolean')

        self.credit_card["save_card"] = value

    @property
    def secure(self):
        return self.credit_card["secure"]

    @secure.setter
    def secure(self, value):
        if value not in [True, False]:
            raise ValueError('Value must be boolean')

        self.credit_card["secure"] = value

    @property
    def channel(self):
        return self.credit_card["channel"]

    @channel.setter
    def channel(self, value):
        self.credit_card["channel"] = value

    @property
    def bank(self):
        return self.credit_card["bank"]

    @bank.setter
    def bank(self, value):
        if value not in ALL_BANKS:
            self.credit_card["bank"] = value

    def set_installment(self,
                        is_forced,
                        bni_terms=None,
                        mandiri_terms=None,
                        cimb_terms=None,
                        bca_terms=None,
                        offline_terms=None):

        self.credit_card["installment"] = dict(required=is_forced, terms=dict())

        if type(bni_terms) is list: self.credit_card["installment"]["terms"]["bni"] = bni_terms
        if type(mandiri_terms) is list: self.credit_card["installment"]["terms"]["mandiri"] = mandiri_terms
        if type(cimb_terms) is list: self.credit_card["installment"]["terms"]["cimb"] = cimb_terms
        if type(bca_terms) is list: self.credit_card["installment"]["terms"]["bca"] = bca_terms
        if type(offline_terms) is list: self.credit_card["installment"]["terms"]["offline"] = offline_terms

    @property
    def whitelist_bins(self):
        return self.credit_card["whitelist_bins"]

    @whitelist_bins.setter
    def whitelist_bins(self, value):
        if type(value) is list:
            self.credit_card["whitelist_bins"] = value
        else:
            raise ValueError("Given value must be a list")

    def __repr__(self):
        return "Midtrans.Charge({0})".format(vars(self))