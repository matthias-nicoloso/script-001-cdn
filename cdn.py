#!/usr/bin/env /bin/python3

# cdn - cdnim, 2022-2023 https://github.com/matthias-nicoloso/script-001-cdn
# 
# A bash/python-based program that allows an in-depth 'cd' command management
# through customisable locations. Each of the locations added are written in a 
# data file and can be easily managed by the program.
#
# (c) Matthias Nicoloso <matthias.nicoloso@heig-vd.ch> <matthiasnicoloso@gmail.com>
# 
# "I just wanted to learn electronics, leave me alone" 
#                   - Matthias Nicoloso, 3rd semester at the HEIG-VD

import sys
import getopt

program_name = sys.argv[0]
user_args = sys.argv[1:]

short_options_args = "hlsva:r:"
long_options_args = ("help", "list", "sort", "version", "add", "remove")

print(f"{program_name}: Arguments parsés: {user_args}")

try:
    # Parsing argument
    parsed_args, parsed_values = getopt.getopt(user_args, short_options_args, long_options_args)
    
    # Vérification des arguments
    for arg, value in parsed_args:
        
        if arg in (""):
            print("Displaying no args")
        elif arg in ("-h", "--help"):
            print ("Displaying help")
        elif arg in ("-l", "--list"):
            print ("Displaying list")
        elif arg in ("-s", "--sort"):
            print ("Displaying sort")
        elif arg in ("-v", "--version"):
            print ("Displaying version")
        
        elif arg in ("-a", "--add"):
            print ("Displaying add")
        elif arg in ("-r", "--remove"):
            print ("Displaying remove")
    
except getopt.error as err:
    print(str(err))

print("ending.")