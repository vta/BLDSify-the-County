import os
import csv
import json
import six

TSV_FOLDER = "../data/tsv/"
FIELDNAMES = ("tract", "apn", "issue_date", "final_date", "lot", "permit_number", "owner",
              "contractor", "applicant", "location", "approval_status", "sub_code",
              "sub_code_description", "work_code", "work_code_description", "census_code",
              "permit_valuation", "reroof_valuation", "square_feet", "units", "rsn", "pool",
              "sewer", "enterprise", "permit_flag")


def clean_and_annotate(row, label):
   title = label.split('_')
   row["year"] = title[1]
   row["type"] = title[2]
   row = { k: (v.strip() if isinstance(v, six.string_types) else v) for k, v in row.items()}
   return row


def convert_to_dicts(label):
    with open(TSV_FOLDER + label + '.txt', 'rU') as tsv_input:
        tsv_reader = csv.DictReader(tsv_input, fieldnames=FIELDNAMES, delimiter='\t')
        # Skip the first line of the CSV file, which contains the headers
        next(tsv_reader)
        return [clean_and_annotate(row, label) for row in tsv_reader]


def run():
    permits = {}   
    # Go through all of the files, and convert them into arrays of dicts
    for file_name in os.listdir(TSV_FOLDER):
        if file_name.endswith(".txt"):
            label = file_name.strip(".txt")
            permits_for_file = convert_to_dicts(label)
            permits[label] = permits_for_file
            
    return permits
