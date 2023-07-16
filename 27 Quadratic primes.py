import math
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
B=[]
for i in range(1, 1000):
    B.append(i)
for i in B:
    for l in B:
        if l%i==0 and i!=l:
            B.remove(l)

A=[]
for i in range(-999, 1000):
    A.append(i)
for i in A:
    if i%2==0:
        A.remove(i)
ans=0
ansa=0
ansb=0
for a in A:
    for b in B:
        n=0
        while n*n+a*n+b>0 and prime((n*n+a*n+b))==1:
            n+=1

            if ans<=n:
                ans=n
                ansa=a
                ansb=b
print(ans, ansa, ansb)
print(ansb*ansa)