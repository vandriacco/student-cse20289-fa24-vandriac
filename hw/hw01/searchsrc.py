# Vince Andriacco
# vandriac@nd.edu

import argparse

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

# counts number of member functions
def countMember(fileLines):
    num_members = 0

    for line in fileLines:
        num_members += line.count('::')

    return num_members

# counts number of pointer dereferences
def countPointer(fileLines):
    num_ptrs = 0

    for line in fileLines:
        num_ptrs += line.count('->')

    return num_ptrs

# counts functions with one line
def countSimpleFunc(fileLines):
    num_simplefunc = 0

    for i in range(len(fileLines)):
        # checks if line before and after logic of function only has a curly brace (and new line)
        if fileLines[i].startswith('{') and fileLines[i+2].startswith('}'):
            num_simplefunc += 1

    return num_simplefunc

# counts functions with one line
def countSimpleFuncEC(fileLines):
    num_simplefunc = 0

    for i in range(len(fileLines)):
        # counts curly brace regardless of whether it is on its own line
        if '{' in fileLines[i] and '}' in fileLines[i+2]:
            num_simplefunc += 1

    return num_simplefunc

# Define the various arguments via argparse
parser = argparse.ArgumentParser(description='Analyze c++ files')
parser.add_argument('file_name', help='Name of file to analyze')
parser.add_argument('--include', help='Count number of includes', action='store_true')
parser.add_argument('--member', help='Count number of member functions', action='store_true')
parser.add_argument('--ptr', help='Count pointer references ->', action='store_true')
parser.add_argument('--simplefunc', help='Count functions with one line', action='store_true')
parser.add_argument('--simplefuncec', help='Count functions with one line extra credit', action='store_true')

args = parser.parse_args()

file = readFile(args.file_name)

# chooses correct output based on flag given
if args.include:
    print('file:', args.file_name, 'lines:', countLine(file), 'include:', countInclude(file))
elif args.member:
    print('file:', args.file_name, 'lines:', countLine(file), 'member:', countMember(file))
elif args.ptr:
    print('file:', args.file_name, 'lines:', countLine(file), 'ptr:', countPointer(file))
elif args.simplefunc:
    print('file:', args.file_name, 'lines:', countLine(file), 'simplefunc:', countSimpleFunc(file))
elif args.simplefuncec:
    print('file:', args.file_name, 'lines:', countLine(file), 'simplefunc:', countSimpleFuncEC(file))