from pagina import Pagina
from lru import Lru
from mem_virtual import Mem_virtual
import random
import sys

# Verifica se foi passado um argumento
if len(sys.argv) > 1:
    tam_memoria_virtual = int(sys.argv[1]) # n paginas na virtual
    tam_memoria_fisica = int(sys.argv[2]) # m paginas na fisica
    tam_referencia = int(sys.argv[3]) # tamanho da lista de controle de referencias. Representa o contador/peso
    num_clocks_simulados = int(sys.argv[3]) # número de clocks simulados
else:
    print("Nenhum argumento recebido.")
    tam_memoria_virtual = 10 # n paginas na virtual
    tam_memoria_fisica = 5 # m paginas na fisica
    tam_referencia = 8 # tamanho da lista de controle de referencias. Representa o contador/peso
    num_clocks_simulados = 4 # número de clocks simulados

mem_virtual = Mem_virtual(tam_memoria_virtual, tam_referencia) # inicializa a memória virtual
mem_fisica = Lru(tam_memoria_fisica) # inicializa a memória física, gerenciada pelo algoritmo LRU

for clk in range(num_clocks_simulados):
    print("Clock: ", clk)
    # sortear quais indices das páginas na memória virtual serão referenciadas
    # sortear n números aleatórios entre 0 e tam_memoria_virtual
    pag_acessadas = [random.randint(0, 1) for i in range(tam_memoria_virtual)]
    print("Páginas acessadas")
    print(pag_acessadas)

    ids_paginas_ref = mem_virtual.referencias_virtual_para_fisica(pag_acessadas) # lista de ids das páginas que foram referenciadas
    mem_fisica.referencia_paginas(ids_paginas_ref, mem_virtual)

# pag_acessadas = [[0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#                  [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
#                  [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
#                  [0, 1, 0, 0, 0, 0, 1, 0, 1, 1]]

# for clk in range(4):
#     print("Clock: ", clk)
#     # sortear quais indices das páginas na memória virtual serão referenciadas
#     # sortear n números aleatórios entre 0 e tam_memoria_virtual
#     # pag_acessadas = [random.randint(0, 1) for i in range(tam_memoria_virtual)]
#     print("Páginas acessadas")
#     print(pag_acessadas[clk])

#     ids_paginas_ref = mem_virtual.referencias_virtual_para_fisica(pag_acessadas[clk]) # lista de ids
#     mem_fisica.referencia_paginas(ids_paginas_ref, mem_virtual)