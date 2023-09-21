#!/usr/bin/python3
'''Module for function that returns fewest number of coins to meet total'''


def makeChange(coins, total):
    '''Function that returns fewest number of coins to meet total'''
    if total <= 0:
        return 0
    change = [float('inf')] * (total + 1)
    change[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            change[amount] = min(change[amount], change[amount - coin] + 1)
    return change[total] if change[total] != float('inf') else -1
