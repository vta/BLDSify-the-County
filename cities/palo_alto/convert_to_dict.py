import os
import csv
import json
import six

TSV_DATA = "./data/palo_alto/data.csv"

FIELDNAMES = ("Description",
              "Job Value",
              "Record Status Date",
              "Last Updated",
              "Record Status",
              "Longitude",
              "Record Type",
              "Record Module",
              "APN",
              "Latitude",
              "Date Opened",
              "Record ID",
              "Business Name",
              "ID",
              "Licence NBR",
              "Address Full Line")


def clean_and_annotate(row, label):
   return row


def convert_to_dicts(label):
    with open(TSV_DATA, 'rU') as tsv_input:
        tsv_reader = csv.DictReader(tsv_input, fieldnames=FIELDNAMES, delimiter=',')
        # Skip the first line of the CSV file, which contains the headers
        next(tsv_reader)
        return [clean_and_annotate(row, label) for row in tsv_reader]


def get_palo_alto_permits():
    permits = {}
    label = 'data'
    print("Load " + TSV_DATA)
    permits_for_file = convert_to_dicts(label)
    permits[label] = permits_for_file
    return permits


