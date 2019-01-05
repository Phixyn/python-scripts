#!/usr/bin/env python3
"""Transposes the contents of a CSV file and saves the output to a new file.

Example usage:
CSV_Transpose.py "input.csv" "output.csv"
"""

__author__ = "Phixyn"
__version__ = "v1.1.1"

import argparse
import csv


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", action="store", default=None, help="Path/file name of the CSV file to be transposed.")
    parser.add_argument("output_file", action="store", default=None, help="Path/file name for the transposed CSV file.")
    parser.add_argument("--version", "-V", action="version", version="CSV Transposer {0}".format(__version__), help="Displays version information and exits.")
    args = vars(parser.parse_args())

    # Read from file and transpose CSV
    transposedCSV = zip(*csv.reader(open(args["input_file"], "r")))
    # Store output in new file
    csv.writer(open(args["output_file"], "w", newline="")).writerows(transposedCSV)
