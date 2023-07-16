s=[]
v=[]
sum1=0
sum2=0
ans=[]
answ=0
for i in range(1, 10000 ):

    sum1=1
    sum2=1
    for j in range(2, int(i**0.5)+1):
        if i%j==0:


            sum1+=j

            sum1+=i/j

    for l in range(2, int(sum1**0.5)+1):
        if sum1%l==0:
            sum2+=l
            sum2+=sum1//l
    if i==sum2 and sum1<10000 and sum2<10000 and sum1!=sum2:
        ans.append(sum1)
        answ+=sum1

print(ans)
print(answ)