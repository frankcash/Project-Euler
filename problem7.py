"""
What is the 10 001st prime number?

Utilizes the Sieve of Eratosthenes
"""

def eratosthenes(limit):
    multiples = set()
    for i in range(2, limit+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, limit+1,i))



print(list(eratosthenes(2000000))[10000])
