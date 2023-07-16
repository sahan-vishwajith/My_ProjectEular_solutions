def binary(b):
    '''a decimal number convert to binary number'''
    n=[]
    while b!=0:
       n.append(str(b%2))
       b=b//2
    n=list(reversed(n))

    return n

def deci(d):
    '''check that is the muber palindrome'''
    m=str(d)
    m=list(reversed(m))
    n=''
    for i in m:
        n+=str(i)
    n=int(n)
    return n

ans=0
for i in range(1000000):
    if i==deci(i) and binary(i)==list(reversed(binary(i))):
        ans+=i
print(ans)

