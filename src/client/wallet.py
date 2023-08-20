from Crypto.PublicKey import RSA
from Crypto import Random
from binascii import hexlify as hex


class Wallet:
    def __init__(self):
        self.generar_llaves()

    def generar_llaves(self):
        random_gen = Random.new().read
        private_key = RSA.generate(1024, random_gen)
        public_key = private_key.publickey()

        self.address = self.formatear_key(public_key)
        self.private_key = self.formatear_key(private_key)

    def formatear_key(self, key):
        return hex(key.exportKey(format="DER")).decode("ascii")
