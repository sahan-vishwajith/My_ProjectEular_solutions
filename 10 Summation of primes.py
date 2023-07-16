def prime(num):
    """if the number is prime then print 1"""
    if num==1:
        c=0
        return c

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            c = 0
            return c
            break
    else:
        c = 1
        return c
z=1
y=1
b=0
while y!=2000000:
    y+=1
    print(y)
    if prime(y)==1:

        b+=y
print(b)

