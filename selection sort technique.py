array=[11,2,5,3,1,6]
def selection_sort(array):
    for i in range(len(array)):#transering whole array
        min_index=i#making 1st element as initial element
        for j in range(i+1,len(array)):#transversing the array except 1st element
            if array[min_index]>array[j]:#comparing the 1st element with remaining elements of array
                min_index=j#if 1st element is greater than jth element making j as min_index 
        array[i],array[min_index]=array[min_index],array[i]
    return array

data=selection_sort(array)
print(data)