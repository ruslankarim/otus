import os
import sys
import csv
from project.utils import split_case

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)


def split_it():
    # Решеия по инстанциям
    cases_1 = 'cases_1.csv'
    cases_2 = 'cases_2.csv'
    cases_3 = 'cases_3.csv'

    current = cases_1

    cases_1_split = 'cases_1_split.csv'
    cases_2_split = 'cases_2_split.csv'
    cases_3_split = 'cases_3_split.csv'

    current_split = cases_1_split

    cases = []

    with open(current, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        max_rows = 0
        rows_read = 0
        for row in reader:
            rows_read += 1
            text = row['text_sol']
            cases.append(split_case(text))
            if max_rows != 0 and rows_read == max_rows:
                break

    try:
        os.remove(current_split)
    except OSError:
        pass

    with open(current_split, 'a', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['intro', 'description', 'justification', 'resolution'])
        for case in cases:
            writer.writerow(['\n'.join(case['intro']), '\n'.join(case['description']), '\n'.join(case['justification']),
                             '\n'.join(case['resolution'])])


split_it()
