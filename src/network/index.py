from flask import Flask, render_template, request
from flask.json import jsonify
import json

app = Flask(__name__)

nodes = []


@app.route("/nodos/obtener", methods=["GET"])
def obtener_nodos():
    return jsonify({"nodes": nodes}), 200


@app.route("/nodos/registrar", methods=["POST"])
def registrar_nodo():
    values = request.get_json()

    nodes.append(values["address"])

    return jsonify({"message": "Nodo agregado"}), 201


@app.route("/nodos/eliminar", methods=["POST"])
def eliminar_nodo():
    values = json.loads(request.get_json())

    nodes.remove(values["address"])

    return jsonify({"message": "Nodo eliminado"}), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5200, debug=True)
