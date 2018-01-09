import json, hashlib, base64
from Crypto import Random
from Crypto.Cipher import XOR

def encrypt_record(payload, passphrase):
	cipher = XOR.new(passphrase)
	return base64.b64encode(cipher.encrypt(payload))

def decrypt_record(ciphertext, passphrase):
	cipher = XOR.new(passphrase)
	return cipher.decrypt(base64.b64decode(ciphertext))

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

	print("\nPushed ciphertext length:", len(ciphertext_push))
	print("Pushed ciphertext hash:", ciphertext_push_hash)

	set_txn_hash = health_recorder.transact().setRecord(address, ciphertext_push)
	chain.wait.for_receipt(set_txn_hash)

	ciphertext_pull = health_recorder.call().getRecord(address)
	ciphertext_pull_hash = hashlib.md5(ciphertext_pull.encode()).hexdigest()

	print("Pulled ciphertext length:", len(ciphertext_pull))
	print("Pulled ciphertext hash:", ciphertext_pull_hash)

	assert ciphertext_push_hash == ciphertext_pull_hash
	assert len(ciphertext_push) == len(ciphertext_pull)

	payload_pull = decrypt_record(ciphertext_pull.encode(), passphrase)
	assert json.loads(payload_pull) == health_record_json