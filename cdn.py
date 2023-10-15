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
import optparse

parser = optparse.OptionParser(add_help_option = False, description="cdn: customisable cd indexer. (c) 2023 Matthias Nicoloso")

class colors:
    bg_red   = '\033[41m'   # Red background
    red      = '\033[1;31m' # Red
    green    = '\033[1;32m' # Green
    orange   = '\033[1;33m' # Orange
    cyan     = '\033[1;36m' # Cyan
    gray     = '\033[0;37'  # Gray
    no_color = '\033[0m'    # No Color
    

class icons:
    error   = colors.red    + "[E]" + colors.no_color
    warning = colors.orange + "[W]" + colors.no_color
    okay    = colors.green  + "[O]" + colors.no_color
    info    = colors.cyan   + "[I]" + colors.no_color
    

def paint(string, color):
    return getattr(colors, color) + string + colors.no_color


def err_IncompleteArg():
    print(f"\n{icons.warning} Please specify a location to go to, or type {paint(parser.get_prog_name() + ' --help', 'cyan')} for help.")


def opt_Help():
    parser.print_help()


def main():
    if len(sys.argv) <= 1:
        err_IncompleteArg()
        # sys.exit()
    else:
        parser.add_option("-h", "--help",
                        help="Print this help page",
                        action="help")
        parser.add_option("-a", "--add",
                        help="Add a new location (using '.' as path will use your working directory)",
                        action='store_true')
        parser.add_option("-r", "--remove",
                        help="Remove a specific location",
                        action='store_true')
        parser.add_option("-l", "--list",
                        help="List all stored locations",
                        action='store_true')
        parser.add_option("-s", "--sort",
                        help="Sort the locations in 'data' by alphabetical order",
                        action='store_true')
        parser.add_option("-v", "--version",
                        help="Print the program's version",
                        action='store_true')
        
        parser.add_option("--ug",
                        help="Update the global script (recommended after an update)",
                        action='store_true')
        parser.add_option("--sp",
                        help="Add the nim's 'starter pack' in the 'data' file",
                        action='store_true')
        parser.add_option("--lp",
                        help=f"{paint('[NIM ONLY]', 'orange')} Add the labos paths in the 'data' file",
                        action='store_true')
        parser.add_option("--np",
                        help="Create a new project directory",
                        action='store_true')
        
        parser.add_option("--PURGE",
                        help="Erase all the saved locations, no warning",
                        action='store_true')
        parser.add_option("--NUKE",
                        help="Remove the data file and folder, no warning",
                        action='store_true')
        (options, args) = parser.parse_args()

    


if __name__ == '__main__':
    main()