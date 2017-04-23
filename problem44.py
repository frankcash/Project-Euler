"""
Problem 44
"""

from math import *
from operator import *
from itertools import *

def genPent(n):
    P = n * (3*n - 1)// 2
    return P

def main():
    numList = set(genPent(n) for n in range(1, 3000))
    combs = combinations(numList, 2)
    for p in combs:
        if add(*p) in numList and abs(sub(*p)) in numList:
            print(abs(sub(*p)))

if __name__ == "__main__":
    main()
