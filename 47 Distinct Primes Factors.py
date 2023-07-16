def prime(p):
    if p==1:
        return False
    elif p==2:
        return True
    elif p>2:
        for y in range(2, int(p**0.5)+1):
            if p%y==0:
                return False

                break
        return True

x=False
v=1
b=[]
c=[]
s1=False
s2=False
s3=False
s4=False
n1=0
n2=0
n3=0
n4=0
while x==False :
    v+=1
    n=v
    b=[]
    n1=n2
    n2=n3
    n3=n4
    n4=v
    s1 = s2
    s2 = s3
    s3 = s4
    s4 = False
    for i in range(2, int(n**0.5)+1):
        n=v
        if n%i==0:

            n = n / i
            if i not in b and prime(i)==True:
                b.append(i)

                for j in range(2, int(n**(1/3)) + 1):
                    if n % j == 0:
                        n = n / j
                        if j not in b and prime(j)==True:
                            b.append(j)

                            for k in range(2, int(n**0.5) + 1):
                                if n % k == 0:
                                    n=int(n/k)
                                    if k not in b and prime(k)==True:
                                        b.append(k)
                                        if n not in b and prime(n)==True:

                                            b.append(n)

                                            s4 = True


    if s1==True and s2==True and s3==True and s4==True:
        x=True
        print("yee",n1)
