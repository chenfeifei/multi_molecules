#!/usr/bin/python

import csv

fname = "percentages.csv"

with open("percentages.csv", "r") as f:
	reader = csv.reader(f, delimiter=",", skipinitialspace=True)
	for r in reader:
		for v in r:
			print(v)
		print("End of row")
