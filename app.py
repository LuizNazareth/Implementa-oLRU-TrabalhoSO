from flask import Flask, render_template, request, jsonify
from lru import Lru
from mem_virtual import Mem_virtual

app = Flask(__name__)

# Configurações iniciais
tam_memoria_virtual = 10
tam_memoria_fisica = 5
tam_referencia = 8

# Instâncias da memória virtual e física (LRU)
mem_virtual = Mem_virtual(tam_memoria_virtual, tam_referencia)
mem_fisica = Lru(tam_memoria_fisica)

# Simulação de acessos
pag_acessadas = [[0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                 [1, 0, 1, 1, 1, 1, 1, 0, 1, 0]]


@app.route('/')
def index():
    """Página inicial com interface para simulação"""
    return render_template('index.html')


@app.route('/simular', methods=['POST'])
def simular_lru():
    """Realiza a simulação do LRU com base nas páginas acessadas"""
    clk = int(request.form.get('clk'))  # Recebe o clock atual da interface
    paginas_ref = mem_virtual.referencias_virtual_para_fisica(pag_acessadas[clk])
    
    # Referencia as páginas na memória física e coleta o resultado
    memoria_inicial = [pag.id for pag in mem_fisica.paginas]
    mem_fisica.referencia_paginas(paginas_ref, mem_virtual)
    memoria_final = [pag.id for pag in mem_fisica.paginas]
    
    # Retorna o estado antes e depois da operação para exibir na interface
    return jsonify({
        'memoria_inicial': memoria_inicial,
        'memoria_final': memoria_final,
        'paginas_acessadas': paginas_ref
    })


if __name__ == '__main__':
    app.run(debug=True)
