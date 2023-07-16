from time import time
strt=time()
def nu(x):
    n=1
    if x==0:
        return 1
    for i in range(1, x+1):
        n=n*i
    return n
def com(a, b):
    num=int((nu(a))/(nu(b)*nu(a-b)))
    return num
x=0
for a in range(1, 101):
    for b in range(1, a+1):
        if com(a, b)>=1000000:
            x+=1
end=time()
print(x)
print(end-strt)