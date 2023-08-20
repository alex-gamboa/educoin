from wallet import Wallet
from transaction import Transaction
from requests import get, post
from collections import OrderedDict

import json

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-nw", "--new_wallet", action="store_true")
    parser.add_argument("-t", "--transaction", action="store_true")
    parser.add_argument("-pubk", "--public_key", type=str, default=None)
    parser.add_argument("-prvk", "--private_key", type=str, default=None)
    parser.add_argument("-r", "--recipient", type=str, default=None)
    parser.add_argument("-a", "--amount", type=float, default=None)
    parser.add_argument("-gt", "--get_transactions", action="store_true")
    parser.add_argument("-m", "--minar", action="store_true")
    parser.add_argument("-bc", "--blockchain", action="store_true")

    args = parser.parse_args()

    if args.new_wallet:
        w = Wallet()
        print(f"Address: {w.address}")
        print(f"Private Key: {w.private_key}")

    if args.transaction:
        t = Transaction(args.public_key, args.recipient, args.amount)

        print(f"Signature: {t.firmar(args.private_key)}")

        response = post(
            "http://127.0.0.1:5001/transactions/nueva",
            headers={
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json",
            },
            json=json.dumps(
                OrderedDict(
                    {
                        "sender": t.origen,
                        "recipient": t.destino,
                        "amount": t.monto,
                        "signature": t.signature,
                    }
                ),
                indent=4,
            ),
        )

        print(response.json())

    if args.get_transactions:
        response = get(
            "http://127.0.0.1:5001/transactions",
            headers={
                "Access-Control-Allow-Origin": "*",
            },
        )

        print(response.json())

    if args.minar:
        response = get(
            "http://127.0.0.1:5001/minar",
            headers={
                "Access-Control-Allow-Origin": "*",
            },
        )

        print(response.json())

    if args.blockchain:
        response = get(
            "http://127.0.0.1:5001/cadena",
            headers={
                "Access-Control-Allow-Origin": "*",
            },
        )

        print(response.json())
