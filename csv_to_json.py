#!/usr/bin/env python3
"""Reads CSV data from a file, converts it to JSON format and saves it to a new file.

Example usages:
CSV_To_JSON.py Input.csv Output.json "Column 1" "Column 2" "Column 3"
CSV_To_JSON.py -i 2 -mk "April Sales" Input.csv Output.json "Column 1" "Column 2" "Column 3"
CSV_To_JSON.py --transpose Needs_Transposing.csv Output.json "Column 1" "Column 2" "Column 3"
"""


__author__ = "Phixyn"
__version__ = "v1.2.0"


import argparse
import csv
import json
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reads CSV data from a file, converts it to JSON format and saves it to a new file.")
    parser.add_argument("input_file", action="store", default=None, help="Path/file name of the CSV file to be converted.")
    parser.add_argument("output_file", action="store", default=None, help="Path/file name for the resulting JSON file.")
    parser.add_argument("keys", action="store", nargs="+", default=None, help="Names for the keys in the JSON file. Usually these are the titles of your columns in your CSV file.")
    parser.add_argument("-t", "--transpose", action="store_true", help="Transposes the contents of the CSV file before converting to JSON.")
    parser.add_argument("-i", "--indent-spaces", action="store", default=4, type=int, metavar="SPACES", help="Number of spaces to use for indentation in the JSON file (defaults to 4).")
    parser.add_argument("-mk", "--main-key", action="store", default="items", help="String used for the main 'key' in the JSON file (defaults to 'items').")
    parser.add_argument("-V", "--version", action="version", version="CSV To JSON {0}".format(__version__), help="Displays version information and exits.")
    args = vars(parser.parse_args())

    keyName = args["main_key"]
    # Dictionary to hold the JSON to write to file
    # You can add additional items here if you want, instead of copying the resulting JSON to an existing file
    finalJSON = {
        keyName: []
    }
    # Get attribute names passed in the command line
    # These are the keys for each value
    fieldNames = args["keys"]

    with open(args["input_file"], "r") as inputCSVFile:
        # Read the CSV from the input file and transpose it if needed
        inputCSV = zip(*csv.reader(inputCSVFile)) if args["transpose"] else csv.reader(inputCSVFile)
        # Iterate through the CSV and append each row to the items in our dictionary
        for row in inputCSV:
            finalJSON[keyName].append(dict(zip(fieldNames, row)))

    # Create and write to output JSON file
    with open(args["output_file"], "w") as jsonFile:
        json.dump(finalJSON, jsonFile, indent=args["indent_spaces"])
