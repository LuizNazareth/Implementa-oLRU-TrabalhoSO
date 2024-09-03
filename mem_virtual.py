from pagina import Pagina
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