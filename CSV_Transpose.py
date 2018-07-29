#!/usr/bin/env python3

# TODO: Add CLI arguments for input and output filenames (and a help/usage argument too)

import csv
a = zip(*csv.reader(open("CSVToTranspose.csv", "r")))
csv.writer(open("output.csv", "w", newline="")).writerows(a)
