from time import time
st=time()
def rever(c):
    c=list(str(c))
    v=reversed(c)
    x=''
    for i in v:
        x+=i
    return int(x)
lychrel=[]
lylist=[]
lyli2=[]
num=[]
x=0
for i in range(9, 10001):
    num.append(i)
for m in num:
    #print(n)
    n=m
    z=0



    for j in range(50):
        z+=1
        n+=rever(n)
        if n < 10000:
            lylist.append(n)
            lylist.append(rever(n))
        if n == rever(n):

            break


    if z==50:

        lychrel.append(m)
end=time()
print(end-st)
print(len(lychrel))

#print(len(num),(num))

