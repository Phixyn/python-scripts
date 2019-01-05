#!/usr/bin/env python3
"""Reads CSV data from a file and converts it to JSON format.

Example usage: (note there are no spaces between the field name parameters)
CSV_To_JSON.py "Column 1","Column 2","Column 3","Column 4"
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

# Optional args to do with default values: indent spaces=4, keyName="items"
parser = argparse.ArgumentParser()
parser.add_argument("input_file", action="store", default=None, help="Path/file name of the CSV file to be converted.")
parser.add_argument("output_file", action="store", default=None, help="Path/file name for the resulting JSON file.")
parser.add_argument("--version", "-V", action="version", version="CSV To JSON {0}".format(__version__), help="Displays version information and exits.")
args = vars(parser.parse_args())


# INPUT_CSV_FILENAME = "TransposedCSV.csv"
# INPUT_CSV_FILENAME = "CSVToTranspose.csv"
# OUTPUT_JSON_FILENAME = "TestJSONImport.json"
keyName = "items"

# Dictionary to hold the JSON to write to file
# You can add additional items here
finalJSON = {
    keyName: []
}
# Get attribute names passed in the command line
# These are the keys for each value
fieldnames = tuple(sys.argv[1].split(","))

with open(args["input_file"], "r") as inputCSVFile:
    # Read the CSV from the input file and transpose it
    inputCSV = zip(*csv.reader(inputCSVFile))
    # TODO: add argument to transpose
    ##inputCSV = csv.reader(inputCSVFile) # No transpose option
    # Iterate through the CSV and append each row to the items
    # in our dictionary
    for row in inputCSV:
        finalJSON[keyName].append(dict(zip(fieldnames, row)))

# Create output JSON file
with open(args["output_file"], "w") as jsonFile:
    # Write JSON to file
    json.dump(finalJSON, jsonFile, indent=4)
