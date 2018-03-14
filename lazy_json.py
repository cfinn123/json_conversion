import pandas as pd
import sys

inFile = sys.argv[1]
outfile = inFile.strip('.csv')

CSV_PATH = inFile
JSON_PATH = outfile + str('.json')


def lazy_csv_to_json(infile, json_path):
    df = pd.read_csv(infile)
    df.to_json(json_path)


lazy_csv_to_json(CSV_PATH, JSON_PATH)
