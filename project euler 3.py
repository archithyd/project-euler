from math import sqrt
def factors(num):
    lis=[]
    i=1
    while i*i<num:
        if num%i==0:
            lis.append(i)
        i+=1
    return prime(lis)


def prime(arr):
    max1=0
    for i in arr:
        val = 0
        j = 1
        while j*j<=i:
            if i%j==0:
                val+=1
            j+=1

        if val==1:
            max1=max(max1,i)
        else:
            pass
    print(max1)

factors(600851475143)