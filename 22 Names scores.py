file= open(r'C:\Users\ACER\Desktop\project euler\p022_names.txt', 'r')
names=[]
ans=0
names=sorted(file.read().replace('"', '').split(','), key=str)

count= {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10, \
        'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19, \
        'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
def let_count(letter):
    '''letter counting'''
    v=count[letter]
    return v
def get(name):
    x=0
    for i in name:
         
        x+=let_count(i)
    return x    


for name in names:
    ans+=get(name)*((names.index(name)+1))
    
print(ans)
