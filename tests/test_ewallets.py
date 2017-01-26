from midtrans import request


def add_item_and_cust_detail_to_req(req):
    req.add_item(request.ItemDetail(id=1, price=200000, name="Headset", quantity=1))
    req.customer_details = request.CustomerDetails(
        first_name="Adam",
        last_name="Pahlevi",
        email="adam@pahlevi.com",
        phone="0815623"
    )


def test_telkomsel_cash_charge_body():
    req = request.ChargeTelkomselCash(
        order_id="ORD-TC2928",
        gross_amount=200000,
        promo=False,
        is_reversal="0",
        customer="9932710273"
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'payment_type': 'telkomsel_cash',
                      'transaction_details': {'order_id': 'ORD-TC2928', 'gross_amount': 200000},
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'telkomsel_cash': {'promo': False, 'customer': '9932710273', 'is_reversal': 0},
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req


def test_xltunai_charge_req():
    req = request.ChargeXlTunai(
        order_id="ORD-XLT28",
        gross_amount=200000
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'transaction_details': {'order_id': 'ORD-XLT28', 'gross_amount': 200000},
                      'payment_type': 'xl_tunai',
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req


def test_indosat_dompetku_charge_req():
    req = request.ChargeIndosatDompetku(
        order_id="ORD-IS9382",
        gross_amount=200000,
        msisdn="08123456789"
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'payment_type': 'indosat_dompetku',
                      'transaction_details': {'order_id': 'ORD-IS9382', 'gross_amount': 200000},
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'indosat_dompetku': {'msisdn': '08123456789'},
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req


def test_mandiri_ecash_charge_req():
    req = request.ChargeMandiriEcash(
        order_id="ORD-MN392",
        gross_amount=200000,
        description="Transaction Description"
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'mandiri_ecash': {'description': 'Transaction Description'},
                      'transaction_details': {'order_id': 'ORD-MN392', 'gross_amount': 200000},
                      'payment_type': 'mandiri_ecash', 'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}], 'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi', 'email': 'adam@pahlevi.com'}}
    print req.serialize()
    assert req.serialize() == serialized_req