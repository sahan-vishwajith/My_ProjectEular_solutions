pluse=0
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


x=0
num = 0
op=1000000
n=0
while n<op:
    n+=1
    z = 0

    pluse=0
    while pluse < 1000000:
        n += 1
        if prime(n) == True:
            pluse += n
            z += 1

            if prime(pluse) == True and pluse<1000000:

                if x<z:
                    x = z


                    num = pluse

print(x, num)
