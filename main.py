from pagina import Pagina
from lru import Lru
from mem_virtual import Mem_virtual
import random




tam_memoria_virtual = 10 # teria n paginas na virtual
tam_memoria_fisica = 5 # teria m paginas na fisica

tam_referencia = 8

mem_virtual = Mem_virtual(tam_memoria_virtual, tam_referencia)
mem_fisica = Lru(tam_memoria_fisica)

for clk in range(10):
    print("Clock: ", clk)
    # sortear quais indices das páginas na memória virtual serão referenciadas
    # sortear n números aleatórios entre 0 e tam_memoria_virtual
    pag_acessadas = [random.randint(0, 1) for i in range(tam_memoria_virtual)]
    print("Páginas acessadas")
    print(pag_acessadas)       

    paginas_ref = mem_virtual.referencias_virtual_para_fisica(pag_acessadas)
    mem_fisica.referencia_paginas(paginas_ref)