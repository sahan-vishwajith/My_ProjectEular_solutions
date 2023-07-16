from time import time
star=time()
l1=[0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, ]
l2=[0, 6, 6, 8, 8, 7, 7, 9, 8, 8, ]
l3=[0, 0, 6, 6, 5, 5, 5, 7,  6, 6]
l4=[7, 3]

name=11
#OneThousand
for j in (range(1, 1000)):
    z=j//100
    i=j%100

    if z>0:
        #print(l1[z]+l4[0])
        if j%100!=0:
            name+=l1[z]+l4[0]+l4[1]
        elif j%100==0:
            name+=l1[z]+l4[0]

    if i==11:
        #print(l2[1])
        name +=l2[1]
    elif i==10:
        #print('ten')
        name +=3
    elif i==12:
        #print(l2[2])
        name +=l2[2]
    elif i==13:
        #print(l2[3])
        name +=l2[3]
    elif i//10==1:
        #print(l2[i%10])
        name +=l2[i%10]
    elif i//10>1:
        x=i//10
        #print(x)
        #print(l3[x])
        name +=l3[x]
        y = (i % 10) // 1
        #print(l1[y])
        name +=l1[y]
    else:
        y = (i % 10) // 1
        #print(l1[y])
        name +=l1[y]
end=time()

print(name)
print(star-end)