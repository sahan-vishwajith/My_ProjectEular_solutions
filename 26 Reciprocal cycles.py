max=0
ans=0
for i in range(1, 1000):
    x = 1
    y = i
    z = 0
    multi = 0
    sub = 0
    listx = []
    listz = []
    v = -1
    while x != 0:
        listx.append(x)
        z = x // y
        multi = z * y
        sub = x - multi
        x = sub * 10
        if x in listx and x != 0:
            '''print('-', listx.index(x))'''
            v = listx.index(x)
            x = 0
        listz.append(z)
    if len(listz[v:])>max :
        max=len(listz[v:])
        ans=i
print(ans)




