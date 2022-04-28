

import re
import pandas as pd

def get_csv():
    try:
        fname = input("Please enter filename in current directory: ")
        if not re.match("^.*.csv", fname.strip()):
            print("File provided is not a CSV file. Please try again with a CSV file.")
            raise TypeError
        else:
            process(fname)
    except TypeError:
        get_csv()

def process(csv):
    txtFile = csv.replace(".csv", ".txt")
    # inFile = pd.read_csv(csv)
    with open(csv, 'r') as inFile, open(txtFile, 'w') as outFile:
        fileContents = inFile.read()
        outFile.write(fileContents.replace(',', ' '))



get_csv()

