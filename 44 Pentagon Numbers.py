def pentagon(n):
    d=int((3*(n**2)-n)/2)
    return d
def checkpenta(p):
    n=(1+(1+(4*2*3*p))**0.5)/6
    if n>0 and n%1==0:
        return True
    else:
        return False

penta=[1,]
x=False
n=0
while x==False:
    n+=1
    for i in penta:
        if checkpenta(pentagon(n)+i)==True:
            if checkpenta(pentagon(n)-i)==True:
                print(pentagon(n)-i)
                x=True
                break
    penta.append(pentagon(n))
