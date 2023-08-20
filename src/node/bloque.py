import json


class Bloque:
    def __init__(
        self,
        indice,
        transactions,
        nonce,
        hash_anterior=None,
    ):
        self.indice = indice
        self.transactions = transactions
        self.nonce = nonce
        self.hash_anterior = hash_anterior

    def to_dict(self):
        return {
            "indice": self.indice,
            "transactions": json.dumps(
                [transaction.to_dict() for transaction in self.transactions]
            ),
            "nonce": self.nonce,
            "previous_hash": self.hash_anterior,
        }
