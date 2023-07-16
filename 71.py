import math
x=3
y=7
z=0
max=0.01
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
c=1
n=1
while c<=1000000:

    n+=1
    c = n * 7
    d = n * 3

    if c<=1000000:
        if max <= (d - 1) / (c - 1):
            max = (d - 1) / (c - 1)
            z = d - 1

    else:
        break


print('the answer is =',z)
