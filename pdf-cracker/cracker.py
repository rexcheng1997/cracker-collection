"""
    python 3 - Pdf File Cracker Source
"""

__author__ = "rexcheng1997"


import os
import multiprocessing as mp
from PyPDF2 import PdfFileReader
from contextlib import contextmanager
from functools import partial
from generator import generator

def cracker_core(_password, _pdf, _wf="pwd.txt", _pscreen=True):
    '''
        Open _pdf using _password.
        If _password is correct, wrote it to _wf if _pscreen is False; otherwise, print _password to stdout on the screen.

        Attributes:

            - _password: password used to open _zfile
            - _pdf: path to the pdf file
            - _wf: path to the file where the correct password is written
    '''
    try:
        with open(_pdf, 'rb') as f:
            reader = PdfFileReader(f)
            f.decrypt(_password)
            if _pscreen:
                print("Found password: " + _password)
            else:
                with open(_wf, 'a') as w:
                    w.write(_password + '\n')
                print("Password successfully found!")
                print("Wrote to file " + _wf + " in the current directory.")
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

def cracker(_plen, _characters, _pdf, _cpu, _wl, _pscreen):
    '''
        Attributes:

            - _plen: length of the passwords
            - _characters: characters included in the passwords
            - _pdf: name of the pdf file
            - _cpu: number of cpu cores to use
            - _wl: list of passwords used
            - _pscreen: print the password to stdout on the screen if True
    '''
    currDir = os.path.abspath('.')
    pdf = os.path.join(currDir, _pdf)
    pwdList = []
    try:
        if _wl:
            with open(os.path.join(currDir, _wl), 'r') as f:
                lines = f.read()
                pwdList = lines.split('\n')[:-1]
        else:
            pwdList = generator(_plen, _characters)
    except AttributeError:
        print("Need to specify the characters included in the password!")
        exit(1)
    except IOError:
        print("No such file called " + _wl + " under the current directory!")
        exit(2)
    try:
        with poolcontext(processes=_cpu) as p:
            p.map(partial(cracker_core, _pdf=pdf, _pscreen=_pscreen), pwdList)
        print("Finished.")
    except GeneratorExit:
        print("Program terminated by the user.")
        exit(0)
