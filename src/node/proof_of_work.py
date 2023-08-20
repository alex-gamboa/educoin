import json
import hashlib


def minar(bloque, bloque_anterior):
    bloque.nonce = 0
    bloque.hash_anterior = calcular_hash(bloque_anterior)

    while validar_prueba(bloque) is False:
        bloque.nonce += 1

    return bloque


def validar_prueba(bloque):
    guess_hash = calcular_hash(bloque)

    return guess_hash[:4] == "0000"


def calcular_hash(block):
    blockStr = json.dumps(
        block.to_dict(),
        sort_keys=True,
    ).encode("utf8")

    hash = hashlib.new("sha256")
    hash.update(blockStr)
    return hash.hexdigest()
