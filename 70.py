from itertools import permutations
x=1000
ran=[]
max=5
j=0
def prime(num):
    """if the number is prime then print 1"""
    if num==1:

        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            c = 0
            return False
            break
    else:

        return True
primes=[]
for i in range(2000,5000):
    if prime(i)==True:
        primes.append(i)
list1=list(permutations(primes,2))
for q in list1:

    phin=(q[0]-1)*(q[1]-1)
    n=(q[0])*(q[1])
    if n<=10000000:
        if sorted(list(str(phin))) == sorted(list(str(n))):

            if max >= n / phin:
                max = n / phin
                j = n
                x=phin

print(j)

