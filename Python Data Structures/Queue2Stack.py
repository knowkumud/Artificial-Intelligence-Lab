#Implementation of queue using stack
class Stack: 
    def __init__(self): 
        self.items = [] 
     
    def push(self, item): 
        self.items.append(item) 
        
    def pop(self): 
        return self.items.pop() if self.items else None   

    def top(self): 
        return self.items[-1] if self.items else None 
    
    def display(self):
        for i in self.items:
            print(i,end = " ")

    def is_empty(self): 
        return not self.items 
if __name__ == "__main__":
    stk1 = Stack()
    stk2 = Stack()
    print("Enqueue of 1-10 into queue: ")
    for i in range(1, 11):
        stk1.push(i)
    print("Queue contents: ")
    print(stk1.display())
    print("Removing 5 elements from queue: ")
    for i in range(10):
        stk2.push(stk1.pop())
    for i in range(5):
        print("Dequeue: ",stk2.pop())
    for i in range(10-5):
        stk1.push(stk2.pop())
    print("Queue contents: ")
    print(stk1.display())
