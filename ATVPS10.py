# Função para busca sequencial
def busca_sequencial(vetor, elemento):
    comparacoes = 0
    for i in range(len(vetor)):
        comparacoes += 1
        if vetor[i] == elemento:
            return comparacoes
    return -1

# Função para busca binária
def busca_binaria(vetor, elemento):
    comparacoes = 0
    inicio = 0
    fim = len(vetor) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if vetor[meio] == elemento:
            return comparacoes
        elif vetor[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# Vetor de exemplo
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 17, 22, 35, 39, 41, 44, 47, 48, 49, 51, 55, 64, 67, 87, 89, 99, 100]

# Elemento a ser buscado
elemento = 48

# Busca sequencial
comparacoes_sequencial = busca_sequencial(vetor, elemento)
if comparacoes_sequencial == -1:
    print("Elemento não encontrado.")
else:
    print("Busca sequencial:")
    print("O elemento foi encontrado em", comparacoes_sequencial, "comparações.")

# Busca binária
comparacoes_binaria = busca_binaria(vetor, elemento)
if comparacoes_binaria == -1:
    print("Elemento não encontrado.")
else:
    print("Busca binária:")
    print("O elemento foi encontrado em", comparacoes_binaria, "comparações.")
