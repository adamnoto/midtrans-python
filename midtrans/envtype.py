class EnvironmentType:
    def __init__(self):
        self.envname = ""
        self.api_url = ""
        self.app_url = ""

    def __repr__(self):
        return "EnvType: {0}".format(self.envname)

SANDBOX = EnvironmentType()
SANDBOX.envname = "SANDBOX"
SANDBOX.api_url = "https://api.sandbox.midtrans.com"
SANDBOX.app_url = "https://app.sandbox.midtrans.com"

PRODUCTION = EnvironmentType()
PRODUCTION.envname = "PRODUCTION"
PRODUCTION.api_url = "https://api.midtrans.com"
PRODUCTION.app_url = "https://app.midtrans.com"
