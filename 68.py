from itertools import permutations
num=[1,2,3,4,5,6,7,8,9,10]
num2=[1,2,3,4,5]
r=[6,7,8,9,10]
max=0
def su(x,y,z):
    if x+y+z==14:
        return True
    else:
        return False
list1= list(permutations(num,10))

for i in list1:
    z=[]
    if su(i[0],i[1],i[7])==True and su(i[1],i[2],i[8])==True and su(i[2],i[3],i[9])==True and su(i[3],i[4],i[5])==True and su(i[4],i[0],i[6])==True :

        a=(i[7],i[1],i[0])
        e=(i[8], i[2], i[1])
        d=(i[9], i[3], i[2])
        c=(i[5], i[4], i[3])
        b=(i[6], i[0], i[4])
        z.append(a)
        z.append(b)
        z.append(c)
        z.append(d)
        z.append(e)
        if z[0][0]==6:
            k=''
            for j in z:
                for t in j:
                    k+=str(t)

            if max<=int(k):

                max=int(k)

print(max)




