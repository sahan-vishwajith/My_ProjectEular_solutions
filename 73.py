import math
import time
strt=time.time()
d=12000
li=[]
count=0
for i in range(1,d+1):
    for j in range(1,i):
        if j/i<1/2 and 1/3<j/i:
            if math.gcd(i,j)==1:
                count+=1
print(count)
end=time.time()
print(end-strt)