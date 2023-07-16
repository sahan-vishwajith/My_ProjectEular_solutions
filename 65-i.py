import math


def first(N):
    A=int(N)
    x=N
    y=A
    z=N**2-(A**2)
    return [A,x,y,z]


def second(a):
    m=False
    n=0
    while m==False:
        n+=1
        q=n*a[3]-a[2]
        if (math.e**2) < q**2:
            A=n-1
            m=True
            break
    x=math.e
    y=A*a[3]-a[2]
    z=(math.e**2-y**2)/a[3]
    return [A,x,y,z]
def ans(x,z):
    #z is a llist
    b=z[1]*x+z[0]
    a=z[1]
    return [a,b]

k = first(math.e)
#print(k[0])
lix=[k[0],]
for i in range(100):
    print(second(k))
    lix.append(second(k)[0])
    k=second(k)
#print(len(lix))
lix=lix[:100]
lix=lix[::-1]
init=[1,lix[0]]
lix.pop(0)
#print(lix)

for i in lix:
    #print(ans(i,init))
    init=ans(i,init)
print(init[0])
print(init[1])
o=str(init[1])
hi=0
for u in o:
    hi+=int(u)
print(hi)