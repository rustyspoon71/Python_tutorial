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
stack.push("Annie Roberts") 
stack.push("Ruth Rodriguez")
stack.push("Richard Roberts")

last_entered = Stack()

# Tell me who was the last person in the building using a stack operation (e.g. size, isEmpty, etc.)
last_person = stack.pop()
last_entered.push(last_person)
print(last_entered.stack_items)
