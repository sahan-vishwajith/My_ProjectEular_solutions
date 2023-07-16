primes=[2, 3, 5, 7, 11, 13, 17, 19]
n=0
p=0
x=1
for i in primes:
    n=0
    p=0
    for j in range(1, 20) :
        n=0
        while j%i==0:
            n+=1
            print(n)
            j=j/i
        if n>=p:
            p=n
            print(p)
    x=x*(i**p)
print(x)
#232792560





