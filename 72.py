import math
count=0
k=1000000
def prime(num):
    """if the number is prime then print 1"""
    if num==1:
        c=0
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            c = 0
            return False
            break
    else:
        c = 1
        return True

primes=[]
for r in range(2,1000000):
    if prime(r)==True:
        primes.append(r)
def phi(n):
    ph=n
    for pri in primes:
        if pri<=n:
            if n%pri==0:
                ph=ph*(pri-1)
                ph=ph/pri

        elif pri>n:
            break
    return int(ph)
print(phi(8))
for i in range(2,k+1):
    count+=phi(i)

print(count)