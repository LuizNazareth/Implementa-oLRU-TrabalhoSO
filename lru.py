from pagina import Pagina
import numpy as np

class Lru: ##classe que representa a memoria fisica
    def _init_(self, tamanho):
        self.tamanho = tamanho
        self.paginas = [] ##estrutura que traz todas as paginas que na memoria fisica, guarda objetos Pagina
        # [pag1, pag2, pag3, pag4, pag5]
        self.lru = range(tamanho) ##estrutura que traz o indice que estao armazenadas na memoria fisica
    
    def referencia_paginas(self, paginas_ref, memoria_virtual):
        # quero saber se a página desse indice já está na memória física
        # se ela estiver, vou referenciar ela
        # se não estiver, e tiver espaço, puxo ela da mem virtual
        # se não tiver espaço, gero falta de página

        lista_ref = np.zeros(len(self.paginas))…
[17:41, 30/08/2024] Mattos: from pagina import Pagina
import random

class Mem_virtual:
    def _init_(self,tam_memoria_virtual, tam_referencia):
        self.tam_memoria_virtual = tam_memoria_virtual
        self.tabela_paginas = [Pagina(i, tam_referencia) for i in range(tam_memoria_virtual)] # lista de páginas na memória virtual

    def get_pagina(self, idx_pagina):
        return self.tabela_paginas[idx_pagina]        

    
    def referencias_virtual_para_fisica(self, pag_acessadas):
        paginas_para_fisica = [] # lista de objetos 

        for idx, pag in enumerate(self.tabela_paginas):
            if pag_acessadas[idx] == 1:
                paginas_para_fisica.append(pag.indice)
            
        return paginas_para_fisica