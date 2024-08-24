import numpy as np

class Pagina:
    def __init__(self, indice: int, tamanho_referencia: int, peso):
        self.indice = indice
        self.lista_referencia = np.zeros(tamanho_referencia)
        self.prox = None
        self.ant = None
        self.tamanho_referencia = tamanho_referencia
        self.peso = 0
        
    def referencia(self):
        np.roll(self.lista_referencia, 1)
        self.lista_referencia[0] = 1
        self.peso = self.binario_para_decimal()
        
    def nao_referencia(self):
        np.roll(self.lista_referencia, 1)
        self.lista_referencia[0] = 0
        self.peso = self.binario_para_decimal()
        
    def binario_para_decimal(self):
    # Converte o vetor de inteiros para uma string concatenada
        binario = ''.join(map(str, self.lista_referencia))
        
        # Converte a string binária para um número decimal
        self.peso = int(binario, 2)
        
        return self.peso