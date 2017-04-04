from .trans_detail import TransactionDetail
from ..serializable import Serializable


class CoreChargeReq(object, Serializable):
    """
    Core charge request, you should not use this class other than for
    the purpose of subclassing. Use the specific class for the payment
    type to use, instead.
    """

    def __init__(self,
                 payment_type,
                 order_id,
                 gross_amount,
                 customer_details=None,
                 custom_field1=None,
                 custom_field2=None,
                 custom_field3=None):

        self.payment_type = payment_type
        self.transaction_details = TransactionDetail(order_id=order_id, gross_amount=gross_amount)
        self.item_details = None
        self.custom_field1 = custom_field1
        self.custom_field2 = custom_field2
        self.custom_field3 = custom_field3
        self.customer_details = customer_details

    def add_item(self, item_detail):
        if self.item_details is None:
            self.item_details = []

        self.item_details.append(item_detail)

    def __repr__(self):
        return "Midtrans.Charge({0})".format(vars(self))
