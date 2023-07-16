from time import time
strt=time()
def prime(p):
    if p==1:
        return False
    elif p==2:
        return True
    elif p>2:
        for y in range(2, int(p**0.5)+1):
            if p%y==0:
                return False

                break
        return True
def dupli(d):
    d=str(d)
    n=[]
    for i in d:
        if not i in n:
            n.append(i)
        elif i in n:
            return int(i)
    if len(d)==len(n):
        return None

def replace(d, x, y):
    d=list(str(d))
    v=''
    for i in d:
        if int(i)==x:
            d[d.index(str(x))]=str(y)
    for u in d:
        v+=str(u)
    v=int(v)
    return v
n=False
i=0
while n==False:
    i+=1
    s=0
    if prime(i)==True:
        if dupli(i)!=None:
            s=dupli(i)
            li=[]
            for t in range(10):
                o=replace(i,s,t)
                if prime(o)==True:
                    if len(str(o))==len(str(i)):
                        #print(i,o)
                        li.append(o)
            if len(li)==8:
                print(li)
                n=True
print(li[0])
end=time()
print(strt-end)