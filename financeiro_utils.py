import csv

def relatorio(movimentacoes):

    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
        return

    total_rec = 0
    total_des = 0
    texto = ''

    texto += '========== RELATÓRIO ==========\n\n'

    for i, movimentacao in enumerate(movimentacoes):

        if movimentacao['tipo'] == 'receita':
            total_rec += movimentacao['valor']

        elif movimentacao['tipo'] == 'despesa':
            total_des += movimentacao['valor']

        texto+= f"\n{i + 1} - {movimentacao['nome']}\n"
        texto+= f"tipo: {movimentacao['tipo']}\n"
        texto+= f"Categoria: {movimentacao['categoria']}\n"
        texto+= f"Valor: R$ {movimentacao['valor']:.2f}\n"

        texto +="-" *31 + '\n'
    
    saldo = total_rec - total_des

    texto+= f'Total de receitas: R$ {total_rec:.2f}\n'
    texto+= f'Total de despesas: R$ {total_des:.2f}\n'
    texto+= f'Saldo final: R$ {saldo:.2f}'

    return texto

def salvar_relatorio(texto):

    
    with open('relatorio.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)

    print('Relatório salvou com sucesso!')

def exportar_csv(movimentacoes):
    with open('relatorio.csv', 'w', encoding='utf-8', newline='') as arquivo:
        campos = ['nome', 'valor', 'tipo', 'categoria']
        escritor = csv.DictWriter(arquivo, campos)
        escritor.writeheader()
        escritor.writerows(movimentacoes)