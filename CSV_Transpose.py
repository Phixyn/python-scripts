#!/usr/bin/env python3
"""Transposes the contents of a CSV file and saves the output to a new file.

Example usages:
CSV_Transpose.py Input.csv Output.csv
CSV_Transpose.py --add-quotes Input.csv Output.csv
"""


__author__ = "Phixyn"
__version__ = "v1.2.0"


import argparse
import csv


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transposes the contents of a CSV file and saves the output to a new file.")
    parser.add_argument("input_file", action="store", default=None, help="Path/file name of the CSV file to be transposed.")
    parser.add_argument("output_file", action="store", default=None, help="Path/file name for the transposed CSV file.")
    parser.add_argument("-q", "--add-quotes", action="store_true", help="Adds double quotation marks (\") to all values in the CSV file. By default, the only quoted values are ones which contain special characters such as delimiter, quotechar or any of the characters in lineterminator.")
    parser.add_argument("-V", "--version", action="version", version="CSV Transposer {0}".format(__version__), help="Displays version information and exits.")
    args = vars(parser.parse_args())

    quotingMode = csv.QUOTE_ALL if args["add_quotes"] else csv.QUOTE_MINIMAL
    # Read from file and transpose CSV
    transposedCSV = zip(*csv.reader(open(args["input_file"], "r")))
    # Store output in new file
    csv.writer(open(args["output_file"], "w", newline=""), quoting=quotingMode).writerows(transposedCSV)
