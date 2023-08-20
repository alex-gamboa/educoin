from collections import OrderedDict
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA3_256
from binascii import hexlify, unhexlify


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.origen = sender
        self.destino = recipient
        self.monto = amount

    def firmar(self, sender_key):
        private_key = RSA.importKey(unhexlify(sender_key))
        signer = PKCS1_v1_5.new(private_key)

        hash = SHA3_256.new(
            str(
                OrderedDict(
                    {
                        "origen": self.origen,
                        "destino": self.destino,
                        "monto": self.monto,
                    }
                )
            ).encode("utf8")
        )

        self.signature = hexlify(signer.sign(hash)).decode("ascii")

        return self.signature
