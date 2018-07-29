#!/usr/bin/env python3
"""Reads CSV data from a file and turns it into JSON format. Only compatible
with Python 2.x at the moment (but easy to port to Python 3).

Example usage: (note there are no spaces between the field name parameters)
CSV_To_JSON.py "Column 1","Column 2","Column 3","Column 4"
"""


__author__ = "Phixyn"
__version__ = "v1.1.3"


import sys
import csv
import json


INPUT_CSV_FILENAME = "TestTableExport.csv"
# INPUT_CSV_FILENAME = "CSVToTranspose.csv"
OUTPUT_JSON_FILENAME = "TestJSONImport.json"
keyName = "items"

# Dictionary to hold the JSON to write to file
# You can add additional items here
finalJSON = {
    keyName: []
}
# Get attribute names passed in the command line
# These are the keys for each value
fieldnames = tuple(sys.argv[1].split(","))

with open(INPUT_CSV_FILENAME, "r") as inputCSVFile:
    # Read the CSV from the input file and transpose it
    inputCSV = zip(*csv.reader(inputCSVFile))
    # TODO: add argument to transpose
    # inputCSV = csv.reader(inputCSVFile) # No transpose option
    # Iterate through the transposed CSV and append each row to
    # the items in our dictionary
    for row in inputCSV:
        finalJSON[keyName].append(dict(zip(fieldnames, row)))

# Create output JSON file
with open(OUTPUT_JSON_FILENAME, "w") as jsonFile:
    # Write JSON to file
    json.dump(finalJSON, jsonFile, indent=4)
