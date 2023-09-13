import hashlib
from cryptography.fernet import Fernet

"""
class User:
    def __init__(self, user, website):
        self.user = user
        self.website = website
        self.password = "1"

    def get_user(self):
        print(self.user)
    def get_hashedpassword(self):
        print(self.password)
    def get_website(self):
        print(self.website)

    def set_password(self, p):
        self.password = p
"""

def Encryptor(password, key):
    key = key.encode('utf-8')
    cipher_suite = Fernet(key)
    password = password.encode('utf-8')
    encrypted_password = cipher_suite.encrypt(password)
    string_encrypted = str(encrypted_password, encoding='utf-8')
    return string_encrypted

def Decryptor(textToDecrypt, key):
    key = key.encode('utf-8')
    cipher_suite = Fernet(key)
    decryptedText = cipher_suite.decrypt(textToDecrypt)
    string_decrypted = str(decryptedText, encoding='utf-8')
    return string_decrypted

def generate_key():
    key = Fernet.generate_key()
    return key


print(Encryptor("lol", 'DvE2pp5nH8H8Kb3F9pk-F3k_j5XjO3tLrJYXBfuojnA='))
textToDecrypt = Encryptor("lol", 'DvE2pp5nH8H8Kb3F9pk-F3k_j5XjO3tLrJYXBfuojnA=')
print(Decryptor(textToDecrypt, 'DvE2pp5nH8H8Kb3F9pk-F3k_j5XjO3tLrJYXBfuojnA='))

