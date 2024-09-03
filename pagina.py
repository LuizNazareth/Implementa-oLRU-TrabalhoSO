import numpy as np

class Pagina:
    def _init_(self, id: int, tamanho_referencias: int):
        self.id = id 
        self.lista_referencias = np.zeros(tamanho_referencias) # é o quadro de bits que guarda as referências à página
        self.prox = None
        self.ant = None
        self.tamanho_referencia = tamanho_referencias
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