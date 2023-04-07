from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

keyPair = RSA.generate(2048)

#private
privateKeyPEM = keyPair.export_key(passphrase="1234")	#privateKey save
with open("Alice_private.pem","wb") as f1:
	f1.write(privateKeyPEM)

#public
publicKey = keyPair.publickey()	
publicKeyPEM = publicKey.export_key() # publicKey save
with open("Alice_public.pem","wb") as f2:
	f2.write(publicKeyPEM)
