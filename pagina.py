import numpy as np

class Pagina:
    def __init__(self, indice: int, tamanho_referencia: int):
        self.indice = indice
        self.lista_referencia = np.zeros(tamanho_referencia)
        self.prox = None
        self.ant = None
        self.tamanho_referencia = tamanho_referencia
        
    def referencia(self):
        np.roll(self.lista_referencia, 1)
        self.lista_referencia[0] = 1
        
    def nao_referencia(self):
        np.roll(self.lista_referencia, 1)
        self.lista_referencia[0] = 0
        