ans =0
count=0
for i in range(1,500000):
    if count<10001:
        val = 0
        j=1
        while j*j<=i:
            if i%j==0:
                val+=1
            j+=1
        if val==1 and i!=1:
            count+=1
            ans = i

print(ans)
