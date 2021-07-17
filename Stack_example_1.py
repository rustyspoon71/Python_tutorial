class Stack:
     def __init__(self):
         self.stack_items = []

     def isEmpty(self):
         return self.stack_items == []

     def push(self, item):
         self.stack_items.append(item)

     def pop(self):
         return self.stack_items.pop()

     def size(self):
         return len(self.stack_items)

stack = Stack()
stack.push(3)
stack.push(4)
stack.pop()
print(stack.stack_items)