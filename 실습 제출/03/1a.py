from Crypto.Hash import HMAC

#sender
f = open('1.txt','r')
str = f.read()
str = bytes(str, 'utf-8')
key = input("input key : ")
h=HMAC.new( bytes(key, 'utf-8')) 
h.update (str)
mac= h.digest()
w = open('H.txt','wb')

w.write(str)
w.write(mac)



