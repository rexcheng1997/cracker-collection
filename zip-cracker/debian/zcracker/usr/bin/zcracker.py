"""
    python 3 - Driver Module
"""

__author__ = "rexcheng1997"


import argparse
import multiprocessing as mp
from dictionaries import *
from cracker import cracker

parser = argparse.ArgumentParser()

# Required arguments.
parser.add_argument("input", type=str, help="path to the zipped file")

parser.add_argument("length", type=int, help="length of the passwords to crack")

# Optional arguments.
parser.add_argument("-l", "--lowercases", help="include lower-case letters in password cracking", action="store_true")

parser.add_argument("-u", "--uppercases", help="include upper-case letters in password cracking", action="store_true")

parser.add_argument("-d", "--digits", help="include digits in password cracking", action="store_true")

parser.add_argument("-s", "--specials", help="include special characters in password cracking", action="store_true")

parser.add_argument("-p", "--print", help="print the password on the screen instead of writing it to a file", action="store_true")

parser.add_argument("-f", "--force", help="[warning] use all computation resources", action="store_true")

args = parser.parse_args()
characters = []
cpu = mp.cpu_count()

if args.lowercases:
    characters += lowerCases
if args.uppercases:
    characters += upperCases
if args.digits:
    characters += digits
if args.specials:
    characters += specials
if not args.force:
    cpu = int(cpu / 2)

cracker(args.length, characters, args.input, cpu, args.print)
