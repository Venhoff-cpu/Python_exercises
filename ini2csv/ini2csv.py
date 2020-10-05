from configparser import ConfigParser
import argparse
import csv

parser = argparse.ArgumentParser(".ini file convertion into .csv")
parser.add_argument("ini_file", help=".editorconfig file")
parser.add_argument("csv_file", help=".csv file name")
parser.add_argument("--collapsed", help="collapses to one row per section", action="store_true")
args = parser.parse_args()

# initialize config parser for our .ini file.
config = ConfigParser()
config.read(args.ini_file)

with open(args.csv_file, 'wt') as csv_file:
    # Initilize csv writer that comes with csv built-in package
    csv_writer = csv.writer(csv_file)
    # if collapse argument was provided create first line of csv writer.
    if args.collapsed:
        csv_writer.writerow(["header", "indent_style", "indent_size"])
    # Iterate through config dict (ConfigDict is a dict inheriting after collection.OrderedType - order of sections and
    # values will be the same as in original file)
    for name, section in config.items():
        if name == "DEFAULT":
            continue
        if args.collapsed:
            csv_writer.writerow([name, *section.values()])
        else:
            for key, value in section.items():
                # No need for strip. csv writer takes care of that.
                csv_writer.writerow([name, key, value])

# Version without csv writer and ConfigParser
# with open(args.ini_file) as ini_file:
#     # open context menager for csv_file with write mode on
#     with open(args.csv_file, "wt") as csv_file:
#         # iterate thorugh each line of inni file
#         for line in ini_file:
#             # section of .ini file starts with '['
#             if line.startswith("["):
#                 # pass on the last element of string - an end bracket ']'
#                 section = line.strip()[1:-1]
#             # check if line (string) after strip have any characters left
#             elif line.strip():
#                 # split line with characters. left side os string contains attribute name,
#                 # right side attribute value.
#                 attr, value = line.split('=')
#                 attr = attr.strip()
#                 value = value.strip()
#                 # Write line into new csv file usin f string
#                 csv_file.write(f"{section},{attr},{value}\n")
