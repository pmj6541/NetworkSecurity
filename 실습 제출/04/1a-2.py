from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

passphrase = input("input passphrase : ")
#read private
with open("Alice_private.pem","rb") as f1:
    privatekeyPem = f1.read()
keyPair = RSA.import_key(privatekeyPem, passphrase)
#read encrypted
with open("enc.txt","rb") as f2:
    enc = f2.read()

decryptor = PKCS1_OAEP.new( keyPair )
decrypted=decryptor.decrypt(enc)
print ("Decrypted: ", decrypted)

