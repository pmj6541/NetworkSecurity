from Crypto.Hash import HMAC

#sender
f = open('1.txt','r')
str = f.read()
str = bytes(str, 'utf-8')
key = input("input key : ")
h=HMAC.new( bytes(key, 'utf-8')) 
h.update (str)
mac2= h.digest()

w = open('H.txt','rb')
mac=w.read()
mac = mac[-16:]
print('H.txt : ', mac)
print('mac2 : ', mac2)
if mac==mac2:
	print('ok')
else :
	print('nok')


