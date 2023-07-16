pri=[]
ans=[]
def prime(x):
    if x==2:
        return True
    elif x>2:
        for i in range(2, int(x**0.5)+1):
            if x%i==0:
                return False
                break

        return True
for v in range(2, 1000000):
    if prime(v)==True:
        pri.append(v)
for i in pri:

    v = []
    i=str(i)
    for a in i:
        v.append(a)
    p=0
    for b in range(len(i)-1):
        x=v[0]
        v.remove(x)
        v.append(x)
        z=''
        for n in v:
            z+=str(n)

        if prime(int(z))==True:
            p+=1

        else:
            break
    if p==len(i)-1:
        ans.append(i)
print(ans)
print(len(ans))
print(prime(98765431))





