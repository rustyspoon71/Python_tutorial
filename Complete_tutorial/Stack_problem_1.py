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

# Okay our stack is all setup. 

# Problem below:

stack = Stack()
stack.push("Annie Roberts") # First in
stack.push("Ruth Rodriguez") # Second in
stack.push("Richard Roberts") # Last in 

# Tell me who was the last person in the building using a stack operation (e.g. size, isEmpty, etc.)