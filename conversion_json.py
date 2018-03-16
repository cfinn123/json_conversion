"""
By: Casey Finnicum and Jeff Beck
"""
import csv
import json
import sys
import progressbar as pb
import os

# Take file name as the parameter passed to json_conversion.py
inFile = sys.argv[1]
CSV_PATH = inFile

# Make output filename from input filename
outfile = inFile.strip('.csv')
JSON_PATH = outfile + str('.json')

# Obtain size (in bytes) of input file
statinfo_in = os.stat(inFile)

# Function for outputting human-readable file sizes:
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

# Print input file in human-readable format
print("Input (.csv) file size: ", sizeof_fmt(statinfo_in.st_size))

# Determine number of lines in input file to be used for progress bar
fname = inFile
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines in csv file:", num_lines)

# Set widgets for progress bar
widgets = ['Converting csv to json. Percentage completed:', pb.Percentage(), ' ',
           pb.Bar(marker='█'), ' ', pb.ETA()]

# Create progress bar and initialize
bar = pb.ProgressBar(widgets=widgets, maxval=num_lines).start()

def csv_to_json(csv_path, json_path):
        # Open connection to csv file
        with open(csv_path, 'r') as csv_file:
            # Create reader object; a dictionary of the csv file
            reader = csv.DictReader(csv_file)
            # Open output json file
            with open(json_path, 'w') as json_file:
                # Iterate over lines in file (i:num_lines) and items in reader dict (row:reader)
                for i, row in zip(range(0, num_lines), reader):
                    # Write each row from reader dict to json file
                    json_file.write(json.dumps(row) + '\n')
                    # Progress bar updates as for loop iterates over line in file (i:num_lines)
                    bar.update(i)
                # End progress bar
                bar.finish()

# Run function
csv_to_json(CSV_PATH, JSON_PATH)

# Obtain size (in bytes) of output file
statinfo_out = os.stat(JSON_PATH)

# Print out file in human-readable format
print("Output (.json) file size: ", sizeof_fmt(statinfo_out.st_size))

print("Conversion completed!")
