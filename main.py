from cache import Cache

if __name__ == "__main__":
    # print("Digite o tamanho da cache:")
    # tamanho = int(input())
    
    tamanho = 3

    cache = Cache(tamanho)

    acessos_paginas = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    cache.simulacao(acessos_paginas)

    cache.imprime_cache()