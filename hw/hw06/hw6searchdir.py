# Vince Andriacco
# vandriac@nd.edu

import os
import subprocess
import argparse
import csv
import statistics
import sys

# runs searchsrc.py on a given file and returns output as a dict
def process_file(path, file):
    full_path = os.path.join(path, file)
    output = subprocess.run(
        ["python3", "../hw6searchsrc.py", full_path, "--include", "--memberfuncs", "--onelinefunc"], 
        capture_output=True, 
        text=True)
    output_list = output.stdout.split("\n")
    while "" in output_list:
        output_list.remove("")

    output_dict = {}
    for item in output_list:
        item = item.split(": ")
        output_dict[item[0]] = item[1]

    return output_dict

# prints a dict from process_file in a compact format
def print_dict(input_dict):
    print(input_dict["path"] + input_dict["file"] + ",", \
          input_dict["lines"], "LOC,", \
          input_dict["include"], "I,", \
          input_dict["includelocal"], "LI,", \
          input_dict["memberfuncs"], "MF,", \
          input_dict["onelinefuncs"], "OLF")

# runs process_file on every file in a given directory
def scan_dir(dir, is_quiet=False, is_recursive=False):
    children = os.listdir(dir)
    # separates files and subdirs from list of sub-directories
    files = []
    sub_dirs = []
    for child in children:
        child = os.path.join(dir, child)
        if child.endswith(".cc"):
            files.append(child)
        elif os.path.isdir(child):
            sub_dirs.append(child)

    # runs subprocess for each file
    dictionaries = []
    if files:
        for file in files:
            output = process_file(dir, file.split("/")[-1])
            if output:
                dictionaries.append(output)
                if not is_quiet:
                    print_dict(output)

    # recursive call with base case
    if is_recursive:
        if not sub_dirs:
            return dictionaries
        
        for sub_dir in sub_dirs:
            if os.listdir(sub_dir): # only makes recursive call if subdirectory is not empty
                dictionaries += scan_dir(sub_dir, is_quiet=is_quiet, is_recursive=is_recursive)
    
    return dictionaries

def create_csv(dict_list, csv_name):
    with open(csv_name, 'w') as csvfile:
        fieldnames = ["path", "file", "lines", "include", "includelocal", "memberfuncs", "onelinefuncs"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for dict in dict_list:
            writer.writerow(dict)

def compute_stats(dict_list):
    lines = []
    includes = []
    localincludes = []
    memberfuncs = []
    onelinefuncs = []

    for dict in dict_list:
        lines.append(dict["lines"])
        includes.append(dict["include"])
        localincludes.append(dict["includelocal"])
        memberfuncs.append(dict["memberfuncs"])
        onelinefuncs.append(dict["onelinefuncs"])

    lines = list(map(int, lines))
    min_lines = min(lines)
    max_lines = max(lines)
    mean_lines = statistics.mean(lines)
    median_lines = statistics.median(lines)
    stdev_lines = statistics.stdev(lines)

    includes = list(map(int,includes))
    min_includes = min(includes)
    max_includes = max(includes)
    mean_includes = statistics.mean(includes)
    median_includes = statistics.median(includes)
    stdev_includes = statistics.stdev(includes)

    localincludes = list(map(int, localincludes))
    min_localincludes = min(localincludes)
    max_localincludes = max(localincludes)
    mean_localincludes = statistics.mean(localincludes)
    median_localincludes = statistics.median(localincludes)
    stdev_localincludes = statistics.stdev(localincludes)

    memberfuncs = list(map(int, memberfuncs))
    min_memberfuncs = min(memberfuncs)
    max_memberfuncs = max(memberfuncs)
    mean_memberfuncs = statistics.mean(memberfuncs)
    median_memberfuncs = statistics.median(memberfuncs)
    stdev_memberfuncs = statistics.stdev(memberfuncs)

    onelinefuncs = list(map(int, onelinefuncs))
    min_onelinefuncs = min(onelinefuncs)
    max_onelinefuncs = max(onelinefuncs)
    mean_onelinefuncs = statistics.mean(onelinefuncs)
    median_onelinefuncs = statistics.median(onelinefuncs)
    stdev_onelinefuncs = statistics.stdev(onelinefuncs)

    for dict in dict_list:
        if int(dict["lines"]) == min_lines:
            min_lines_file = dict["file"]
        if int(dict["lines"]) == max_lines:
            max_lines_file = dict["file"]
        if int(dict["include"]) == min_includes:
            min_includes_file = dict["file"]
        if int(dict["include"]) == max_includes:
            max_includes_file = dict["file"]
        if int(dict["includelocal"]) == min_localincludes:
            min_localincludes_file = dict["file"]
        if int(dict["includelocal"]) == max_localincludes:
            max_localincludes_file = dict["file"]
        if int(dict["memberfuncs"]) == min_memberfuncs:
            min_memberfuncs_file = dict["file"]
        if int(dict["memberfuncs"]) == max_memberfuncs:
            max_memberfuncs_file = dict["file"]
        if int(dict["onelinefuncs"]) == min_onelinefuncs:
            min_onelinefuncs_file = dict["file"]
        if int(dict["onelinefuncs"]) == max_onelinefuncs:
            max_onelinefuncs_file = dict["file"]

    print("Field, Min, MinFile, Max, MaxFile, Mean, Median, StdDev")
    print("lines,", str(min_lines) + ",", min_lines_file + ",", str(max_lines) + ",", max_lines_file + ",", str(mean_lines) + ",", str(median_lines) + ",", stdev_lines)
    print("includes,", str(min_includes) + ",", min_includes_file + ",", str(max_includes) + ",", max_includes_file + ",", str(mean_includes) + ",", str(median_includes) + ",", stdev_includes)
    print("localincludes,", str(min_localincludes) + ",", min_localincludes_file + ",", str(max_localincludes) + ",", max_localincludes_file + ",", str(mean_localincludes) + ",", str(median_localincludes) + ",", stdev_localincludes)
    print("memberfuncs,", str(min_memberfuncs) + ",", min_memberfuncs_file + ",", str(max_memberfuncs) + ",", max_memberfuncs_file + ",", str(mean_memberfuncs) + ",", str(median_memberfuncs) + ",", stdev_memberfuncs)
    print("onelinefuncs,", str(min_onelinefuncs) + ",", min_onelinefuncs_file + ",", str(max_onelinefuncs) + ",", max_onelinefuncs_file + ",", str(mean_onelinefuncs) + ",", str(median_onelinefuncs) + ",", stdev_onelinefuncs)

    

if __name__ == "__main__":
    # command argument parsing
    parser = argparse.ArgumentParser(description="Analyze c++ files")
    parser.add_argument("directory")
    parser.add_argument("-r", action="store_true")
    parser.add_argument("--csv")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--quiet", action="store_true")

    args = parser.parse_args()
    if not os.path.isdir(args.directory):
        sys.stderr.write("error: directory does not exist, please enter an existing directory\n")
        sys.exit(1)

    # if not os.listdir(args.directory):
    #     sys.stderr.write("error: the inputed directory was empty\n")
    #     sys.exit(1)
    dict_list = scan_dir(args.directory, is_quiet=args.quiet, is_recursive=args.r)
    if args.csv:
        if os.path.isfile(args.csv):
            sys.stderr.write("error: csv file already exists, please choose a different name\n")
            sys.exit(1)
        create_csv(dict_list, args.csv)

    if args.stats and dict_list:
        compute_stats(dict_list)