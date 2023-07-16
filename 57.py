def frac(x,y,a,b):
    c=a*x
    d=b*y
    p=c+d
    return p,a
def digitco(x):
    x=str(x)
    return len(x)
ans=0
for n in range(1000):
    a=2
    b=1
    for i in range(n):
        x=frac(2,1,a,b)
        a=x[0]
        b=x[1]
    z=frac(1,1,a,b)
    if digitco(z[0])>digitco(z[1]):
        ans+=1

print(ans)
