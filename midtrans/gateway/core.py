from midtrans import response


class Core:
    """
    Core API gateway
    """

    def __init__(self, client):
        self.client = client

    def call(self, method, path, parameters=dict()):
        if not path[0] == "/":
            path = "/" + path

        url = self.client.environment_type.api_url + path
        json_resp = self.client.call(method, url, parameters)
        return response.Response(**json_resp)

    def charge(self, charge_request):
        return self.call("post", "v2/charge", charge_request.serialize())

    def capture(self, charge_request):
        return self.call("post", "v2/capture", charge_request.serialize())

    def approve(self, order_id):
        return self.call("post", "v2/" + order_id + "/approve")

    def cancel(self, order_id):
        return self.call("post", "v2/" + order_id + "/cancel")

    def expire(self, order_id):
        return self.call("post", "v2/" + order_id + "/expire")

    def status(self, order_id):
        return self.call("get", "v2/" + order_id + "/status")