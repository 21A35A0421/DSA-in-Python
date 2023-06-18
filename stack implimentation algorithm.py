class Stack:
    def __init__(self):
        self.array=[]
    def push(self,data):
        self.array.append(data)
        print("elemnts in stack is",self.array)
    def pop(self):
        if self.length()==0:
            print("stack is empty")
            return
        return self.array.pop()
    def peek(self):
        if self.length()==0:
            print("no items present in stack")
            return
        return self.array[-1]
    def length(self):
        return len(self.array)
    
stack=Stack()
stack.push(9)
stack.peek()
stack.pop()
stack.peek()
stack.push(69)
  
