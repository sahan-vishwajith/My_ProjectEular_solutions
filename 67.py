use=[]
path=[]
with open('p067_triangle.txt','r')as triangle:
    lisz=(triangle.read().replace(' ','').split('\n'))
    for i in lisz:
        p=[]
        k=list(i)

        if len(k)!=0:
            for t in range(len(k) // 2):
                p.append(int(k[t * 2] + k[(t * 2) + 1]))

            path.append(p.index(max(p)))
            use.append(p)


use=list(reversed(use))

for j in range(1,len(use)):
    for o in range(len(use[j])):
        use[j][o]+=max(use[j-1][o],use[j-1][o+1])
print(use[-1][0])






