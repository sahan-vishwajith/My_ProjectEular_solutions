from itertools import permutations
import math
num=0
snu=[]
for i in range(10, 100000):
    snu.append(i)
v1=0
v2=0
for a in snu:
    b=str(a)
    x=0
    for c in b:
        x+=math.factorial(int(c))
    if x==a:
        num+=a

print(num)

