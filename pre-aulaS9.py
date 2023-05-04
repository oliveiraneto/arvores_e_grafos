# Definição da classe do nó da lista
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Função para buscar um elemento na lista encadeada
def search(head, key):
    # Percorre a lista até encontrar o elemento ou chegar ao final
    current = head
    while current is not None:
        if current.data == key:
            return current  # Retorna o nó encontrado
        current = current.next
    return None  # Retorna nulo se o elemento não for encontrado
