import math
from math import sqrt
from collections import Counter
z=1500000
value=[]
for m in range(2,int(sqrt(z/2))+1):
    for n in range(1,m):
        l = 2 * m * (m + n)
        k=1
        if (m+n)%2==1 and math.gcd(m,n)==1:
            while l*k<=z:
                value.append(k*l)
                k+=1
c = Counter(value)
cou=0
for x in c.values():
    if x==1:
        cou+=1
print(cou)