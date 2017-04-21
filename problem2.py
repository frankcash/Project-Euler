"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
a, b = 1, 1
fiboTotal, total =0, 0
while(fiboTotal < 4000000):
    fiboTotal = a+b;
    a, b = b, fiboTotal
    if((b%2)==0):
        total+=b;
        
print(fiboTotal)

print(total)
