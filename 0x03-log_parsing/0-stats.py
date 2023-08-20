#!/usr/bin/python3
''' Log parsing module prints status_codes in ascending order and file size '''
from sys import stdin
from collections import Counter
import re

total_size = 0
status_dict = Counter()
line_count = 0
possible = [200, 301, 400, 401, 403, 404, 405, 500]

# Regex for robust line validation
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)"  # nopep8


def print_statistics():
    '''Handles print statements'''
    print("File size: {}".format(total_size))
    for code, count in sorted(status_dict.items()):
        print("{}: {}".format(code, count))


try:
    for log in stdin:
        match = re.search(pattern, log)
        if match:
            status_code, file_size = match.groups()
            if status_code.isdigit() and int(status_code) in possible:
                status_dict[status_code] += 1
                total_size += int(file_size)
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    pass

# Print the final statistics after the loop or after KeyboardInterrupt
print_statistics()
