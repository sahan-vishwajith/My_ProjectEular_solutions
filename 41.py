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
max=0

from itertools import permutations
num=[[],[],[],[],[1, 2, 3, 4], [1,2,3,4,5],[1,2,3,4,5,6],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9]]
li=[]
for i in range(4,10):
    li.append(list(permutations(num[i], i)))

n=''
for x in li:
    n=''
    for y in x:
        n=''
        for z in y:
            n+=str(z)
        n=int(n)
        if prime(int(n))==True:
            if max<int(n):
                max=n

print(max)
