array=[3,4,2,6,8,9]
n=6#lengeth of the array
x=9#element to find
def linearsearch(array,n,x):
    for i in range(0,n):
         if array[i]==x:
            return i
    return -1  
result=linearsearch(array,n,x)
print(result)