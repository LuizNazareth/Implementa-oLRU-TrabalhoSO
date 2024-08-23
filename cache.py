from node import Node

class Cache:
    def __init__(self, tamanho: int):
        self.tamanho = tamanho
        self.cache ={} #utiliza-se um dicionario para fazer consultas mais rapidamente em relação ao nós da lista
        self.cabeca = None #cabeca da lista(mais usada recentemente)
        self.cauda = None #cauda da lista(menos usada recentemente)
        ##ideia de sempre remover a cauda, depois de inserir na cabeca, tornando mais facil a remoção

    def remove_pagina(self, node: Node):
        if node.prev != None:
            node.prev.next = node.next
        else:
            self.cabeca = node.next
        if node.next != None:
            node.next.prev = node.prev
        else:
            self.cauda = node.prev

        del self.cache[node.indice]

    def adiciona_pagina(self, node: Node):
        if self.cabeca == None:
            self.cabeca = node
            self.cauda = node
        else:
            self.cabeca.prev = node
            node.next = self.cabeca
            self.cabeca = node
        self.cache[node.indice] = node

    def acessar_pagina(self, indice: int):
        if indice in self.cache:
            node = self.cache[indice]
            self.remove_pagina(node)
            self.adiciona_pagina(node)
        else:
            node = Node(indice)
            if len(self.cache) >= self.tamanho:
                self.remove_pagina(self.cauda)
            self.adiciona_pagina(node)

    def simulacao(self, acessos: list):
        for i in acessos:
            self.acessar_pagina(i)

    def imprime_cache(self):
        node = self.cabeca
        while node != None:
            print(node.indice, end = " ")
            node = node.next