from itertools import combinations
def prime(num):
    """if the number is prime then print 1"""
    if num==1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
            break
    else:
        return True

m=0
listpri=[]
for u in range(10000):
    if prime(u)==True:
        listpri.append(str(u))
#print(listpri)
sa=False
while sa==False:
    m+=1
    n=str(m)
    if prime(m)==True:
        for i in range(len(n) - 1):
            x = (n[:i + 1])
            if x[0]=='0':
                break
            y = (n[i + 1:])
            if y[0]=='0':
                break
            if prime(int(x)) == True:
                #print(x)
                if prime(int(y)) == True:
                    # print(x, y)
                    if prime(int((y) + (x))) == True:
                        listx=[x,]
                        listz=[]
                        for z in listpri:
                            if prime(int(x+z)):
                                if prime(int(z+x)):
                                    if prime(int(y+z)):
                                        if prime(int(z+y)):
                                            listz.append(int(z))
                        listcom=list(combinations(listz,3))
                        for com in listcom:
                            if prime(int(str(com[0])+str(com[1])))==True:
                                if prime(int(str(com[1]) + str(com[0])))==True:
                                    if prime(int(str(com[1]) + str(com[2])))==True:
                                        if prime(int(str(com[2]) + str(com[1])))==True:
                                            if prime(int(str(com[2]) + str(com[0])))==True:
                                                if prime(int(str(com[0]) + str(com[2])))==True:
                                                    print(com[0]+com[1]+com[2]+int(x)+int(y))
                                                    sa=True
                                                    break
