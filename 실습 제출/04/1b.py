from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


with open("Alice_public.pem","rb") as f2:
    publicKeyPEM = f2.read()

pubkey = RSA.importKey(publicKeyPEM) 

encryptor = PKCS1_OAEP.new ( pubkey )

with open("1.txt","r") as f1:
	msg = f1.read()
msg = bytes(msg, 'utf-8')
encrypted=encryptor.encrypt(msg)

with open("enc.txt","wb") as f3:
    f3.write(encrypted)