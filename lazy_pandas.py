import pandas as pd
import sys

inFile = sys.argv[1]
outfile = inFile.strip('.csv')

CSV_PATH = inFile
JSON_PATH = outfile + str('.json')

df = pd.read_csv(inFile)
df.to_json(JSON_PATH)
