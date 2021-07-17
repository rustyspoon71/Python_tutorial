class Tree:

    class Node:
        def __init__(self,data): 
            self.data = data
            self.left = None   
            self.right = None
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Tree.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self,data,node):
        if data == node.data:
            return 
        if data < node.data:
            if node.left is None:
                node.left = Tree.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Tree.Node(data)
            else:
                self._insert(data, node.right)
                
    def search(self, data):
        return self._contains(data, self.root)  

    def _contains(self, data, node):
        if data == node.data:
            return True
        else:
            if data < node.data:
                if node.left is None:
                    return False
                elif node.left is not None:    
                    return self._contains(data,node.left)
            if data > node.data:
                if node.right is None:
                    return False
                elif node.left is not None: 
                    return self._contains(data,node.right)
        return False

    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def __reversed__(self):        
        yield from self._traverse_backward(self.root)  # Start at the root
    def _traverse_backward(self, node):
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root
    def _get_height(self, node):        
        if node == None:
            return 0 
        else:
            return  1 + max(self._get_height(node.left),self._get_height(node.right))
# Code that runs the tree
tree_BST = Tree()
tree_BST.insert(3)
tree_BST.insert(4)
tree_BST.insert(1)
print("This is the height: ",tree_BST.get_height())
print(" ")
for x in tree_BST:
    print("Smallest to Largest: ",x)
print("  ")
for x in reversed(tree_BST):
    print("Largest to Smallest: ",x)
print(" ")
print("Is 4 in the Tree? T/F: ",tree_BST.search(4))
print("Is 5 in the Tree? T/F: ",tree_BST.search(5))
print(" ")
