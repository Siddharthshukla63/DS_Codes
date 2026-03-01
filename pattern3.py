n=int(input("enterthe number : "))
for i in range(1,n+1): #loop for rows 
    for j in range(1,i+1): #loop for column
        print(j,end="")
    print()  