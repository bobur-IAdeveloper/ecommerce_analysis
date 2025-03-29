import csv

def load_csv(file):
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)
