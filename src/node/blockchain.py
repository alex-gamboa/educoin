from time import time
from transaction import Transaction
from binascii import hexlify, unhexlify
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA3_256
from collections import OrderedDict
from requests import get

from bloque import Bloque
from proof_of_work import minar, calcular_hash, validar_prueba


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.chain.append(Bloque(1, [], 0, "0" * 64))

    def submit_transaction(self, transaction):
        # validar la firma
        if not self.valid_signature(transaction):
            return -1

        self.current_transactions.append(transaction)

        return len(self.chain) + 1

    def valid_signature(self, transaction):
        public_key = RSA.importKey(unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        hash = SHA3_256.new(
            str(
                OrderedDict(
                    {
                        "sender": transaction.sender,
                        "recipient": transaction.recipient,
                        "amount": transaction.amount,
                    }
                )
            ).encode("utf8")
        )

        try:
            verifier.verify(hash, unhexlify(transaction.signature))
            return True
        except ValueError:
            return False

    def proof_of_work(self):
        bloque = minar(
            Bloque(len(self.chain) + 1, self.current_transactions, 0),
            self.chain[-1],
        )

        self.current_transactions = []
        self.chain.append(bloque)

        # enviar la recompensa al minero por 1 Sagan , los nodos deben tener un wallet

        return bloque

    def is_valid_chain(self, chain):
        index = 1

        while index < len(chain):
            if chain[index].previous_hash != calcular_hash(chain[index - 1]):
                return False

            if not validar_prueba(chain[index]):
                return False

            index += 1

        return True

    def resolver_conflictos(self):
        # obtener la cadena mas larga de la red
        max_length = len(self.chain)
        new_chain = None

        # Obtener los nodos del registro de nodos
        for node in self.nodes:
            response = get(f"http://{node}/cadena")

            if response.status_code == 200:
                length = response.json()["length"]
                chain = response.json()["chain"]

                if length > max_length and self.is_valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False
