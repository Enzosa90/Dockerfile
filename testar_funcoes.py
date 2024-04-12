import requests

def testar_funcoes():
    payloads = [
        {"operacao": "fatorial", "numero": 6},
        {"operacao": "arranjo", "n": 8, "r": 2},
        {"operacao": "combinacao", "n": 10, "r": 2},
        {"operacao": "permutacao", "numero": 6}
    ]

    for payload in payloads:
        response = requests.post('https://calcservidor1-b6ivxkcr.b4a.run/calcular', json=payload)
        resultado = response.text
        
        if payload['operacao'] == 'fatorial':
            print(f'A fatorial de {payload["numero"]} eh {resultado}')
        elif payload['operacao'] == 'arranjo':
            print(f'O arranjo de {payload["n"]} elementos tomados {payload["r"]} eh {resultado}')
        elif payload['operacao'] == 'combinacao':
            print(f'A combinacao de {payload["n"]} elementos tomados {payload["r"]} eh {resultado}')
        elif payload['operacao'] == 'permutacao':
            print(f'A permutacao de {payload["numero"]} elementos eh {resultado}')

if __name__ == "__main__":
    testar_funcoes()
