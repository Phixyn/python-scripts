#!/usr/bin/env python3
"""Transposes the contents of a CSV file and saves the output to a new CSV file.

Example usage:
CSV_Transpose.py "input.csv" "output.json"
"""


__author__ = "Phixyn"
__version__ = "v1.1.0"


import argparse
import csv


# Set up command line argument parser
parser = argparse.ArgumentParser()
parser.add_argument("input_file", action="store", default=None, help="Path/file name of the CSV file to be transposed.")
parser.add_argument("output_file", action="store", default=None, help="Path/file name for the transposed CSV file.")
parser.add_argument("--version", "-V", action="version", version="CSV Transposer {0}".format(__version__), help="Displays version information and exits.")
args = vars(parser.parse_args())

# Transpose CSV and store output in new file
a = zip(*csv.reader(open(args["input_file"], "r")))
csv.writer(open(args["output_file"], "w", newline="")).writerows(a)
