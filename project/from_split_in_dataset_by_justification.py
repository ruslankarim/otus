import csv
import os
import re

from project.utils import extract_joint_stock, clean_name_sides

cases_1_split = 'cases_1_split.csv'
output_sides = 'output_sides.csv'
output_justification = 'output_justification.csv'


def from_split_in_dataset_by_justification():
    sides = []
    with open(cases_1_split, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        max_rows = 300
        rows_read = 0
        justification = []
        for row in reader:
            cleaned = []
            rows_read += 1
            text = row['justification']
            if not text:
                continue
            for line in text.split('\n'):
                cleaned_names = clean_name_sides(line)

                cleaned.append(cleaned_names)

            if len(cleaned) > 0: justification.append(['\n'.join(cleaned)])
            if max_rows != 0 and rows_read == max_rows:
                break

    try:
        os.remove(output_sides)
    except OSError:
        pass
    with open(output_sides, 'a', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(sides)

    try:
        os.remove(output_justification)
    except OSError:
        pass
    with open(output_justification, 'a', encoding='utf-8') as output_file_j:
        writer = csv.writer(output_file_j)
        writer.writerows(justification)


from_split_in_dataset_by_justification()
