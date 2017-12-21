import zlib
import json
import requests
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

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


#
# MAIN: Encryption function testing 
# 

if __name__ == "__main__":
    health_record_json_1 = {
        "name" : "John Doe",
        "city" : "Tampa",
        "Hospital" : "John's Hopkin's",
        "condition" : "healthy"
    }

    pub_key, priv_key, passphrase = "public.pem", "private.pem", "blockchain"

    cipher_text = encrypt_record(json.dumps(health_record_json_1), pub_key)

    

    original_message = decrypt_record(cipher_text, priv_key, passphrase)
