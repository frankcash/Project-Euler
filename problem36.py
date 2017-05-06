"""
Find the sum of all numbers, n, such that n < 1000000.
Where n is a palindrome in both base 10 and base 2.
Reference on Palindrome: http://mathworld.wolfram.com/PalindromicNumber.html
"""

def pali(num):
    if( str(num) == str(num)[::-1] ):
        return num
    else:
        return 0

def intToBin(num):
    return "{0:b}".format(num)

def main():
    sum = 0;
    for x in range(1, 1000000): # Start at 1 since 0 is disqualified by no leading 0 rule
        if(pali(x) == x):
            temp = intToBin(x)
            if(temp == pali(temp)):
                sum = sum + x
    print(sum)


main()
