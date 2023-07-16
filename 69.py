x=1000
ran=[]
max=0
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
def fact(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return (i, x//i)
    else:
        return (x,True)

def factlist(c):
    x=c
    li1=[]
    while x!=True:
        y=fact(x)
        li1.append(y[0])
        x=y[1]
    return li1
def pre(y,w):
    z=(w*(y-1))//y
    return z
def new(m,n):
    return n/m
for n in range(2,1000000):
    liz=factlist(n)

    m=n
    linew=[]
    for i in liz:

        if not  i in linew:
            linew.append(i)
    for o in linew:
        n=pre(o,n)
    k=new(n,m)
    if k>=max:
        max=k
        j=m

print('answer is =',j)




