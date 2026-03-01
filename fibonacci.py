a,b=0,1
print(a,end=' ')
n=int(input("enter the number of terms: "))
for i in range(2,n):
    c=a+b
    print(c,end=' ')
    a=b
    b=c