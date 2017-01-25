from ..serializable import Serializable


class CustAddress(Serializable):
    """
    Object representing the customer address
    """

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 phone,
                 address,
                 city,
                 postal_code,
                 country_code):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.postcode = postal_code
        self.country_code = country_code

    def __repr__(self):
        return "CustAddress('{0}')".format(self.first_name)
