from time import time
str=time()
def maxi(w):
    if 'A' in w:
        return 'A'
    elif 'K' in w:
        return 'K'
    elif 'Q' in w:
        return 'Q'
    elif 'J' in w:
        return 'J'
    elif 'T' in w:
        return 'T'
    elif '9' in w:
        return '9'
    elif '8' in w:
        return '8'
    elif '7' in w:
        return '7'
    elif '6' in w:
        return '6'
    elif '5' in w:
        return '5'
    elif '4' in w:
        return '4'
    elif '3' in w:
        return '3'
    elif '2' in w:
        return '2'
dict={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14,}


def hicard(sha):
    sha2=[sha[0],sha[2],sha[4],sha[6],sha[8]]
    sha3=[sha[10],sha[12],sha[14],sha[16],sha[18]]
    sha4=[maxi(sha2),maxi(sha3)]
    if  (sha4.index(maxi(sha4)))==0:
        return 'player1'
    else:
        return 'player2'

def pair1(c):
    li1=[c[0], c[2], c[4], c[6], c[8]]
    li2 = [c[10], c[12], c[14], c[16], c[18]]
    l1=[]
    l2=[]
    x1=0
    x2=0
    x3=[]
    for i in li1:
        if not i in l1:
            l1.append(i)
        else:
            x1=i
    for i in li2:
        if not i in l2:
            l2.append(i)
        else:
            x2=i
    if len(l1)==4 and len(l2)==4:
        x3.append(x1)
        x3.append(x2)
        if x1==x2:
            return None
        elif x3.index(maxi(x3))==0:
            return 'player1'
        else:
            return 'player2'
    elif len(l1)==4:
        return 'player1'
    elif len(l2)==4:
        return 'player2'

def pair2(c):
    li1=[c[0], c[2], c[4], c[6], c[8]]
    li2 =[c[10], c[12], c[14], c[16], c[18]]
    l1=[]
    l2=[]
    x1=[]
    x2=[]
    x3=[]
    for i in li1:
        if not i in l1:
            l1.append(i)
        else:
            x1.append(i)
    for i in li2:
        if not i in l2:
            l2.append(i)
        else:
            x2.append(i)
    if len(l1)==3 and len(l2)==3:
        x3.append(maxi(x1))
        x3.append(maxi(x2))
        if x3.index(maxi(x3))==0:
            return 'player1'
        else:
            return 'player2'
    if len(l1)==3 and len(x1)==2:
        return 'player1'
    elif len(l2)==3 and len(x2)==2:
        return 'player2'

def card3(c):
    li1=[c[0], c[2], c[4], c[6], c[8]]
    li2=[c[10], c[12], c[14], c[16], c[18]]
    l1=[]
    l2=[]
    x1=[]
    x2=[]
    x3=[]
    for i in li1:
        if not i in l1:
            l1.append(i)
        elif not i in x1:
            x1.append(i)
    for i in li2:
        if not i in l2:
            l2.append(i)
        elif not i in x2:
            x2.append(i)
    if len(l1)==3 and len(l2)==3 and len(x1)==1 and len(x2)==1:
        x3.append(maxi(x1))
        x3.append(maxi(x2))
        if x3.index(maxi(x3))==0:
            return 'player1'
        else:
            return 'player2'
    elif len(l1)==3 and len(x1)==1:
        return 'player1'
    elif len(l2)==3 and len(x2)==1:
        return 'player2'

def straight(c):
    li1 = sorted([dict[c[0]], dict[c[2]], dict[c[4]], dict[c[6]], dict[c[8]]])
    li2 = sorted([dict[c[10]], dict[c[12]], dict[c[14]], dict[c[16]], dict[c[18]]])

    if (li1[0]+4==li1[-1] and li1[0]+3==li1[-2] and li1[0]+2==li1[-3]and li1[0]+1==li1[-4]) and (li2[0]+4==li2[-1] and li2[0]+3==li2[-2] and li2[0]+2==li2[-3]and li2[0]+1==li2[-4]):
        if li1[-1]>li2[-1]:
            return 'player1'
        else:
            return 'player2'
    elif li1[0]+4==li1[-1] and li1[0]+3==li1[-2] and li1[0]+2==li1[-3]and li1[0]+1==li1[-4]:
        return 'player1'
    elif li2[0]+4==li2[-1] and li2[0]+3==li2[-2] and li2[0]+2==li2[-3]and li2[0]+1==li2[-4]:
        return 'player2'
def flush(c):
    li1 = [c[1], c[3], c[5], c[7], c[9]]
    li2 = [c[11], c[13], c[15], c[17], c[19]]
    l1=[]
    l2=[]
    x1=[]
    x2=[]

    for i in li1:
        if not i in l1:
            l1.append(i)
        if not i in x1:
            x1.append(i)
    for i in li2:
        if not i in l2:
            l2.append(i)
        if not i in x2:
            x2.append(i)
    if (len(l1)==1 and len(x1)==1) and (len(l2)==1 and len(x2)==1):
        return 'player1 and player2'
    elif len(l1)==1 and len(x1)==1:
        return 'player1'
    elif len(l2)==1 and len(x2)==1:
        return 'player2'

def fullho(c):
    li1 = ([dict[c[0]], dict[c[2]], dict[c[4]], dict[c[6]], dict[c[8]]])
    li2 = ([dict[c[10]], dict[c[12]], dict[c[14]], dict[c[16]], dict[c[18]]])
    l1 = []
    l2 = []
    x1 = []
    x2 = []

    for i in li1:
        if not i in l1:
            l1.append(i)
        elif not i in x1:
            x1.append(i)
    for i in li2:
        if not i in l2:
            l2.append(i)
        elif not i in x2:
            x2.append(i)
    if (len(l1) == 2 and len(x1) == 2) and (len(l2) == 2 and len(x2) == 2):
        if li1.count(l1[0]) == 3:
            x3 = l1[0]
        elif li1.count(l1[1]) == 3:
            x3 = l1[1]
        if li2.count(l2[0]) == 3:
            x4 = l2[0]
        elif li2.count(l2[1]) == 3:
            x4 = l2[1]
        if x3 > x4:
            return 'player1'
        elif x3 < x4:
            return 'player2'
    elif len(l1) == 2 and len(x1) == 2:
        return 'player1'
    elif len(l2) == 2  and len(x2) == 2:
        return 'player2'

def card4(c):
    li1=[c[0], c[2], c[4], c[6], c[8]]
    li2 = [c[10], c[12], c[14], c[16], c[18]]
    l1=[]
    l2=[]
    x1=[]
    x2=[]
    x3=0
    x4=0
    for i in li1:
        if not i in l1:
            l1.append(i)
        else:
            x1.append(i)
    for i in li2:
        if not i in l2:
            l2.append(i)
        else:
            x2.append(i)
    if (len(l1)==2 and len(x1)==3) and (len(l2)==2 and len(x2)==3):
        if li1.count(l1[0])==4:
            x3=l1[0]
        elif li1.count(l1[1])==4:
            x3=l1[1]
        if li2.count(l2[0])==4:
            x4=l2[0]
        elif li2.count(l2[1])==4:
            x4=l2[1]
        if x3>x4:
            return 'player1'
        elif x3<x4:
            return 'player2'
    elif len(l1)==2 and len(x1)==1:
        return 'player1'
    elif len(l2)==2 and len(x2)==1:
        return 'player2'
def straflu(c):
    if (straight(c)=='player1') and (flush(c)=='player1' or flush(c)=='player1 and player2'):
        return 'player1'
    elif (straight(c)=='player2') and (flush(c)=='player2' or flush(c)=='player1 and player2'):
        return 'player2'

def royal(c):
    if flush(c)=='player1' or flush(c)=='player1 and player2':
        li1 = [c[0], c[2], c[4], c[6], c[8]]

        if ('T' in li1) and ('J' in li1) and ('Q' in li1) and ('K' in li1) and('A' in li1):
            return 'player1'
    elif flush(c) == 'player1' or flush(c) == 'player1 and player2':
        li2 = [c[10], c[12], c[14], c[16], c[18]]
        if ('T' in li2) and ('J' in li2) and ('Q' in li2) and ('K' in li2) and('A' in li2):
            return 'player2'


helo=[]
n=0
with open('p054_poker.txt', 'r')as poker:
    le=(poker.read().replace(' ', ',').split('\n'))
    for u in le:
        helo.append(list(u))
    helo.pop(-1)
    for c in helo:

        if royal(c)=='player1':
            n+=1
        elif royal(c) == 'player2':
            pass
            print(c, '*******1')
        elif straflu(c) == 'player1':
            n += 1
        elif straflu(c) == 'player2':
            print(c, '*******2')
            pass
        elif card4(c) == 'player1':
            n += 1
            print(c, '*******3')
        elif card4(c) == 'player2':
            pass
            print(c, '*******3')
        elif fullho(c)== 'player1':
            n+=1
        elif fullho(c) == 'player2':
            pass
            #print(c, '*******4')
        elif flush(c) == 'player1':
            n += 1
        elif flush(c) == 'player2':
            pass
            #print(c, '*******5')
        elif straight(c) == 'player1':
            n += 1
            #print(c, '*******6')
        elif straight(c) == 'player2':
            pass

        elif card3(c) == 'player1':
            n += 1

        elif card3(c) == 'player2':
            pass
            #print(c, '*******7')
        elif pair2(c) == 'player1':
            n += 1
            #print(c[0], c[2], c[4], c[6], c[8],'|',c[10], c[12], c[14], c[16], c[18])

        elif pair2(c) == 'player2':
            pass

            #print(c, '*******8')
        elif pair1(c) == 'player1':
            n += 1

        elif pair1(c) == 'player2':
            pass
            #print(c, '*******9')
        elif hicard(c) == 'player1':
            n += 1
        elif hicard(c) == 'player2':
            pass
            #print(c, '*******10')
end=time()
print(n)
print(end - str)
