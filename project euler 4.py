max1=0
for i in range(900,999):
    for j in range(999,990,-1):
        val = i*j
        rev_val=str(val)
        if str(val)==rev_val[::-1]:
            max1=max(max1,i*j)
print(max1)