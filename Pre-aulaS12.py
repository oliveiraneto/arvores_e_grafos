class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)
            
    def _insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)
        else:
            # if the value already exists in the tree, do nothing
            pass
            
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)

# criando a árvore e inserindo os valores
tree = BinaryTree()
for val in [53,30,14,39,9,23,34,49,72,61,84,79,2,3,27,31]:
    tree.insert(val)

# imprimindo a árvore em ordem
print(tree.inorder_traversal())
