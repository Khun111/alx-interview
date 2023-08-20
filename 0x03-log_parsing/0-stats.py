#!/usr/bin/python3
'''Log parsing module: prints total file size and \
status code in ascending order'''
from sys import stdin
from collections import Counter

total_size = 0
status_dict = Counter()
line_count = 0
possible = [200, 301, 400, 401, 403, 404, 405, 500]
try:
    for log in stdin:
        if len(log.split()) == 9:
            status_code, file_size = log.split()[-2], log.split()[-1]
            total_size += int(file_size)
            if status_code.isdigit() and int(status_code) in possible:
                status_dict[status_code] += 1
                line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in sorted(status_dict.items()):
                print("{}: {}".format(code, count))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code, count in sorted(status_dict.items()):
        print("{}: {}".format(code, count))
