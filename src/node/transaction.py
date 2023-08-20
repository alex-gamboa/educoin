from collections import OrderedDict
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA3_256
from binascii import hexlify, unhexlify


class Transaction:
    def __init__(self, sender, recipient, amount, signature=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

        if signature:
            self.signature = signature

    def to_dict(self):
        if hasattr(self, "signature"):
            return OrderedDict(
                {
                    "sender": self.sender,
                    "recipient": self.recipient,
                    "amount": self.amount,
                    "signature": self.signature,
                }
            )
        else:
            return OrderedDict(
                {
                    "sender": self.sender,
                    "recipient": self.recipient,
                    "amount": self.amount,
                }
            )

    def sign(self, sender_key):
        private_key = RSA.importKey(unhexlify(sender_key))
        signer = PKCS1_v1_5.new(private_key)

        hash = SHA3_256.new(str(self.to_dict()).encode("utf8"))

        self.signature = hexlify(signer.sign(hash)).decode("ascii")

        return self.signature
