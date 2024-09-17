import numpy as np

class Pagina:
    def __init__(self, id: int, tamanho_referencias: int):
        self.id = id 
        self.lista_referencias = np.zeros(tamanho_referencias, dtype=int) # lista que representa o numero binário e permite usar o algoritmo de aging
        self.tamanho_referencia = tamanho_referencias 
        self.peso = 0
        self.estado = 0
        
    def referencia(self):
        self.lista_referencias = np.roll(self.lista_referencias, 1)
        self.lista_referencias[0] = 1
        self.binario_para_decimal()
        # print(f"Página {self.id} referenciada. Peso atualizado para {self.peso}.")
        # print()
        
    def nao_referencia(self):
        self.lista_referencias = np.roll(self.lista_referencias, 1)
        self.lista_referencias[0] = 0
        self.binario_para_decimal()
        # print(f"Página {self.id} não referenciada. Peso atualizado para {self.peso}.")
        # print()
        
    def binario_para_decimal(self):
        # Converte o vetor de inteiros para uma string concatenada
        binario = ''.join(map(str, self.lista_referencias.astype(int)))  # Assegura que a lista contém apenas inteiros
        
        # Converte a string binária para um número decimal
        self.peso = int(binario, 2)

    def __str__(self):
        referencias_str = ' '.join(map(str, self.lista_referencias.astype(int)))
        return f"Página ID: {self.id}, Referências: [{referencias_str}], Peso: {self.peso}, Estado: {self.estado}\n"
