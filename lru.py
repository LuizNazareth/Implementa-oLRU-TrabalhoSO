from pagina import Pagina
import numpy as np

class Lru:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.paginas = []  # Páginas na memória física. É uma lista de objetos pagina
        self.lru = []  # Armazena diretamente as referências às páginas. É uma lista de objetos pagina

    def referencia_paginas(self, ids_paginas_ref_dentro, ids_paginas_ref_fora, memoria_virtual):
        lista_ref = np.zeros(self.tamanho)
        lista_fora_memoria = []

        # print(f"\nReferenciando páginas: {ids_paginas_ref}")
        print(f"Estado atual da memória física: {[pag.id for pag in self.paginas]}")
        print()

        for id_pag_virtual_dentro in ids_paginas_ref_dentro:
            # Verifica se a página já está na memória física
            pagina_fisica = next((pag for pag in self.paginas if pag.id == id_pag_virtual_dentro), None)
            lista_ref[self.paginas.index(pagina_fisica)] = 1
            
        for id_pag_virtual_fora in ids_paginas_ref_fora:
            lista_fora_memoria.append(memoria_virtual.get_pagina(id_pag_virtual_fora))


        print(f"Lista de referências: {lista_ref}") # lista de 0 ou 1, indicando se a página naquela posição foi referenciada ou não
        print(f"Lista de páginas fora da memória: {[pag.id for pag in lista_fora_memoria]}")
        print()

        self.acessar_pagina(lista_ref)
        self.adiciona_falta_de_pagina(lista_fora_memoria)

        print(f"Estado final da memória física: {[pag.id for pag in self.paginas]}")
        print()

    def acessar_pagina(self, pag_acessadas):
        for idx, pag in enumerate(self.paginas):
            if idx < len(pag_acessadas) and pag_acessadas[idx] == 1:
                pag.referencia()
            else:
                pag.nao_referencia()
        # self.ordena_lru()
        # print(f"Lista LRU ordenada (apos acessos): {[(pag.id, pag.peso) for pag in self.lru]}")

    def ordena_lru(self):
        print("Ordenando a lista LRU")
        # Reordenar a lista LRU baseado nos pesos das páginas
        # A lista lru deve conter os indices do vetor de páginas, ordenado de acordo com o peso de cada pagina contina nesse indice
        self.lru.sort(key=lambda idx_pag: self.paginas[idx_pag].peso, reverse=True)
        # self.lru.sort(key=lambda pag: pag.peso, reverse=True)

    def adiciona_falta_de_pagina(self, lista_fora_memoria):
        for pagina_entra in lista_fora_memoria:
            if len(self.paginas) < self.tamanho:
                # Se ainda há espaço na memória física, adiciona a nova página
                pagina_entra.estado = 1
                self.paginas.append(pagina_entra)
                self.lru.append(0 if(len(self.lru) == 0) else len(self.lru))
                self.paginas[-1].referencia()  
                self.paginas[self.lru[-1]]        
            else:
                self.ordena_lru()
                print(f"Lista LRU ordenada (antes falta de pagina): {[(self.paginas[idx_pag].id, self.paginas[idx_pag].peso) for idx_pag in self.lru]}")

                # Remove a última página da lista LRU (a menos utilizada)
                # pagina_removida = self.lru.pop()
                pagina_removida = self.paginas[self.lru[-1]]
                pagina_removida.estado = 0
                index_removida = self.paginas.index(pagina_removida)
                self.paginas.remove(pagina_removida)

                # Adiciona a nova página na mesma posição da página removida
                self.paginas.insert(index_removida, pagina_entra)
                # self.lru.append(pagina_entra)
                # self.lru.append(index_removida)
                self.paginas[index_removida].referencia()
                # self.ordena_lru()

        print(f"Lista LRU ordenada (apos falta de pagina): {[(self.paginas[idx_pag].id, self.paginas[idx_pag].peso) for idx_pag in self.lru]}")