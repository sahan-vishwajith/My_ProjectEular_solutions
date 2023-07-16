ans=[]
num=[]
for i in range(11, 100):
    if i%10!=0:
        num.append(i)

b=0
for x in num:
    b=num

    for y in b:
        v=str(y)
        w=str(x)

        if y>x:
            z=x/y
            if (int(w[0])/int(v[0]))==z and w[1]==v[1]:
                ans.append(z)
                print(w, '/', v, '=', z)
            if (int(w[0])/int(v[1]))==z and w[1]==v[0]:
                ans.append(z)
                print(w, '/', v, '=', z)
            if  (int(w[1])/int(v[0]) and w[0]==v[1])==z:
                ans.append(z)
                print(w, '/', v, '=', z)
            if (int(w[1])/int(v[1]) and w[0]==v[0])==z:
                ans.append(z)
                print(w, '/', v, '=', z)
v=1
print(ans)
for an in ans:
   v=v*(1/an)
print(v)




