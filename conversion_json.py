"""
By: Casey Finnicum and Jeff Beck
"""
import csv
import json
import sys

# take the file name as the parameter passed to conversion.py
inFile = sys.argv[1]
outfile = inFile.strip('.csv')

CSV_PATH = inFile
JSON_PATH = outfile + str('.json')


def csv_to_json(csv_path, json_path):
    with open(csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        with open(json_path, 'w') as json_file:
            for row in reader:
                json_file.write(json.dumps(row) + '\n')


csv_to_json(CSV_PATH, JSON_PATH)
