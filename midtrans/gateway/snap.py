from ..response import Response
from ..request import SnapChargeReq


class Snap:
    """
    Snap API gateway
    """

    def __init__(self, client):
        self.client = client

    def call(self, method, path, parameters=dict()):
        if not path[0] == "/":
            path = "/" + path

        url = self.client.environment_type.app_url + path
        json_resp = self.client.call(method, url, parameters)
        return response.SnapResponse(**json_resp)

    def get_token(self, snap_req):
        """
        Perform get token for charging with snap using SnapChargeReq
        :param snap_req: the snap charge request of type SnapChargeReq
        :return: the snap response object
        """

        return self.call("post", "snap/v1/transactions", snap_req.serialize())

    def get_token_quick(self, order_id, gross_amount):
        """
        Quickly get token without constructing the body manually
        :param order_id: the order id from the merchant's side
        :param gross_amount: the total gross amount for all items; including: taxes (if any), and discounts (if any)
        :return: the snap response object
        """

        snap_req = SnapChargeReq(order_id=order_id, gross_amount=gross_amount)
        return self.get_token(snap_req)
