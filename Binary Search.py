#binary searching algorithem(applies olny when array is sorted)
array=[2,3,1,5,7,11]
x=11
def binarysearch(array,x,low,high):
    mid=high-low//2
    if low<=high:
        if array[mid]==x:
            return mid
        elif array[mid]>x:
            return binarysearch(array,x,low,mid-1)
        elif array[mid]<x:
            binarysearch(array,array,x,mid+1,high)
    return -1
result=(binarysearch(array,x,0,len(array)-1))
print(result)
