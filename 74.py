dict1={'1':1,'2':2,'3':6,'4':24,'5':120,'6':720,'7':5040,'8':40320,'9':362880,'0':1}
def getsum(n):
    n=str(n)
    sume=0
    for i in n:
        sume+=dict1[i]
    return sume

def length(n):
    list1=[]
    x=False
    while x==False:
        z=getsum(n)
        if z in list1:
            x=True
            return len(list1)+1
            break
        list1.append(z)
        n=z

count=0
for i in range(1,1000000):
    if length(i)==60:
        count+=1
print(count)