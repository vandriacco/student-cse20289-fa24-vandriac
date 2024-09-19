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
    sub_dirs = os.listdir(dir)
    
    # gets files from list of sub-directories
    files = []
    for sub_dir in sub_dirs:
        if sub_dir.endswith(".cc"):
            files.append(sub_dir)

    directories = []
    for file in files:
        output = process_file(dir, file)
        directories.append(output["path"] + file)
        if not is_quiet:
            print_dict(output)

    return directories

print(scan_dir(args.directory, is_quiet=args.quiet))

# print(os.walk("src"))