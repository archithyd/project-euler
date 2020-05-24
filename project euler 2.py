a = [1,2]
ans=0
for i in range(2,100):
    val = a[i-1]+a[i-2]
    if val<4000000 and val%2==0:
        ans+=val
    a.append(a[i-1]+a[i-2])

print(ans+2)