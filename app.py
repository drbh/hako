
import base64, json, os, sys

# import sys
sys.path.append("..")
from ncipfs import ncipfs
from umbral.keys import UmbralPrivateKey, UmbralPublicKey
from flask import Flask, request, send_from_directory, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

# start connections
n = ncipfs.ncipfs()
n.connect(
	# "localhost:11501",
	# "18.212.122.50:11500",
	"52.14.207.225:9151", ## NUCPYHERS TEST NETWORK
	# "localhost:5001"
	"192.168.0.6:5001"
	# "https://ipfs.infura.io:5001" ## INFURAS IPFS GATEWAY (limitations)
)

@app.route('/data', methods=["POST", "OPTIONS"]) 
def data():

	if request.method == 'OPTIONS':
		return jsonify({"status": "ok"})
	print(request.form)


	# print(request.files)

	if len(request.files) > 0:
		file = request.files['file']
		data = file.read()
		print(file)
		print(len(data))

	response = jsonify({'some': 'data'})
	response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
	response.headers.add('Access-Control-Allow-Headers', '*')	

	my_nucid = n.add_data_and_grant_self_access(
		request.form["username"],
		request.form["password"],
		request.form["filename"],
		data)

	print(my_nucid)
	return jsonify({"nucid": my_nucid})


@app.route('/create_user', methods=["POST"])
def create_user():
	n.create_new_user(request.json["name"], request.json["password"])
	return jsonify({'status': 'user created!'})

@app.route('/add_data', methods=["POST"])
def add_data():
	my_nucid = n.add_data_and_grant_self_access(
	    request.json["username"], 
	    request.json["password"],
	    request.json["filename"], 
	    request.json["contents"])
	return jsonify({"nucid": my_nucid})

@app.route('/allow_access', methods=["POST"])
def allow_access():
	shareable_nucid = n.grant_others_access(
	    request.json["username"], 
	    request.json["password"],
	    request.json["cid"],
	    request.json["filename"], 
	    request.json["enc"], 
	    request.json["sig"])
	return jsonify({"nucid": shareable_nucid})

@app.route('/decrypt_message', methods=["POST"])
def decrypt_message():
	print(request.json)
	message = n.fetch_and_decrypt_nucid(
		request.json["username"], 
		request.json["nucid"])

	print("DECRYPTING\n")
	print(request.json["username"], request.json["nucid"])

	if type(message) is not str:
		print(type(message))
		return jsonify({"contents": base64.b64encode(message).decode("utf-8")})

	return jsonify({"contents": message})

@app.route('/my_public_keys', methods=["POST"])
def my_public_keys():
	message = ncipfs.get_users_public_keys(request.json["username"], True)
	print(message)
	return jsonify({"keys": message})


if __name__ == '__main__':
	app.run(host="0.0.0.0")