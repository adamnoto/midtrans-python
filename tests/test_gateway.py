from midtrans import Client, PRODUCTION, gateway, request

def test_snap_gateway():
    client = Client(
        client_key="Vt-Client-Key",
        server_key="Vt-Server-Key",
        environment_tyoe=PRODUCTION
    )

    snap = gateway.Snap(client=client)
    snap_charge = request.SnapChargeReq(
        order_id="ORD-238232",
        gross_amount=200000
    )
    snap_charge.whitelist_bins = ['451111', '501921']

    token = snap.get_token(snap_charge).token

    methods = dir(snap)
    assert "get_token" in methods
    assert "get_token_quick" in methods