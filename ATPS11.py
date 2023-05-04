class ArvoreBinaria:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.arvore = [None] * tamanho
        self.raiz = None

    def criar_arvore(self, raiz):
        self.raiz = raiz
        self.arvore[0] = raiz

    def inserir_elemento(self, elemento):
        if self.raiz is None:
            self.raiz = elemento
            self.arvore[0] = elemento
        else:
            posicao = self.arvore.index(None)
            pai = (posicao - 1) // 2
            if posicao % 2 == 0:
                self.arvore[posicao] = elemento
                self.arvore[pai].direita = elemento
            else:
                self.arvore[posicao] = elemento
                self.arvore[pai].esquerda = elemento

    def construir_arvore(self, lista):
        repetidos = []
        for elemento in lista:
            if self.raiz is None:
                self.raiz = elemento
                self.arvore[0] = elemento
            else:
                posicao = self.arvore.index(None)
                pai = (posicao - 1) // 2
                if posicao % 2 == 0:
                    self.arvore[posicao] = elemento
                    self.arvore[pai].direita = elemento
                else:
                    self.arvore[posicao] = elemento
                    self.arvore[pai].esquerda = elemento
            if lista.count(elemento) > 1 and elemento not in repetidos:
                repetidos.append(elemento)
        return repetidos
    
arvore = ArvoreBinaria(15)
arvore.criar_arvore(1)
arvore.inserir_elemento(2)
arvore.inserir_elemento(3)
arvore.inserir_elemento(4)
arvore.inserir_elemento(5)
arvore.inserir_elemento(6)
arvore.inserir_elemento(7)
arvore.inserir_elemento(8)
arvore.inserir_elemento(9)
arvore.inserir_elemento(10)
arvore.inserir_elemento(11)
arvore.inserir_elemento(12)
arvore.inserir_elemento(13)
arvore.inserir_elemento(14)
arvore.inserir_elemento(15)
repetidos = arvore.construir_arvore([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 14, 13])
print(repetidos)

