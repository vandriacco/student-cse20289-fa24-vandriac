import os
import subprocess
import argparse

def process_file(path, file):
    full_path = os.path.join(path, file)
    output = subprocess.run(["python3", "searchsrc.py", full_path, "--include", "--includelocal", "--memberfuncs", "--onelinefunc"], capture_output=True, text=True)
    output_list = output.stdout.split("\n")

    while "" in output_list:
        output_list.remove("")

    output_dict = {}
    for item in output_list:
        item = item.split(": ")
        output_dict[item[0]] = item[1]

    return output_dict


def print_dict(input_dict):
    print(input_dict["path"] + input_dict["file"] + ",", \
          input_dict["lines"], "LOC,", \
          input_dict["include"], "I,", \
          input_dict["includelocal"], "LI,", \
          input_dict["memberfuncs"], "MF,", \
          input_dict["onelinefuncs"], "OLF")

# print_dict(process_file("src", "RIPPS_PktPair.cc"))

parser = argparse.ArgumentParser(description="Analyze c++ files")
parser.add_argument("directory")
parser.add_argument("-r", action="store_true")
parser.add_argument("--csv")
parser.add_argument("--stats", action="store_true")
parser.add_argument("--quiet", action="store_true")

args = parser.parse_args()

def scan_dir(dir, is_quiet=False, is_recursive=False):
    children = os.listdir(dir)

    # gets files from list of sub-directories
    files = []
    sub_dirs = []
    for child in children:
        if child.endswith(".cc"):
            files.append(child)
        else:
            sub_dirs.append(child)


    directories = []
    if files:
        for file in files:
            output = process_file(dir, file)
            directories.append(output["path"] + file)
            if not is_quiet:
                print_dict(output)

    if is_recursive:
        if not sub_dirs:
            return directories
        
        for sub_dir in sub_dirs:
            directories += scan_dir(os.path.join(dir, sub_dir), is_quiet=is_quiet, is_recursive=is_recursive)
    
    return directories

print(scan_dir(args.directory, is_quiet=args.quiet, is_recursive=args.r))