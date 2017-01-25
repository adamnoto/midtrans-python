class EnvironmentType:
    def __init__(self):
        self.envname = ""
        self.api_url = ""
        self.app_url = ""

    def __repr__(self):
        return "EnvType: {0}".format(self.envname)

SANDBOX = EnvironmentType()
SANDBOX.envname = "SANDBOX"
SANDBOX.api_url = "https://api.sandbox.veritrans.co.id"
SANDBOX.app_url = "https://app.sandbox.veritrans.co.id"

PRODUCTION = EnvironmentType()
PRODUCTION.envname = "PRODUCTION"
PRODUCTION.api_url = "https://api.veritrans.co.id"
PRODUCTION.app_url = "https://app.veritrans.co.id"
