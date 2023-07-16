def tri(n):
    v=(n*(n+1))/2
    return v
def checkpenta(p):
    n=(1+((1+24*p)**0.5))/6
    if n%1==0:
        return True
def checkhexa(h):
    n=(1+((1+8*h)**0.5))/4
    if n%1==0:
        return True
x=False
n=285
while x==False:
    n+=1
    v=tri(n)
    if checkpenta(v)==True and checkhexa(v)==True:
        print(int(v))
        x=True
    
    
