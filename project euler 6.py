square =0
sum1=0
for i in range(1,101):
    square+=pow(i,2)
    sum1+=i
print(pow(sum1,2)-square)