from .cust_address import CustAddress
from ..serializable import Serializable


class CustomerDetails(Serializable):
    """
    Represent the customer detail
    """

    def __init__(self,
                 first_name,
                 last_name=None,
                 email=None,
                 phone=None,
                 billing_address=None,
                 customer_address=None):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

        if billing_address:
            self.billaddr = CustAddress(billing_address)

        if customer_address:
            self.shipaddr = CustAddress(billing_address)

    def __repr__(self):
        return "CustDetail('{0}')".format(self.first_name)