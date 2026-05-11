import json

def salvar(movimentacoes):
    with open("movimentacoes.json", "w") as arquivo:
        json.dump(movimentacoes, arquivo, indent=4, ensure_ascii=False)

def carregar():
    try:
        with open("movimentacoes.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados

    except FileNotFoundError:
        movimentacoes = []
        return movimentacoes