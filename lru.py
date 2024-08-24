from pagina import Pagina

class Lru:
    def __init__(self, tamanho: int, paginas):
        self.tamanho = tamanho
        self.paginas = paginas ##estrutura que traz todas as paginas que estao armazenadas na cache
        
    def acessar_pagina(self, vector_pag_acessadas):
        for i in vector_pag_acessadas:
            
        
    