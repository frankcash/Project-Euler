val = 0
for y in range(0, 999): 
    for x in range (0, 999):
        tv = x*y
        if(str(tv) == str(tv)[::-1]):
            if(tv>val):
                print(tv)
                val=tv

print(val)
