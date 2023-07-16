x=100
fac=1
ans=0
for i in range(1, x+1):
    fac=fac*i
z=str(fac)
for k in range(len(z)):
    ans+=int(z[k])
print(ans)

