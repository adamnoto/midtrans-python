from midtrans import request
from datetime import datetime


def make_request():
    req = request.SnapChargeReq(
        order_id="ORD-SNP291",
        gross_amount=200000
    )
    return req


def exp_time(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")


def test_short_snap_request_body():
    req = make_request()
    serialized_req = {'transaction_details': {'order_id': 'ORD-SNP291', 'gross_amount': 200000}}
    assert req.serialize() == serialized_req


def test_snap_with_expiry_body():
    req = make_request()

    time = datetime.now()
    req.set_expiry_time(5, "minutes", time)
    serialized_req = {'transaction_details': {'order_id': 'ORD-SNP291', 'gross_amount': 200000},
                      'expiry': {'duration': 5, 'start_time': exp_time(time), 'unit': 'minutes'}}
    assert req.serialize() == serialized_req


def test_snap_complete_body():
    req = make_request()

    time = datetime.now()
    req.set_expiry_time(5, "day", time)

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

    req.whitelist_bins = ["48111", "45555"]
    req.secure = True
    req.channel = "migs"
    req.bank = "bca"
    req.set_installment(is_forced=True,
                        bni_terms=[3, 6, 12],
                        mandiri_terms=[3, 6, 12],
                        cimb_terms=[3],
                        bca_terms=[3, 6, 12],
                        offline_terms=[6, 12])

    serialized_req = {
        'credit_card': {
            'installment': {
                'required': True,
                'terms': {'offline': [6, 12],
                          'cimb': [3],
                          'bni': [3, 6, 12],
                          'mandiri': [3, 6, 12],
                          'bca': [3, 6, 12]}
            },
            'whitelist_bins': ['48111', '45555'],
            'secure': True, 'channel': 'migs'
        },
        'transaction_details': {'order_id': 'ORD-SNP291', 'gross_amount': 200000},
        'item_details': [{'price': 200000.0, 'id': 'ITEM-1', 'name': 'Ayam Bakar', 'quantity': 5}],
        'expiry': {'duration': 5, 'start_time': exp_time(time), 'unit': 'day'},
        'customer_details': {
            'first_name': 'Ivana', 'last_name': 'Jessica', 'phone': '08127323',
            'billing_address': {'city': 'Jakarta', 'first_name': 'Ivana', 'last_name': 'Jessica',
                                'phone': '08237132', 'postcode': '61177', 'country_code': 'IDN',
                                'address': 'Jalan Beton', 'email': 'iv@example.com'},
            'shipping_address': {'city': 'Bandung', 'first_name': 'Budi', 'last_name': 'Utomo',
                                 'phone': '081128371', 'postcode': '61155', 'country_code': 'IDN',
                                 'address': 'Sudirman', 'email': 'budi@utomo.com'},
            'email': 'ivana@jessica.com'}
    }
    assert req.serialize() == serialized_req