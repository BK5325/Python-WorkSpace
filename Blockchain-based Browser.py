from flask import Flask, request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

app = Flask(__name__)

class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, data):
        block = {"data": data}
        self.chain.append(block)
        return block

@app.route("/blockchain", methods=["POST"])
def add_block():
    data = request.get_json()
    blockchain = Blockchain()
    block = blockchain.add_block(data)
    return jsonify({"message": "Block added successfully", "block": block}), 201