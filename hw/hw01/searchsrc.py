import argparse

def readFile(filename: str):
    file = open(filename, 'r')
    return file.readlines()

def countLine(fileLines):
    return len(fileLines)

def countInclude(fileLines):
    num_includes = 0
    
    for line in fileLines:
        if line.startswith("#include"):
            num_includes += 1

    return num_includes

def countMember(fileLines):
    num_members = 0

    for line in fileLines:
        num_members += line.count('::')

    return num_members

def countPointer(fileLines):
    num_ptrs = 0

    for line in fileLines:
        num_ptrs += line.count('->')

    return num_ptrs



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

if args.include:
    print('file:', args.file_name, 'lines:', countLine(file), 'include:', countInclude(file))
elif args.member:
    print('file:', args.file_name, 'lines:', countLine(file), 'member:', countMember(file))
elif args.ptr:
    print('file:', args.file_name, 'lines:', countLine(file), 'ptr:', countPointer(file))
