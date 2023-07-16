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
def ans(x,z):
    #z is a llist
    b=z[1]*x+z[0]
    a=z[1]
    return [a,b]
def pell(x,y,d):
    if (x**2)-(d*(y**2))==1:
        return True
    else:
        return False
ammo=[]
ammomax=[]
harimax=0
count=0
for v in range(2,1001):
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
        #print(v, listans, len(listans))
        lix=listans
        liz=listans
        count=0
        for i in range(1,len(lix)+1):
            lix = listans
            lix = lix[:i]
            lix = lix[::-1]
            init = [0, 1]
            count+=1
            # print(lix)

            for i in lix:
                # print(ans(i,init))
                init = ans(i, init)
            #print(init[1], '/', (init[0]))
            y=init[0]
            x=init[1]
            if pell(x,y,v):
                #print(init[1], '/', (init[0]),'*'*5,v)

                if harimax<=x:
                    harimax=x
                    ammomax=[x,v]
                break
            elif count==len(listans):
                e=False
                liy = listans[1:]
                while e==False:
                    #print('something')
                    for n in liy:
                        listans.append(n)
                        #print(listans)
                        lix = listans
                        lix = lix[::-1]
                        init = [0, 1]
                        count += 1
                        # print(lix)

                        for i in lix:
                            # print(ans(i,init))
                            init = ans(i, init)
                        #print(init[1], '/', (init[0]))
                        y = init[0]
                        x = init[1]
                        if pell(x, y, v):
                            #print(init[1], '/', (init[0]), '*' * 5, v)

                            if harimax <= x:
                                harimax = x
                                ammomax = [x, v]
                            e = True
                            break

end=time()
print(end-str)
print('answer is =',ammomax[1])





