#!/usr/bin/env python
#coding:utf-8
import os, sys
from cryptography.fernet import Fernet


victim = os.environ["USERNAME"]
drive = os.environ["SystemDrive"]

path = "{}.key".format(victim)
file = open(path, 'rb')
key = file.read()
file.close()

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def rep_cible():
    repertoire = ["%s\\Users\\%s\\Desktop\\repertoire_test\\"%(drive, victim)]
    for element in repertoire:
        for (root,dirs,files) in os.walk(element):  #selection de tout les element du repertoire
            for file in files :
                for extension in file.split("."):
                    if file.endswith(extension):
                        full = os.path.join(root, file)  #selection de toutes les extensions possibles
                        decrypt(full, key)
rep_cible()
