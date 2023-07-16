def digits(x):
    x=str(x)
    sum=0
    for i in x:
        sum+=int(i)
    return sum
maxi=0
for a in range(1,101):
    for b in range(1, 101):
        num=a**b
        if digits(num)>maxi:
            maxi=digits(num)
print(maxi)
