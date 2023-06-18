class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
array=[3,4,5,6,7,8,9]

def create_binary_tree(array,root,i,n):#n=length of array and i=1(sine array is an 1 indexed array)
    if i<n:
        root=Treenode(array[i-1])#creatinding an node value 
        root.left=create_binary_tree(array,root.left,2*i,n)
        root.right=create_binary_tree(array,root.right,2*i+1,n)
    return root
root=None
binarytree=create_binary_tree(array,root,1,len(array)+1)    
print(binarytree)
