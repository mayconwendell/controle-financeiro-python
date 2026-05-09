def adicionar_movimentacao(tipo, movimentacoes):
    
    continuar = 's'
    while continuar == 's':

        try:
            nome = input('Digite o nome: ')
            print("\n========== Categorias ==========\n")
            print("1 - Alimentação" \
            "\n2 - Transporte" \
            "\n3 - Lazer" \
            "\n4 - Salário" \
            "\n5 - Estudos" \
            "\n6 - Outro")
            categoria = int(input('Qual categoria: '))

            if categoria == 1:
                categoria = 'alimentação'
            
            elif categoria == 2:
                categoria = 'transporte'
            
            elif categoria == 3:
                categoria = 'lazer'
            
            elif categoria == 4:
                categoria = 'salario'
            
            elif categoria == 5:
                categoria = 'estudos'
            
            elif categoria == 6:
                nova_categoria = input('Digite a categoria: ').lower()
                categoria = nova_categoria

            else:
                print("Categoria inválida!")
                
            valor = float(input('Digite o valor: '))

            nova_movimentacao = {
                'nome': nome,
                'valor': valor,
                'tipo': tipo,
                'categoria': categoria
            }

            movimentacoes.append(nova_movimentacao)
            print('Movimentação adicionada com sucesso!')

        except ValueError:
            print('Você digitou um valor inválido!')

        continuar = input('Deseja adicionar outra movimentação? (s / n) ').lower().strip()

def ver_movimentacoes(movimentacoes):

    if not movimentacoes:
        print('Não tem movimentações cadastradas!')

    else:
        try:
            continuar = 's'
        
            print('\n1 - Ver Tudo'
            '\n2 - Ver Receitas'
            '\n3 - Ver despesas'
            '\n4 - Voltar\n')
                
            while continuar == 's':

                pergunta = int(input('Qual opção deseja: '))

                if pergunta < 1 or pergunta > 4:
                        print('Opção inválida!')

                elif pergunta == 4:
                    return
                
                else:

                    for i, movimentacao in enumerate(movimentacoes):
        
                        if pergunta == 1:
                            print(f"{i + 1} - {movimentacao['nome']} - {movimentacao['valor']} - {movimentacao['tipo']}")
                        
                        elif pergunta == 2:
                            if movimentacao['tipo'] == 'receita':

                                print(f"{i + 1} - {movimentacao['nome']} - {movimentacao['valor']} - Receita")

                        elif pergunta == 3:
                            if movimentacao['tipo'] == 'despesa':
                                print(f"{i + 1} - {movimentacao['nome']} - {movimentacao['valor']} - Despesa")

        except ValueError:
            print('Você digitou um valor inválido!')

        continuar = input('Deseja escolher outra opção? (s / n) ').lower().strip()

def ver_saldo(movimentacoes):

    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
    
    else:
        somar = 0

        for movimentacao in movimentacoes:
            
            if movimentacao['tipo'] == 'receita':
                somar += movimentacao['valor']
            
            elif movimentacao['tipo'] == 'despesa':
                somar -= movimentacao['valor']
            
        print(f'Seu saldo final é R$: {somar}')