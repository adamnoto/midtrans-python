from midtrans import request


def add_item_and_cust_detail_to_req(req):
    req.add_item(request.ItemDetail(id=1, price=200000, name="Headset", quantity=1))
    req.customer_details = request.CustomerDetails(
        first_name="Adam",
        last_name="Pahlevi",
        email="adam@pahlevi.com",
        phone="0815623"
    )


def test_indomaret_charge_body():
    req = request.ChargeIndomaretConvStore(
        order_id="ORD-IN2831",
        gross_amount=200000,
        message="Tiket1 transaction"
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'cstore': {'message': 'Tiket1 transaction', 'store': 'Indomaret'},
                      'transaction_details': {'order_id': 'ORD-IN2831', 'gross_amount': 200000},
                      'payment_type': 'cstore',
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req


def test_kioson_charge_body():
    req = request.ChargeKiosonConvStore(
        order_id="ORD-K2910",
        gross_amount=200000,
        message="Tiket 2 transaction"
    )

    add_item_and_cust_detail_to_req(req)

    serialized_req = {'cstore': {'message': 'Tiket 2 transaction', 'store': 'kioson'},
                      'transaction_details': {'order_id': 'ORD-K2910', 'gross_amount': 200000},
                      'payment_type': 'cstore',
                      'item_details': [{'price': 200000.0, 'id': 1, 'name': 'Headset', 'quantity': 1}],
                      'customer_details': {'phone': '0815623', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req
