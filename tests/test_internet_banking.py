from midtrans import request


def add_item_and_cust_detail_to_req(req):
    req.add_item(request.ItemDetail(id=1, price=200000, name="Headset", quantity=1))
    req.customer_details = request.CustomerDetails(
        first_name="Adam",
        last_name="Pahlevi",
        email="adam@pahlevi.com",
        phone="0815623"
    )


def test_bca_klikpay():
    req = request.ChargeBcaKlikpay(
        order_id="ORD-BC23",
        gross_amount=200000,
        klikpay_type=1,
        description="Pembelian barang"
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'bca_klikpay': {'type': 1, 'description': 'Pembelian barang'},
                      'transaction_details': {'order_id': 'ORD-BC23', 'gross_amount': 200000},
                      'payment_type': 'bca_klikpay',
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req


def test_bca_klikbca():
    req = request.ChargeBcaKlikBca(
        order_id="ORD-BC929",
        gross_amount=200000,
        desc="Testing transaction",
        user_id="midtrans1012"
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'payment_type': 'bank_transfer',
                      'transaction_details': {'order_id': 'ORD-BC929', 'gross_amount': 200000},
                      'bca_klikbca': {'user_id': 'midtrans1012', 'desc': 'Testing transaction'},
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    print req.serialize()
    assert req.serialize() == serialized_req


def test_mandiri_clickpay():
    req = request.ChargeMandiriClickpay(
        order_id="ORD-MAN182",
        gross_amount=200000,
        card_number="4111111111111111",
        input1="1111111111",
        input2="145000",
        input3="54321",
        token="000000"
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'mandiri_clickpay': {'input2': '145000', 'input3': '54321', 'token': '000000',
                                           'input1': '1111111111', 'card_number': '4111111111111111'},
                      'transaction_details': {'order_id': 'ORD-MAN182', 'gross_amount': 200000},
                      'payment_type': 'mandiri_clickpay',
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam',
                                           'last_name': 'Pahlevi', 'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req


def test_epay_bri():
    req = request.ChargeEpayBri(
        order_id="ORD-BRI29",
        gross_amount=200000
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'transaction_details': {'order_id': 'ORD-BRI29', 'gross_amount': 200000},
                      'payment_type': 'bri_epay',
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req


def test_cimb_clicks():
    req = request.ChargeCimbClicks(
        order_id="ORD-CIM929",
        gross_amount=200000
    )

    req.description = "Purchase of a special event item"
    add_item_and_cust_detail_to_req(req)

    serialized_req = {'cimb_clicks': {'description': 'Purchase of a special event item'},
                      'transaction_details': {'order_id': 'ORD-CIM929', 'gross_amount': 200000},
                      'payment_type': 'cimb_clicks',
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req