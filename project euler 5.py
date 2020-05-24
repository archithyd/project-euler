lis1=[]
ans_lis=[]
dec={}
value=0

for i in range(2,10):
    lis1.append(i)


for i in lis1:
    for j in range(1,i+1):
        if i%j==0:
            ans_lis.append(j)

print(ans_lis)
for i in ans_lis:
    if i in dec:
        dec[i]+=1
    else:
        dec[i]=1


print(dec)

#NOT COMPLETE


