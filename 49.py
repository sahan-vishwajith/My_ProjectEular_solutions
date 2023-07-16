from itertools import permutations
from itertools import combinations
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
lists=[]
p=[]
for o in range(1000, 7000):
    if prime(o)==True and '0' not in str(o):
        lists.append(list(str(o)))

x=[]
for i in lists:
    x.append(list(permutations(i, 4)))

m=[]
for i in x:
    k=[]
    for j in i:
        s=''
        for let in j:
            s+=str(let)
        k.append(int(s))
    m.append(k)

for b in m:
    for a in b:


        n=a+3330
        if n in b:

            q=n+3330
            if q in b:

                if prime(a)==True and prime(n)==True and prime(q)==True:
                    p.append(str(a)+str(n)+str(q))
print(max(p))