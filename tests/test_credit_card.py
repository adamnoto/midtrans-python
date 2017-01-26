from midtrans import request


def get_request():
    req = request.ChargeCreditCard(
        order_id="ORD-129",
        gross_amount=100000,
        token_id="MY-TOKEN"
    )
    return req


def test_credit_card_normal_charge_simple():
    req = get_request()
    serialized_req = {'transaction_details': {'order_id': 'ORD-129', 'gross_amount': 100000},
                      'payment_type': 'credit_card','credit_card': {'token_id': 'MY-TOKEN'}}

    assert req.serialize() == serialized_req


def test_credit_card_complete_body():
    req = get_request()

    req.add_item(request.ItemDetail(
        id="ITEM-1",
        price=200000,
        quantity=5,
        name="Ayam Bakar"
    ))

    req.customer_details = request.CustomerDetails(
        first_name="Ivana",
        last_name="Jessica",
        email="ivana@jessica.com",
        phone="08127323",
        billing_address=request.CustAddress(
            first_name="Ivana",
            last_name="Jessica",
            email="iv@example.com",
            phone="08237132",
            address="Jalan Beton",
            city="Jakarta",
            postal_code="61177",
            country_code="IDN"
        ),
        shipping_address=request.CustAddress(
            first_name="Budi",
            last_name="Utomo",
            email="budi@utomo.com",
            phone="081128371",
            address="Sudirman",
            city="Bandung",
            postal_code="61155",
            country_code="IDN"
        )
    )

    serialized_req = {'credit_card': {'token_id': 'MY-TOKEN'},
                      'transaction_details': {'order_id': 'ORD-129', 'gross_amount': 100000},
                      'payment_type': 'credit_card',
                      'item_details': [
                          {'price': 200000.0, 'id': 'ITEM-1', 'name': 'Ayam Bakar', 'quantity': 5}],
                      'customer_details': {'first_name': 'Ivana', 'last_name': 'Jessica', 'phone': '08127323',
                                           'billing_address': {'city': 'Jakarta', 'first_name': 'Ivana', 'last_name': 'Jessica', 'phone': '08237132', 'postcode': '61177', 'country_code': 'IDN', 'address': 'Jalan Beton', 'email': 'iv@example.com'},
                                           'shipping_address': {'city': 'Bandung', 'first_name': 'Budi', 'last_name': 'Utomo', 'phone': '081128371', 'postcode': '61155', 'country_code': 'IDN', 'address': 'Sudirman', 'email': 'budi@utomo.com'},
                                           'email': 'ivana@jessica.com'}}

    assert req.serialize() == serialized_req


def test_credit_card_with_bin_promo():
    req = get_request()
    req.set_bin_promo(["4811111", "bni", "5"])

    serialized_req = {'transaction_details': {'order_id': 'ORD-129', 'gross_amount': 100000}, 'payment_type': 'credit_card', 'credit_card': {'token_id': 'MY-TOKEN', 'bins': ['4811111', 'bni', '5']}}
    assert req.serialize() == serialized_req


def test_credit_card_with_installment_term():
    req = get_request()
    req.set_installment(12)

    serialized_req = {'transaction_details': {'order_id': 'ORD-129', 'gross_amount': 100000}, 'payment_type': 'credit_card', 'credit_card': {'token_id': 'MY-TOKEN', 'installment_term': 12}}
    assert req.serialize() == serialized_req


def test_credit_card_with_preauth():
    req = get_request()
    req.set_preauth()

    serialized_req = {'transaction_details': {'order_id': 'ORD-129', 'gross_amount': 100000}, 'payment_type': 'credit_card', 'credit_card': {'token_id': 'MY-TOKEN', 'type': 'authorize'}}
    assert req.serialize() == serialized_req


def test_saving_token_id():
    req = get_request()
    req.set_one_click()

    serialized_req = {'transaction_details': {'order_id': 'ORD-129', 'gross_amount': 100000}, 'payment_type': 'credit_card', 'credit_card': {'token_id': 'MY-TOKEN', 'save_token_id': True}}
    assert req.serialize() == serialized_req

    req.set_two_click()
    assert req.serialize() == serialized_req
