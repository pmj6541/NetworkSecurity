from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os, random, struct

def decrypt_file(key, filename):
	
	chunk_size = 16
	
	
	#open the encrypted file and the initialization vector. 
	#The IV is required for creating the cipher.
	
	
	with open(filename, 'rb') as infile:
		
		#create the cipher using the key and the IV.
		iv = b"Netsec@Soongsil."
		origsize = infile.read(4)
		
		#We also write the decrypted data to a verification file, 
		#so we can check the results of the encryption 
		#and decryption by comparing with the original file.
		decryptor = AES.new(key, AES.MODE_CBC, iv)
		while True:

			chunk = infile.read(chunk_size)
			if len(chunk) == 0:
				break
			
			message_decrypted = decryptor.decrypt(chunk)
			print(message_decrypted.strip().decode('utf-8'),end = ' ')
			

password = b"ABCDEF0123456789"
def getKey(password):
	hasher = SHA256.new(password)
	return hasher.digest()
	
decrypt_file(b"ABCDEF0123456789", 'enc1.txt');

