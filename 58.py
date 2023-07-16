def prime(num):
    """if the number is prime then print 1"""
    if num==1:
        c=0
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            c = 0
            return False
            break
    else:

        return True

n=0
num=1
z=0
x=0
s=False
while s==False:
    n+=2
    for j in range(4):
        num+=n

        z+=1
        if prime(num)==True:
            x+=1
        if int((x/z)*100)<10:

            s=True
            break
print(n-1)
