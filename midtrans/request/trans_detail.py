from ..serializable import Serializable


class TransactionDetail(Serializable):
    """
    Representing the transaction detail object
    """

    def __init__(self, order_id, gross_amount):
        self.order_id = order_id
        self.gross_amount = int(gross_amount)