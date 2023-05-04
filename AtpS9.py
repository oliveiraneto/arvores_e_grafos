def busca_sequencial(vetor, valor):
    comp = 0
    for i in range(len(vetor)):
        comp += 1
        if vetor[i] == valor:
            return i, comp
    return -1, comp

vetor = [1, 2, 5, 7, 10, 12, 13, 14, 16, 20]
media = sum(vetor) / len(vetor)

mais_proximo = vetor[0]
dist_mais_proximo = abs(vetor[0] - media)
comp = 0

for i in range(len(vetor)):
    dist_atual = abs(vetor[i] - media)
    if dist_atual < dist_mais_proximo:
        mais_proximo = vetor[i]
        dist_mais_proximo = dist_atual
    comp += 1

indice, comp_busca = busca_sequencial(vetor, mais_proximo)

print("O valor mais próximo da média é:", mais_proximo)
print("Quantidade de comparações na busca sequencial:", comp_busca)
