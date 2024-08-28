from pagina import Pagina
import numpy as np
from main import enviar_pagina

class Lru: ##classe que representa a memoria fisica
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.paginas = [] ##estrutura que traz todas as paginas que na memoria fisica, guarda objetos Pagina
        # [pag1, pag2, pag3, pag4, pag5]
        self.lru = range(tamanho) ##estrutura que traz o indice que estao armazenadas na memoria fisica
    
    def referencia_paginas(self, paginas_ref):
        # recebe um vetor de índices de páginas virtuais que foram referenciadas
        # idx [6, 7, 3, 5]
        # se a pagina ja esta na memoria fisica, ela é referenciada, se não, ela é adicionada
        # caso ainda tenha espaço na memoria fisica, não causará falta de página
        # caso não tenha espaço na memoria fisica, causará falta de página, tendo que remover uma página da lru

        # se a função não encontrar uma página com indice passado na self.paginas, ela adiciona a pagina na memoria fisica, pegando ela da memória virtual

        lista_ref = np.zeros(len(self.paginas))
        lista_fora_memoria = []
        for idx_pag in paginas_ref:
            if(idx_pag in self.paginas):
                lista_ref[self.paginas.index(idx_pag)] = 1
        
            else:
                if(len(self.paginas) < self.tamanho):
                    # self.paginas.append(Pagina(idx_pag, 8))
                    # iria buscar a página na memória virtual(main.py)
                    self.append(enviar_pagina(idx_pag))
                    # verificar se as modificações realizadas no objeto Pagina, agora na Lru, serão refletidas para a main.py
                    # se alterar, ao remover a pag nda memoria fisica, tem que zerar a lista de referencias
                else:
                    # ele referencia todo mundo do bloco antes de acionar as faltas de página?
                    lista_fora_memoria.append(pag)
                    # self.adiciona_falta_de_pagina(Pagina(pag))

        # tem que realizar as referencias antes de realizar a falta de página
        self.acessar_pagina(lista_ref)
        
        #fora do for chamando a falta de pagina 
        for pag in lista_fora_memoria:
            self.adiciona_falta_de_pagina(Pagina(pag))

    def acessar_pagina(self, pag_acessadas): #recebe uma lista que indica se as páginas na memória fisica foram referenciadas ou não
        #     [1, 0, 0, 1, 1]
        # idx [7, 3, 5, 2, 4]
        for idx, pag in enumerate(self.paginas):
            if(pag_acessadas[idx] == 1):
                pag.referencia()
            else:
                pag.nao_referencia()
        self.ordena_lru()

                
    def ordena_lru(self):
        print("Ordenando paginas")
        ##percorrer as paginas e ordená a lista lru de acordo com os pesos das paginas

        self.lru = sorted(self.lru, key=lambda x: self.paginas[x].peso)


    def adiciona_falta_de_pagina(self, pagina):
        idx_remove = self.lru[-1]
        pagina_removida = self.paginas[idx_remove]
        self.paginas[idx_remove] = pagina
        pagina.referencia()
        self.ordena_lru()