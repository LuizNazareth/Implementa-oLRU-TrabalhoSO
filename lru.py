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

        lista_ref = np.zeros(len(self.paginas))
        lista_fora_memoria = []

        for idx_pag_virtual in paginas_ref:

            for idx_pagina_fisica, pagina_fisica in enumerate(self.paginas):

                if idx_pag_virtual == pagina_fisica.id:
                    lista_ref[idx_pagina_fisica] = 1

                else:
                    if(len(self.paginas) < self.tamanho):
                        # self.paginas.append(Pagina(idx_pag, 8))
                        # iria buscar a página na memória virtual(main.py)
                        self.paginas.append(memoria_virtual.get_pagina(idx_pag_virtual))
                        # verificar se as modificações realizadas no objeto Pagina, agora na Lru, serão refletidas para a main.py
                        # se alterar, ao remover a pag nda memoria fisica, tem que zerar a lista de referencias
                    else:
                        # ele referencia todo mundo do bloco antes de acionar as faltas de página?
                        lista_fora_memoria.append(memoria_virtual.get_pagina(idx_pag_virtual))
                        # self.adiciona_falta_de_pagina(Pagina(pag))


        # tem que realizar as referencias antes de realizar a falta de página
        self.acessar_pagina(lista_ref)
        
        #fora do for chamando a falta de pagina 
        for pagina_virtual_fora in lista_fora_memoria:
            self.adiciona_falta_de_pagina(Pagina(pagina_virtual_fora))

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
        id_remove = self.lru[-1]

        for idx_pagina, pag in enumerate(self.paginas):
            if id_remove == pag.id:
                pagina_removida = self.paginas[idx_pagina]
                # tem que zerar a pagina de referencia
                pagina.referencia()
                self.paginas[idx_pagina] = pagina
                self.ordena_lru()
                break