def ans(x,z):
    #z is a llist
    b=z[1]*x+z[0]
    a=z[1]
    return [a,b]
lis=[2, 1]
for i in range(1,100):
    lis.append(i*2)
    lis.append(1)
    lis.append(1)
    if len(lis)>=100:
        break
lis.pop(-1)
lis.pop(-1)
lis=lis[::-1]


lisy=[1,1]

for i in lis:

    lisy=ans(int(i),lisy)

o=str(lisy[1])
hi =0
for u in o:
    hi+=int(u)
print(hi)