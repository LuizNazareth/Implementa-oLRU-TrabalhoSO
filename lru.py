from pagina import Pagina
import numpy as np

class Lru:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.paginas = []  # Páginas na memória física. É uma lista de objetos pagina
        self.lru = []  # Armazena diretamente as referências às páginas. É uma lista de objetos pagina

    def referencia_paginas(self, ids_paginas_ref, memoria_virtual):
        lista_ref = np.zeros(self.tamanho)
        lista_fora_memoria = []

        print(f"\nReferenciando páginas: {ids_paginas_ref}")
        print(f"Estado atual da memória física: {[pag.id for pag in self.paginas]}")
        print()

        for id_pag_virtual in ids_paginas_ref:
            # Verifica se a página já está na memória física
            pagina_fisica = next((pag for pag in self.paginas if pag.id == id_pag_virtual), None)

            if pagina_fisica:##modificação luiz, esse if estava errado
                # Página já está na memória, somente atualiza a referência
                lista_ref[self.paginas.index(pagina_fisica)] = 1 
            else:
                # if len(self.paginas) < self.tamanho:
                #     # Adiciona nova página se há espaço na memória física
                #     nova_pagina = memoria_virtual.get_pagina(id_pag_virtual)
                #     self.paginas.append(nova_pagina)
                #     lista_ref[len(self.paginas) - 1] = 1
                #     # Atualiza a lista LRU
                #     self.lru.append(nova_pagina)

                #     # VERIFICAR SE É AQUI QUE ADICIONAMOS AS PAGINAS OU SE É PELA FUNÇÃO ADICIONA_FALTA_DE_PAGINA
                # else:
                #     # Se não há espaço, precisa substituir uma página existente
                #     lista_fora_memoria.append(memoria_virtual.get_pagina(id_pag_virtual))

                lista_fora_memoria.append(memoria_virtual.get_pagina(id_pag_virtual))

        print(f"Lista de referências: {lista_ref}") # lista de 0 ou 1, indicando se a página naquela posição foi referenciada ou não
        print(f"Lista de páginas fora da memória: {[pag.id for pag in lista_fora_memoria]}")
        print()

        self.acessar_pagina(lista_ref)
        for pagina_virtual_fora in lista_fora_memoria:
            self.adiciona_falta_de_pagina(pagina_virtual_fora)

        print(f"Estado final da memória física: {[pag.id for pag in self.paginas]}")
        print()

        

    def acessar_pagina(self, pag_acessadas):
        for idx, pag in enumerate(self.paginas):
            if idx < len(pag_acessadas) and pag_acessadas[idx] == 1:
                pag.referencia()
            else:
                pag.nao_referencia()
        self.ordena_lru()
        print(f"Lista LRU ordenada (apos acessos): {[(pag.id, pag.peso) for pag in self.lru]}")

    def ordena_lru(self):
        print("Ordenando a lista LRU")
        # Reordenar a lista LRU baseado nos pesos das páginas
        self.lru.sort(key=lambda pag: pag.peso, reverse=True)

    def adiciona_falta_de_pagina(self, pagina_entra):
        # if len(self.paginas) == 0:
        #     # Se não há páginas na memória, adiciona a nova página
        #     self.paginas.append(pagina_entra)
        #     self.lru.append(pagina_entra)

        #     # PODERIA MUDAR ESSA LÓGICA PARA ADICIONAR CASO TENHA ESPAÇO NA MEMÓRIA FÍSICA

        if len(self.paginas) < self.tamanho:
            # Se ainda há espaço na memória física, adiciona a nova página
            self.paginas.append(pagina_entra)
            self.lru.append(pagina_entra)
            self.paginas[-1].referencia()
            self.ordena_lru()
        else:
            # Remove a última página da lista LRU (a menos utilizada)
            pagina_removida = self.lru.pop()
            self.paginas.remove(pagina_removida)

            # Adiciona a nova página
            self.paginas.append(pagina_entra)
            self.lru.append(pagina_entra)
            self.paginas[-1].referencia()
            self.ordena_lru()

        print(f"Lista LRU ordenada (apos falta de pagina): {[(pag.id, pag.peso) for pag in self.lru]}")