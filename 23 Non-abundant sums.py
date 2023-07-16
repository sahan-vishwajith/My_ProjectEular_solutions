from time import time
strt=time()
ans=0
pluse=0
abun=[]
num=[]
abu=[]
s=0
v=0
for i in range(2, 28123):
    pluse=1
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            if j==(i**0.5):
                pluse+=j
            else:    
                pluse+=j
                pluse+=(i//j)
    if pluse>i:
        abun.append(i)

for i in range(1, 28124):
    num.append(i)
for k in abun:
    v1=int(abun.index(k))
    v2=int(len(abun))+1
    for h in range(v1, v2):
        s=k+abun[h]

        if s>28123:
            break
        abu.append(s)

abu=list(dict.fromkeys(abu))
for u in abu:
    num.remove(u)

for i in num:
    ans+=i
end=time()
print(ans)
print(strt-end)

    
