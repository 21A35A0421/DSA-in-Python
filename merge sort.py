def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//1#finding the mid value
    left=merge_sort(arr[:mid])#dividing the left part of array recursively
    right=merge_sort(arr[mid:])#dividnig right part of array  recursively
    return merged(left,right)#merging the left and right parts of array useing a fun called merged
def merged(left,right):
    merged=[]#creating an empty list to store the merged elements
    i=j=0#used to point the elemnts of arrays
    while i<len(left) and i<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged+=left[i:]+right[j:]
    return merged
arr=[34,2,56,1,7]
result=merge_sort(arr)
print(result)