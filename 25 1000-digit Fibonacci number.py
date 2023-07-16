f0=0
f1=1
log=0
x=1
times=1
while x==1:
    times+=1
    f3=f0+f1
    f0=f1
    f1=f3
    log=f3//10**999
    if log>=1:
        x=0
        print(f3)
        print(times)
