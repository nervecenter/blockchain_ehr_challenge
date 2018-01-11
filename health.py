import json, base64
from Crypto import Random
from Crypto.Cipher import XOR
from populus import Project

p = Project()
with p.get_chain('emr') as chain:
    health_recorder, deploy_tx_hash = chain.provider.get_or_deploy_contract('HealthRecorder')

print("Health Recorder contract address on emr is {address}".format(address=health_recorder.address))
if deploy_tx_hash is None:
    print("The contract is already deployed on the chain")
else:
    print("Deploy Transaction {tx}".format(tx=deploy_tx_hash))

def encrypt_record(payload, passphrase):
	cipher = XOR.new(passphrase)
	return base64.b64encode(cipher.encrypt(payload))

def decrypt_record(ciphertext, passphrase):
	cipher = XOR.new(passphrase)
	return cipher.decrypt(base64.b64decode(ciphertext))

def get_record_chain(address, passphrase):
	ciphertext_pull = health_recorder.call().getRecord(address)
	return json.loads(decrypt_record(ciphertext_pull.encode(), passphrase))

def set_record_chain(record_dict, address, passphrase):
	ciphertext_push = encrypt_record(json.dumps(record_dict), passphrase)
	set_txn_hash = health_recorder.transact({'from':chain.web3.eth.coinbase}).setRecord(address, ciphertext_push)
	chain.wait.for_receipt(set_txn_hash)