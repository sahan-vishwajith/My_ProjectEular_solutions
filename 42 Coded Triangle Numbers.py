def letterc(x):
    '''get the alphabatic number of a letter'''
    num={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    C=num[x]
    return C

def triangle(t):
    ''' check that is the number triangle number'''
    if (1+8*t)>=0:
        if (-1+((1+8*t)**0.5))>0 and ((-1+((1+8*t)**0.5))/2)%1==0:
            return True

file=open(r'C:\Users\ACER\Desktop\project euler\p042_words.txt', 'r')
words=sorted(file.read().replace('"', '').split(','), key=str)

twords=0
count=0
for word in words:
    count=0
    for letter in word:
        count+=letterc(letter)
    
    if triangle(count)==True:

        
        twords+=1
print(twords)

