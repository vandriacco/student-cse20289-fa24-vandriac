# Vince Andriacco
# vandriac@nd.edu

import argparse
import re

# reads file into list of strings
def readFile(filename: str):
    file = open(filename, 'r')
    return file.readlines()

# counts number of lines in file
def countLine(fileLines):
    return len(fileLines)

# counts number of include statements
def countInclude(fileLines):
    num_includes = 0
    
    for line in fileLines:
        if line.startswith("#include"):
            num_includes += 1

    return num_includes

def countIncludeLocal(fileLines):
    num_includes = 0
    
    for line in fileLines:
        if line.startswith("#include") and line.split()[1].startswith("\""):
            num_includes += 1

    return num_includes

# counts number of member functions
def countMemberFuncs(fileLines):
    num_members = 0

    for line in fileLines:
        if re.search("^[a-zA-Z0-9].*(::)", line):
            num_members += 1

    return num_members

# counts functions with one line
def countOneLineFunc(fileLines):
    num_simplefunc = 0

    for i in range(len(fileLines)):
        # checks if line before and after logic of function only has a curly brace (and new line)
        if re.search("^[a-zA-Z0-9].*[{]$", fileLines[i]):
            if re.search("\n$", fileLines[i+1]):
                if re.search("^}", fileLines[i+2]):
                    num_simplefunc += 1

    return num_simplefunc


# Define the various arguments via argparse
parser = argparse.ArgumentParser(description='Analyze c++ files')
parser.add_argument('file_name', help='Name of file to analyze')
parser.add_argument('--include', help='Count number of includes', action='store_true')
parser.add_argument('--includelocal', help='Count number of local includes', action='store_true')
parser.add_argument('--memberfuncs', help='Count number of member functions', action='store_true')
parser.add_argument('--onelinefuncs', help='Count functions with one line', action='store_true')

args = parser.parse_args()

file = readFile(args.file_name)

# chooses correct output based on flag given

path = args.file_name.split('/')
file_name = path.pop()
path = '/'.join(path) + '/'

print('path:', path)
print('file:', file_name)
print('lines:', countLine(file))

if args.include:
    print('include:', countInclude(file))
if args.includelocal:
    print('includelocal:', countIncludeLocal(file))
if args.memberfuncs:
    print('memberfuncs:', countMemberFuncs(file))
if args.onelinefuncs:
    print('onelinefuncs:', countOneLineFunc(file))