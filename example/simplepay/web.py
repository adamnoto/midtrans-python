from flask import Flask, request, session, g, \
        redirect, url_for, abort, render_template, flash

from midtrans import Client, SANDBOX, gateway
from midtrans.request import SnapChargeReq
import uuid

app = Flask(__name__)
midtrans_client = Client(
    client_key="VT-client-IKktHiy3aRYHljsw",
    server_key="VT-server-7CVlR3AJ8Dpkez3k_TeGJQZU",
    environment_tyoe=SANDBOX
)

@app.route('/')
def hello_world():
    snap = gateway.Snap(client=midtrans_client)
    snap_charge = SnapChargeReq(
        order_id = str(uuid.uuid4()),
        gross_amount = 200000
    )
    token = snap.get_token(snap_charge).token

    return render_template('index.html', token = token)
