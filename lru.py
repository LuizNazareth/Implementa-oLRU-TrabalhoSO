from pagina import Pagina

class Lru: ##classe que representa a memoria fisica
    def __init__(self, tamanho, paginas):
        self.tamanho = tamanho
        self.paginas = paginas ##estrutura que traz todas as paginas que na memoria fisica
        # [pag1, pag2, pag3, pag4, pag5]
        self.lru = range(tamanho) ##estrutura que traz o indice que estao armazenadas na memoria fisica
        
    def acessar_pagina(self, pag_acessadas):
        #[1, 0, 0, 1, 1]
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


    def adiciona_pagina(self, pagina):
        idx_remove = self.lru[-1]
        pagina_removida = self.paginas[idx_remove]
        self.paginas[idx_remove] = pagina
        pagina.referencia()
        self.ordena_lru()