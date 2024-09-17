from flask import Flask, render_template, request, jsonify
from lru import Lru
from mem_virtual import Mem_virtual
import random

app = Flask(__name__)

@app.route('/')
def index():
    """Página inicial com interface para simulação"""
    return render_template('index.html')


@app.route('/simular', methods=['POST'])
def simular_lru():
    """Realiza a simulação do LRU com base nas páginas acessadas e nos parâmetros informados"""
    tam_memoria_virtual = int(request.form.get('tam_memoria_virtual'))
    tam_memoria_fisica = int(request.form.get('tam_memoria_fisica'))
    num_clocks_simulados = int(request.form.get('num_clocks_simulados'))
    
    # Instâncias da memória virtual e física (LRU)
    tam_referencia = 8  # Pode ser fixo ou ajustável se necessário
    mem_virtual = Mem_virtual(tam_memoria_virtual, tam_referencia)
    mem_fisica = Lru(tam_memoria_fisica)
    
    resultado_simulacao = []

    # Simular acessos aleatórios para cada clock
    for clk in range(num_clocks_simulados):
        # Sorteia quais páginas da memória virtual serão acessadas neste clock
        pag_acessadas = [random.randint(0, 1) for _ in range(tam_memoria_virtual)]
        paginas_ref = mem_virtual.referencias_virtual_para_fisica(pag_acessadas)

        # Estado da memória física antes da operação
        memoria_inicial = [pag.id for pag in mem_fisica.paginas]
        
        # Referencia as páginas na memória física e coleta o resultado
        mem_fisica.referencia_paginas(paginas_ref, mem_virtual)
        
        # Estado da memória física depois da operação
        memoria_final = [pag.id for pag in mem_fisica.paginas]
        
        resultado_simulacao.append({
            'clk': clk,
            'memoria_inicial': memoria_inicial,
            'memoria_final': memoria_final,
            'paginas_acessadas': paginas_ref
        })

    # Retorna o resultado de toda a simulação
    return jsonify(resultado_simulacao)


if __name__ == '__main__':
    app.run(debug=True)
