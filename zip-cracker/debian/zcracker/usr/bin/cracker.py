"""
    python 3 - Zip File Cracker Source
"""

__author__ = "rexcheng1997"


import os, zipfile
import multiprocessing as mp
from contextlib import contextmanager
from functools import partial
from generator import generator

def cracker_core(_password, _zfile, _wf="pwd.txt", _pscreen=True):
    '''
        Open _zfile using _password.
        If _password is correct, wrote it to _wf if _pscreen is False; otherwise, print _password to stdout on the screen.

        Attributes:

            - _password: password used to open _zfile
            - _zfile: path to the zipped file
            - _wf: path to the file where the correct password is written
    '''
    try:
        with zipfile.ZipFile(_zfile, 'r') as f:
            f.extractall(pwd=bytes(_password, "utf-8"))
            if _pscreen:
                print("Found password: " + _password)
            else:
                with open(_wf, 'a') as w:
                    w.write(_password + '\n')
                print("Password successfully found!")
                print("Wrote to file " + _wf + " in the current directory.")
    except zipfile.BadZipFile:
        print("File type not supported!")
        exit(2)
    except:
        pass

@contextmanager
def poolcontext(*args, **kwargs):
    try:
        p = mp.Pool(*args, **kwargs)
        yield p
        p.terminate()
    except KeyboardInterrupt:
        raise GeneratorExit

def cracker(_plen, _characters, _zfile, _cpu, _pscreen):
    '''
        Attributes:

            - _plen: length of the passwords
            - _characters: characters included in the passwords
            - _zfile: name of the zipped file
            - _cpu: number of cpu cores to use
            - _pscreen: print the password to stdout on the screen if True
    '''
    currDir = os.path.abspath('.')
    zfile = os.path.join(currDir, _zfile)
    try:
        pwdList = generator(_plen, _characters)
    except AttributeError:
        print("Need to specify the characters included in the password!")
        exit(1)
    try:
        with poolcontext(processes=_cpu) as p:
            p.map(partial(cracker_core, _zfile=zfile, _pscreen=_pscreen), pwdList)
        print("Finished.")
    except GeneratorExit:
        print("Program terminated by the user.")
        exit(0)
