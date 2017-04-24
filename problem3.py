"""
What is the largest prime factor of the number 600851475143 ?

"""

def main():
    num = 600851475143
    for x in range(2, num):
        if(num % x == 0):
            num /= x;

        print(num)

main()
