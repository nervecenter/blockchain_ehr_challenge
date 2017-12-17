import zlib
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def encrypt_record(json_str, public_key_file):
    key = RSA.importKey(open(public_key_file).read())
    cipher = PKCS1_OAEP.new(key)
    cipher_text = cipher.encrypt(str.encode(json_str))
    return cipher_text

def decrypt_record(cipher_text, private_key_file):
    key = RSA.importKey(open(private_key_file).read())
    cipher = PKCS1_OAEP.new(key)
    json_str = cipher.decrypt(cipher_text).decode()
    return json_str

if __name__ == "__main__":
    message = "Hello world! How do you do? I am a health record."

    print(message)

    pub_key = "rsa_key.pub"
    cipher_text = encrypt_record(message, pub_key)

    print(cipher_text)

    priv_key = "rsa_key.der"
    original_message = decrypt_record(cipher_text, priv_key)

    print(original_message)
