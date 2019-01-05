#!/usr/bin/env python3
"""Reads CSV data from a file and converts it to JSON format.

Example usages:
CSV_To_JSON.py Input.csv Output.json "Column 1" "Column 2" "Column 3"
CSV_To_JSON.py -i 2 -mk "April Sales" Input.csv Output.json "Column 1" "Column 2" "Column 3"
"""

__author__ = "Phixyn"
__version__ = "v1.1.3"

import argparse
import csv
import json
import sys


##########
## TODO for both?
# Add this to our CSV scripts (can add --quote arg to them)
## wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
###########

parser = argparse.ArgumentParser()
parser.add_argument("input_file", action="store", default=None, help="Path/file name of the CSV file to be converted.")
parser.add_argument("output_file", action="store", default=None, help="Path/file name for the resulting JSON file.")
parser.add_argument("keys", action="store", nargs="+", default=None, help="Names for the keys in the JSON file. Normally these are the titles of your columns in your CSV file.")
parser.add_argument("-i", "--indent-spaces", action="store", default=4, type=int, help="Number of spaces to use for indentation in the JSON file (defaults to 4).")
parser.add_argument("-mk", "--main-key", action="store", default="items", help="String used for the main 'key' in the JSON file (defaults to 'items').")
parser.add_argument("--version", "-V", action="version", version="CSV To JSON {0}".format(__version__), help="Displays version information and exits.")
args = vars(parser.parse_args())
print(args)


# INPUT_CSV_FILENAME = "TransposedCSV.csv"
# INPUT_CSV_FILENAME = "CSVToTranspose.csv"
# OUTPUT_JSON_FILENAME = "TestJSONImport.json"
keyName = args["main_key"]

# Dictionary to hold the JSON to write to file
# You can add additional items here
finalJSON = {
    keyName: []
}
# Get attribute names passed in the command line
# These are the keys for each value
fieldNames = args["keys"]

with open(args["input_file"], "r") as inputCSVFile:
    # Read the CSV from the input file and transpose it
    inputCSV = zip(*csv.reader(inputCSVFile))
    # TODO: add argument to transpose
    ##inputCSV = csv.reader(inputCSVFile) # No transpose option
    # Iterate through the CSV and append each row to the items
    # in our dictionary
    for row in inputCSV:
        finalJSON[keyName].append(dict(zip(fieldNames, row)))

# Create output JSON file
with open(args["output_file"], "w") as jsonFile:
    # Write JSON to file
    json.dump(finalJSON, jsonFile, indent=args["indent_spaces"])
