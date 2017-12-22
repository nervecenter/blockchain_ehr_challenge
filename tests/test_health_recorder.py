from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import json
import hashlib

def encrypt_record(json_str, public_key_file):
	key = RSA.importKey(open(public_key_file).read())
	cipher = PKCS1_OAEP.new(key)
	cipher_text = cipher.encrypt(str.encode(json_str))
	return cipher_text

def decrypt_record(cipher_text, private_key_file, passphrase):
	key = RSA.importKey(open(private_key_file).read(), passphrase)
	cipher = PKCS1_OAEP.new(key)
	json_str = cipher.decrypt(cipher_text).decode()
	return json_str

def test_adding_encrypted_record(chain):
	address = "0xe1acf4f3e8d20577759ff1009d54fe4cbfa946ad"
	health_recorder, _ = chain.provider.get_or_deploy_contract('HealthRecorder')

	health_record_json = {
		"name" : "John Doe",
		"city" : "Tampa",
		"Hospital" : "John's Hopkin's",
		"condition" : "healthy"
	}

	pub_key, priv_key, passphrase = "public.pem", "private.pem", "blockchain"

	cipher_text = encrypt_record(json.dumps(health_record_json), pub_key)

	print("\nCiphertext length:", len(cipher_text))
	print("Ciphertext hash:", hashlib.md5(cipher_text).hexdigest())

	set_txn_hash = health_recorder.transact().setRecord(address, cipher_text)
	chain.wait.for_receipt(set_txn_hash)

	stored_cipher_text = health_recorder.call().getRecord(address).encode()
	print("Pulled ciphertext length:", len(stored_cipher_text))
	print("Pulled ciphertext hash:", hashlib.md5(stored_cipher_text).hexdigest())

	original_message = decrypt_record(stored_cipher_text, priv_key, passphrase)
	assert json.loads(original_message) == health_record_json

# def test_adding_record(chain):
# 	address = "0xe1acf4f3e8d20577759ff1009d54fe4cbfa946ad"
# 	health_recorder, _ = chain.provider.get_or_deploy_contract('HealthRecorder')

# 	health_record_json = {
# 		"name" : "John Doe",
# 		"city" : "Tampa",
# 		"Hospital" : "John's Hopkin's",
# 		"condition" : "healthy"
# 	}

# 	print(health_record_json)

# 	json_text = json.dumps(health_record_json)

#   #print()
# 	#print("JSON length:", len(json_text))
# 	#print(json_text)

# 	set_txn_hash = health_recorder.transact().setRecord(address, json_text)
# 	chain.wait.for_receipt(set_txn_hash)

# 	stored_json_text = health_recorder.call().getRecord(address).encode()
# 	#print("Pulled JSON length:", len(stored_json_text))
# 	#print(stored_json_text)
# 	print(json.loads(stored_json_text))

# 	assert json.loads(stored_json_text) == health_record_json