from time import time
str=time()
def first(N):
    A=int(N**0.5)
    x=N
    y=A
    z=N-(A**2)
    return [A,x,y,z,1]


def second(a):
    x=False
    n=0
    y=0
    b=0
    while x==False:
        n+=1
        y=a[3]*n-a[2]
        if y**2>a[1]*(a[4]**2):
            b=y-a[3]
            d=b*a[3]
            c=n-1
            x=True
            break
    z=a[1]*(a[4]**2)-b**2
    if z%a[3]==0:
        return [c,a[1],b,z//a[3],1]
    else:
        return [c,a[1],d,z,a[3]*a[4]]
count=0
for v in range(2,10001):
    g=(v**0.5)
    if g%1!=0:

        k = first(v)

        listx = [k, ]
        listans = []
        o=False
        while o ==False:

            k = second(k)

            if k in listx:
                #print('ok')
                o=True
                break
            listx.append(k)

        for u in listx:
            listans.append(u[0])
        listans.pop(0)
        #print(v, listans, len(listans))
        if len(listans)%2!=0:
            count+=1
print(count)
end=time()
print(end-str)

