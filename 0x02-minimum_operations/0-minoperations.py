#!/usr/bin/python3
'''Module for mini operations'''


def minOperations(n):
    if n <= 1:
        return 0
    factor = 2
    ops = 0
    while factor <= n:
        if n % factor == 0:
            ops += factor
            n //= factor
        else:
            factor += 1
    return ops
