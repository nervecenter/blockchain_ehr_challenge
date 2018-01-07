import json, hashlib
from Crypto import Random
from Crypto.Cipher import AES

BS = AES.block_size
mode = AES.MODE_CBC
padding = '{'

def encrypt_record(payload, passphrase):
	pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

	key = hashlib.sha256(passphrase.encode()).digest()
	iv = Random.new().read(BS)
	cipher = AES.new(key, mode, iv)

	return iv + cipher.encrypt(pad(payload).encode())

def decrypt_record(ciphertext, passphrase):
	unpad = lambda s : s[0:-ord(s[-1])]

	key = hashlib.sha256(passphrase.encode()).digest()
	iv = ciphertext[:BS]
	cipher = AES.new(key, mode, iv)

	return unpad(cipher.decrypt(ciphertext[BS:]).decode())

def test_adding_encrypted_record(chain):
	address = "0xe1acf4f3e8d20577759ff1009d54fe4cbfa946ad"
	health_recorder, _ = chain.provider.get_or_deploy_contract('HealthRecorder')

	health_record_json = {
		"name" : "John Doe",
		"city" : "Tampa",
		"Hospital" : "John's Hopkin's",
		"condition" : "healthy"
	}

	passphrase = "blockchain"

	ciphertext_push = encrypt_record(json.dumps(health_record_json), passphrase)
	ciphertext_push_hash = hashlib.md5(ciphertext_push).hexdigest()

	print("\n", type(ciphertext_push))

	print("Pushed ciphertext length:", len(ciphertext_push))
	print("Pushed ciphertext hash:", ciphertext_push_hash)

	set_txn_hash = health_recorder.transact().setRecord(address, ciphertext_push)
	chain.wait.for_receipt(set_txn_hash)

	ciphertext_pull = health_recorder.call().getRecord(address)
	print(type(ciphertext_pull))
	ciphertext_pull_hash = hashlib.md5(ciphertext_pull.encode()).hexdigest()

	print("Pulled ciphertext length:", len(ciphertext_pull))
	print("Pulled ciphertext hash:", ciphertext_pull_hash)

	#assert ciphertext_push_hash == ciphertext_pull_hash
	#assert len(ciphertext_push) == len(ciphertext_pull)

	payload_pull = decrypt_record(ciphertext_pull.encode(), passphrase)
	assert json.loads(payload_pull) == health_record_json

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