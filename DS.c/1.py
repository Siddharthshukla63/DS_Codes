arr1 =[1,5,10,20,40,80]
arr2 =[6,7,20,80,100]
arr3 =[3,4,15,20,30,70,80,120]
result = set(arr1) & set(arr2) & set(arr3)
print("Common elements in three arrays:", list(result))