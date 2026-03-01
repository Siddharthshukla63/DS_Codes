n =int(input("enter the value of n: "))
for i in range(n):
    p=1
    for j in range(i+1):
        print(chr(p+64),end=" ")
        p+=1
    print()    