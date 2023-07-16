from itertools import permutations
num={1, 2, 3, 4, 5, 6, 7, 8, 9}
per=list(permutations(num, 4))
ans=[]
for pe in per:

    a=set(num.difference(pe))

    b=list(permutations(a, 1))+list(permutations(a, 2))


    for i in b:
        q=[]
        p=a.difference(i)
        j=[]
        for y in p:
            j.append(str(y))
        c=''
        for x in i:
            c+=str(x)

        d=''
        for z in pe:
            d+=str(z)

        if int(d)%int(c)==0:

            g=int(int(d)//int(c))
            for t in str(g):
                q.append(t)

            if sorted(list(j))==sorted(q):
                ans.append(int(d))
                print(c,'*',g,'=',d)
ans=list(dict.fromkeys(ans))
sum=0
for y in ans:
    sum+=y
print(sum)