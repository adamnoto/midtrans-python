# Midtrans

Midtrans :heart: Python! :snake: :tada:

Python is a dynamically typed language, which has a clean and very
structured syntax and is very well suited for the web, amongst other things.
Now, you can use Midtrans in Python, natively!

## Usage blueprint

1. There is a class named `Client` (midtrans.Client) that should be instantiated first.
2. Instance of `Client` is then passed to the `midtrans.gateway` driver. Two drivers exist,
   you can use either: `Snap` or `Core` (for raw API access).
3. Any activity (charge, approve, get token, etc) is done in the gateway level.

## Example

Snap, getting the token using `get_token_quick`:

```python
def test_snap_gateway():
    client = Client(
        client_key="Vt-Client-Key",
        server_key="Vt-Server-Key",
        environment_type=PRODUCTION
    )

    snap = gateway.Snap(client=client)
    snap_resp = snap.get_token_quick("my-order-id", 200000)
    token = snap_resp.token
```

Alternatively you may construct your own snap request:

```python
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
```

Using the core API is not much different. There are plenty of test examples
ready to browse at the `tests` folder, which should provide you
with examples on how to better utilise this library.

## Installation

To install the package:

```
python setup.py install
```

### For maintainer

To install on development mode:

```
python setup.py develop
```

To install on local machine:

```
pip install .
```

To install the package with a symlink:

```
pip install -e .
```

To make the distribution, execute:

```
python setup.py sdist
```

To make the distribution, and publish it so other can install without cloning this repository:

```
python setup.py register sdist upload
```

### Testing

The library test units are written in pytest. After successful install of
`pytest`, just simply execute `pytest` at the root directory to run
the unit testings.