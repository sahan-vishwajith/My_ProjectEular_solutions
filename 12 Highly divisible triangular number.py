s=[]
s1=[]
b=0
s3=[]
p=0
for i in range(100000):
    b+=i
    s1.append(b)

s=[]


for i in range(2, 100):
    s.append(i)

for j in s:

    for k in s:
        if k==j:
            pass

        elif k%j==0:
            s.remove(k)


for i in s1:

    m=i
    s3=[]
    s3.append(1)

    for k in s:
        for c in range(1, 10000000):
            n=k*c


            if i**0.5>=n:

                if i%n==0:
                    if n!=i:
                        p=i//n
                        s3.append(n)
                        s3.append(p)



            else:
                break
    s3.append(i)

    if len(list(set(s3)))>500:
        print(i)
        print(s3)
        print('yes')
        break





