from flask import Flask, request
import math

app = Flask(__name__)

def calcular_fatorial(n):
    return math.factorial(n)

def calcular_arranjo(n, r):
    return math.perm(n) // math.perm(n - r)

def calcular_combinacao(n, r):
    return math.perm(n) // (math.perm(r) * math.perm(n - r))

def calcular_permutacao(n):
    return math.perm(n)

@app.route('/')
def index():
    return 'Servidor de Cálculo'

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.get_json()
    if dados['operacao'] == 'fatorial':
        resultado = calcular_fatorial(dados['numero'])
    elif dados['operacao'] == 'arranjo':
        resultado = calcular_arranjo(dados['n'], dados['r'])
    elif dados['operacao'] == 'combinacao':
        resultado = calcular_combinacao(dados['n'], dados['r'])
    elif dados['operacao'] == 'permutacao':
        resultado = calcular_permutacao(dados['numero'])
    else:
        resultado = 'Operação inválida'
    return str(resultado)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
