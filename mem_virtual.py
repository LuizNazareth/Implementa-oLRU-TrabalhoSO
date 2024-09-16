from pagina import Pagina
import random

class Mem_virtual:
    def __init__(self,tam_memoria_virtual, tam_referencia):
        self.tam_memoria_virtual = tam_memoria_virtual
        self.tabela_paginas = [Pagina(i*10, tam_referencia) for i in range(tam_memoria_virtual)] # lista de páginas na memória virtual

    def get_pagina(self, id_pagina):
        for idx, pag_fis in enumerate(self.tabela_paginas):
            if pag_fis.id == id_pagina:
                return self.tabela_paginas[idx]      

    
    def referencias_virtual_para_fisica(self, pag_acessadas):
        paginas_para_fisica = [] # lista de objetos

        for idx, pag in enumerate(self.tabela_paginas):
            # print(idx)
            if pag_acessadas[idx] == 1:
                paginas_para_fisica.append(pag.id)
            
        return paginas_para_fisica