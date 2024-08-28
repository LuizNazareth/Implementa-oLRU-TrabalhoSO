from pagina import Pagina
from lru import Lru
import random

def envia_pagina(idx_pagina):
    return tabela_paginas[idx_pagina]

tam_memoria_virtual = 10 # teria n paginas na virtual
tam_memoria_fisica = 5 # teria m paginas na fisica

tam_referencia = 8

tabela_paginas = [Pagina(i, tam_referencia) for i in range(tam_memoria_virtual)] # lista de páginas na memória virtual

# print("Tabela de páginas")
# for pag in tabela_paginas:
#     print(pag.indice)
#     print(pag.lista_referencia)

# executar 10 passagens de clock

for clk in range(10):
    print("Clock: ", clk)
    # sortear quais indices das páginas na memória virtual serão referenciadas
    # sortear n números aleatórios entre 0 e tam_memoria_virtual
    idx_pag_acessadas = [random.randint(0, 1) for i in range(tam_memoria_virtual)]
    print("Páginas acessadas")
    print(idx_pag_acessadas)

    # paginas_para_virtual = []

    # for idx, pag in enumerate(tabela_paginas):
    #     if pag_acessadas[idx] == 1 and idx < tam_memoria_fisica:
    #         paginas_para_virtual.append(pag)
    #     elif pag_acessadas[idx] == 1 and idx >= tam_memoria_fisica:
    