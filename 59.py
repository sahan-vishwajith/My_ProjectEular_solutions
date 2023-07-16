from itertools import permutations
text=('abcdefghijklmnopqrstuvwxyz')
x=list(permutations(text, 3))

with open('p059_cipher.txt', 'r') as f:
    file=(f.read().split(','))
ans=0
for y in x:
    perm=(y*(1455//3))
    list1=''
    for u in range(1455):
        list1+=chr(int(file[u])^ord(perm[u]))
    if list1.find('the')>0 and list1.find(('is'))>0 and list1.find('taken')>0:
        for i in list1:
            ans+=ord(i)
        print(ans)
        print(list1)
        break
