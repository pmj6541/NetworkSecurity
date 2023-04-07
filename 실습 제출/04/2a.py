from Crypto.Util.asn1 import *
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import base64

#create KeyPair
from Crypto.PublicKey import RSA
keyPair=RSA.generate(2048)

#save publicKey
pubKey = keyPair.publickey()
pubKeyDER= pubKey.export_key( format="DER" )
with open("public.der","wb") as f1:
	f1.write(pubKeyDER)

#read 1.txt
with open("1.txt","r") as f1:
	msg = f1.read()
msg = bytes(msg, 'utf-8')

#auth
h= SHA.new()
h.update(msg)
signer=PKCS1_PSS.new(keyPair)
sig=signer.sign(h)

#base64 encode & save
sig_base64 = base64.b64encode(sig)
with open("sig.txt","wb") as f2:
    f2.write(sig_base64)