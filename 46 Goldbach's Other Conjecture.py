def ocompo(n):
    if n%2!=0:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return True
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
        
z=False        
u=0
while z==False:
    u+=1
    if ocompo(u)==True:
        n=0
        for x in range(1, int((u/2)**0.5)+1):
            n+=1
            if prime(u-(2*(x**2)))==True:
                z=False
                
                break
            if n==int((u/2)**0.5):
                z=True
                print(u)
        
