'''
By: Casey Finnicum and Jeff Beck
'''

import csv
import json
import sys

inFile = sys.argv[1]
outfile = inFile.strip('.csv')

CSV_PATH = inFile
JSON_PATH = outfile + str('.json')

with open(CSV_PATH, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    with open(JSON_PATH, 'w') as json_file:
        for row in reader:
            json_file.write(json.dumps(row) + '\n')

