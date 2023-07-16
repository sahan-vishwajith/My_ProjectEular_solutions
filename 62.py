from itertools import permutations
from time import time
srt=time()
def perm(x):
    x=str(x)
    listx=list(permutations(x))
    listy=[]
    for i in listx:
        v=''
        for y in i:
            v+=y
        v=int(v)
        if v not in listy:
            listy.append(v)
    return listy

def cubroot(y):
    c = y**(1/3)
    if c%1==0:
        return True
    else:
        return False
k=2
x=False
listsec=[[1,2],[2,2],]
while x==False:

    k+=1
    v=k**3
    b=list(str(v))
    b=sorted(b)
    t=0
    for n in listsec:
        t += 1
        if b==n[1]:
            n.append(b)

            if len(n)==6:
                x=True
                print(n[0]**3)
                break                                
            break
    if t==len(listsec):
        listsec.append([k, b],)
end=time()
print(end-srt)
    
        
                    
