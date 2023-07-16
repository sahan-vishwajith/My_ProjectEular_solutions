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

y=1
x=0
while x<=10000:
    y+=1
    if prime(y)==1:
        primes=y
        x+=1

print(primes)