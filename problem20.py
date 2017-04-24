"""
Find the sum of the digits in the number 100!

"""

def factorial(fact):
    if(fact < 2):
        return fact
    if(fact == 2):
        return 2
    tot = 1
    for x in range(2, fact):
        tot *= x
    return tot


def sumFact(tot):
    sum = 0
    for x in range(0, len(str(tot))):
        sum += int(str(tot)[x])
    return sum


def main():
    print(sumFact(factorial(100)))


main()
