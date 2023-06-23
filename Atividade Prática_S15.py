class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes_non_recursive(root):
    if root is None:
        return 0
    
    stack = [root]
    count = 0
    
    while stack:
        node = stack.pop()
        count += 1
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return count

def count_nodes_recursive(root):
    if root is None:
        return 0
    
    return 1 + count_nodes_recursive(root.left) + count_nodes_recursive(root.right)

def sum_values_non_recursive(root):
    if root is None:
        return 0
    
    stack = [root]
    total_sum = 0
    
    while stack:
        node = stack.pop()
        total_sum += node.value
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return total_sum

def sum_values_recursive(root):
    if root is None:
        return 0
    
    return root.value + sum_values_recursive(root.left) + sum_values_recursive(root.right)

def tree_height_non_recursive(root):
    if root is None:
        return 0
    
    stack = [(root, 1)]
    height = 0
    
    while stack:
        node, current_height = stack.pop()
        height = max(height, current_height)
        
        if node.left:
            stack.append((node.left, current_height + 1))
        if node.right:
            stack.append((node.right, current_height + 1))
    
    return height

def tree_height_recursive(root):
    if root is None:
        return 0
    
    left_height = tree_height_recursive(root.left)
    right_height = tree_height_recursive(root.right)
    
    return 1 + max(left_height, right_height)

# Criação dos nós
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Configuração dos nós filhos
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

# Testando os algoritmos
print("Número de nós (não recursivo):", count_nodes_non_recursive(node1))
print("Número de nós (recursivo):", count_nodes_recursive(node1))
print("Soma dos valores (não recursivo):", sum_values_non_recursive(node1))
print("Soma dos valores (recursivo):", sum_values_recursive(node1))
print("Altura da árvore (não recursivo):", tree_height_non_recursive(node1))
print("Altura da árvore (recursivo):", tree_height_recursive(node1))
