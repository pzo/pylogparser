#!/usr/bin/env python
import csv

a = """"F1", "F2", "F3", "F4", "F5"
"A",2,3,4,5
"B",6,7,8,9
"""

r = csv.DictReader(a.split("\n"), dialect = csv.excel)
for row in r:
	print(row)

print("Hello, World!")
