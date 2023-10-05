#!/usr/bin/python3
'''Module for prime game function'''


def is_prime(n):
    '''Function to check for prime number'''
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(n):
    '''Function to add prime numbers from 1 to n'''
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    '''Function to get winner of prime game'''
    maria = 0
    ben = 0

    for n in nums:
        primes = get_primes(n)
        available_set = [True] * (n + 1)
        available_set[0] = available_set[1] = False

        maria_turn = True
        while True:
            found = False
            for prime in primes:
                if prime <= n and available_set[prime]:
                    found = True
                    available_set[prime] = False
                    for multiple in range(prime, n + 1, prime):
                        available_set[multiple] = False
                    break
            if not found:
                break
            maria_turn = not maria_turn
        if maria_turn:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return 'None'
