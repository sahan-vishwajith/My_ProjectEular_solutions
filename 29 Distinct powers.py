num=[]
for i in range(2, 101):
    num.append(i)

ans=[]
for i in num:
    for t in num:
        ans.append(i**t)
ans=list(dict.fromkeys(ans))
print(len(ans))
