array=[32,1,45,89,2,5,5]
def bubblesort(array):
    for i in range(len(array)):#transversing whole array
        for j in range(0,len(array)-i-1):#comparing two elements
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
print(bubblesort(array))