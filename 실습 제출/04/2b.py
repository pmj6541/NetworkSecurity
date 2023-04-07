from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import base64

with open("public.der","rb") as f1:
    public_der = f1.read()
pubKey= RSA.importKey(public_der)

with open("sig.txt","rb") as f2:
    sig_base64 = f2.read()
sig = base64.b64decode(sig_base64)

with open("1.txt","r") as f3:
    msg = f3.read()
msg = bytes(msg, 'utf-8')

h = SHA.new()
h.update(msg)
verifier=PKCS1_PSS.new ( pubKey )
verifier.verify ( h, sig )
if verifier.verify(h,sig) :
    print("verified")
else :
    print("not verified")