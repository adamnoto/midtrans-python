from midtrans import request
from midtrans import banks


def test_permata_va():
    req = request.ChargeBankTransfer(
        order_id="ORD-123",
        gross_amount=250000,
        bank=banks.PERMATA
    )

    serialized_req = {'bank_transfer': {'bank': 'permata'}, 'payment_type': 'bank_transfer', 'transaction_details': {'gross_amount': 250000, 'order_id': 'ORD-123'}}

    assert req.serialize() == serialized_req


def test_bca_va():
    req = request.ChargeBankTransfer(
        order_id="ORD-1234",
        gross_amount=500000,
        bank=banks.BCA
    )

    req.customer_details = request.CustomerDetails(
        email="adam@pahlevi.com",
        first_name="Adam",
        last_name="Pahlevi",
        phone="0856071748"
    )

    req.add_item(request.ItemDetail(
        id="ITEM-1",
        price=200000,
        quantity=5,
        name="Ayam Bakar"
    ))

    req.add_item(request.ItemDetail(
        id="ITEM-2",
        price=300000,
        quantity=8,
        name="Bubur Ayam"
    ))

    req.va_number = "1111"
    req.add_bca_inquiry_texts(indonesian_text="Indonesian", english_text="English")
    req.add_bca_payment_text(indonesian_text="Indonesian", english_text="English")

    serialized_req = {'payment_type': 'bank_transfer',
                      'transaction_details': {'order_id': 'ORD-1234', 'gross_amount': 500000},
                      'bank_transfer': {'va_number': '1111',
                                        'free_text': {'inquiry':[{'en': 'English', 'id': 'Indonesian'}],
                                                      'payment': [{'en': 'English', 'id': 'Indonesian'}]},
                                        'bank': 'bca'},
                      'item_details': [
                          {'price': 200000.0, 'id': 'ITEM-1', 'name': 'Ayam Bakar', 'quantity': 5},
                          {'price': 300000.0, 'id': 'ITEM-2', 'name': 'Bubur Ayam', 'quantity': 8}
                      ],
                      'customer_details': {'phone': '0856071748', 'first_name': 'Adam', 'last_name': 'Pahlevi',
                                           'email': 'adam@pahlevi.com'}}

    assert req.serialize() == serialized_req


def test_mandiri_bill():
    req = request.ChargeMandiriBill(
        order_id="ORD-4821",
        gross_amount=200000
    )

    req.add_item(request.ItemDetail(
        id="ITEM-1",
        price=200000,
        quantity=5,
        name="Ayam Bakar"
    ))

    serialized_req = {'transaction_details': {'order_id': 'ORD-4821', 'gross_amount': 200000},
                      'payment_type': 'echannel',
                      'item_details': [{'price': 200000.0, 'id': 'ITEM-1', 'name': 'Ayam Bakar', 'quantity': 5}]}

    print req.serialize()

    assert req.serialize() == serialized_req