#!/usr/bin/python3
'''UTF-8 Validation module'''


def validUTF8(data):
    '''UTF-8 Validation Function
Returns True/False
'''


def validUTF8(data):
    numBytes = 0

    for num in data:
        if numBytes == 0:
            if (num >> 7) == 0b0:
                numBytes = 0
            elif (num >> 5) == 0b110:
                numBytes = 1
            elif (num >> 4) == 0b1110:
                numBytes = 2
            elif (num >> 3) == 0b11110:
                numBytes = 3
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            numBytes -= 1

    return numBytes == 0
