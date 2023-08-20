import sys


from flask import Flask, render_template, request
from flask.json import jsonify
from transaction import Transaction

from blockchain import Blockchain
import json

app = Flask(__name__)

blockchain = Blockchain()


@app.route("/transactions/nueva", methods=["POST"])
def new_transaction():
    values = json.loads(request.get_json())

    block_number = blockchain.submit_transaction(
        Transaction(
            values["sender"],
            values["recipient"],
            values["amount"],
            values["signature"],
        )
    )

    if block_number == -1:
        return jsonify({"message": "Error en la transacción"}), 406
    else:
        return jsonify({"block": block_number}), 200


@app.route("/transactions", methods=["GET"])
def obtener_transacciones():
    return {"trx_length": len(blockchain.current_transactions)}, 200


@app.route("/minar", methods=["GET"])
def minar():
    bloque = blockchain.proof_of_work()

    return jsonify(bloque.to_dict()), 201


@app.route("/cadena", methods=["GET"])
def obtener_cadena():
    return (
        jsonify(
            {
                "chain": [bloque.to_dict() for bloque in blockchain.chain],
                "length": len(blockchain.chain),
            }
        ),
        200,
    )


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=5000)
    args = parser.parse_args()
    port = args.port

    app.run(host="127.0.0.1", port=port, debug=True)
