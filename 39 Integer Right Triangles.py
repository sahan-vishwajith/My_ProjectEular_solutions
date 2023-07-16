max=0
ans=0
for p in range(1, 1000):
    n=0
    for a in range(1, int((p*(2**0.5)/(2+(2**0.5)))/(2**0.5))+1):
        b1=((p**2)-(2*p*a))/(2*p-2*a)
        if (b1//1)==(b1) and int(b1)!=0:

            n+=1
            if max<n:
                max=n
                ans=p



print(ans)
