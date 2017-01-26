from midtrans import midtrans


def test_environment_type():
    assert midtrans.SANDBOX.envname == "SANDBOX"
    assert midtrans.SANDBOX.api_url == "https://api.sandbox.veritrans.co.id"
    assert midtrans.SANDBOX.app_url == "https://app.sandbox.veritrans.co.id"

    assert midtrans.PRODUCTION.envname == "PRODUCTION"
    assert midtrans.PRODUCTION.api_url == "https://api.veritrans.co.id"
    assert midtrans.PRODUCTION.app_url == "https://app.veritrans.co.id"