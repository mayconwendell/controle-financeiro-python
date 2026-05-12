def adicionar(tipo, movimentacoes):

    continuar = 's'

    while continuar == 's':

        try:
            nome = input('Digite o nome: ')

            categoria = escolher_categoria()

            if categoria:

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

def escolher_categoria():
    print("\n========== Categorias ==========\n")

    print("1 - Alimentação"
        "\n2 - Transporte"
        "\n3 - Lazer"
        "\n4 - Salário"
        "\n5 - Estudos"
        "\n6 - Outro")

    categoria = int(input('Qual categoria: '))

    if categoria == 1:
        categoria = 'alimentação'

    elif categoria == 2:
        categoria = 'transporte'

    elif categoria == 3:
        categoria = 'lazer'

    elif categoria == 4:
        categoria = 'salário'

    elif categoria == 5:
        categoria = 'estudos'

    elif categoria == 6:
        categoria = input('Digite a categoria: ').lower()

    else:
        print('Categoria inválida!')
        return None
    
    return categoria

def ver_movimentacoes(movimentacoes):

    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
        return

    try:

        continuar = 's'

        while continuar == 's':

            print('\n1 - Ver Tudo'
                  '\n2 - Filtrar por categoria' \
                  '\n3 - Ver Receitas'
                  '\n4 - Ver Despesas'
                  '\n5 - Voltar\n')

            pergunta = int(input('Qual opção deseja: '))

            if pergunta < 1 or pergunta > 5:
                print('Opção inválida!')

            elif pergunta == 5:
                return

            else:

                if pergunta == 2:
                    encontrou = False
                    categoria = input('Digite a categoria: ').lower()

                for i, movimentacao in enumerate(movimentacoes):
                    if pergunta == 1:

                        print(f"{i + 1} - {movimentacao['nome']} - R$ {movimentacao['valor']:.2f} - {movimentacao['tipo']} - {movimentacao['categoria']}")

                    elif pergunta == 2:
                        
                        if categoria == movimentacao['categoria']:
                            encontrou = True
                            print(f"{i + 1} - {movimentacao['nome']} - {movimentacao['valor']} - {movimentacao['categoria']}")

                    elif pergunta == 3:

                        if movimentacao['tipo'] == 'receita':

                            print(f"{i + 1} - {movimentacao['nome']} - R$ {movimentacao['valor']:.2f} - Receita - {movimentacao['categoria']}")
                    elif pergunta == 4:

                        if movimentacao['tipo'] == 'despesa':

                            print(f"{i + 1} - {movimentacao['nome']} - R$ {movimentacao['valor']:.2f} - Despesa - {movimentacao['categoria']}")
                            
                if pergunta == 2 and not encontrou:
                    print('Categoria não localizada!')

            continuar = input('\nDeseja escolher outra opção? (s / n) ').lower().strip()

    except ValueError:
        print('Você digitou um valor inválido!')

def listar_movimentacoes(movimentacoes):
    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
    
    else:
        print("========== LISTA DE MOVIMENTAÇÕES ==========")
        for i, movimentacao in enumerate(movimentacoes):
            print(f"{i + 1} - {movimentacao['nome']} - R$ {movimentacao['valor']:.2f} - {movimentacao['tipo']} - {movimentacao['categoria']}")

def editar_movimentacoes(movimentacoes):
    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
    
    else:
        continuar = 's'
        while continuar == 's':
                
            try:
                listar_movimentacoes(movimentacoes)
                pergunta = int(input('Qual movimentação deseja editar: '))

                if pergunta > 0 and pergunta <= len(movimentacoes):
                    print('1 - Nome' \
                    '\n2 - Valor' \
                    '\n3 - Tipo' \
                    '\n4 - Categoria\n')

                    opcao = int(input('Qual opção deseja: '))
                    indice = pergunta - 1

                    if opcao <1 or opcao > 4:
                        print('Opção inválida!')

                    else:
                        if opcao == 1:
                            novo_nome = input('Digite o novo nome: ').lower()
                            movimentacoes[indice]['nome'] = novo_nome
                        
                        elif opcao == 2:
                            novo_valor = float(input('Digite o novo valor: '))
                            movimentacoes[indice]['valor'] = novo_valor
                        
                        elif opcao == 3:
                            print('1 - Receita' \
                            '\n2 - Despesa\n')
                            novo_tipo = int(input('Qual o novo tipo: '))
                            
                            if novo_tipo == 1:
                                novo_tipo = 'receita'
                                movimentacoes[indice]['tipo'] = novo_tipo
                            elif novo_tipo == 2:
                                novo_tipo = 'despesa'
                                movimentacoes[indice]['tipo'] = novo_tipo
                            else:
                                print('tipo inválido!')
                            
                        
                        elif opcao == 4:
                            nova_categoria = escolher_categoria()
                            if nova_categoria:
                                movimentacoes[indice]['categoria'] = nova_categoria                          
                else:
                    print('Movimentação não encontrada!')
            except ValueError:
                print('Valor digitado inválido!')
            
            continuar = input('Deseja editar outra movimentação? (s / n) ').lower()

def ver_saldo(movimentacoes):

    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
        return

    saldo = 0

    for movimentacao in movimentacoes:

        if movimentacao['tipo'] == 'receita':
            saldo += movimentacao['valor']

        elif movimentacao['tipo'] == 'despesa':
            saldo -= movimentacao['valor']

    print(f'Seu saldo final é R$: {saldo:.2f}')


def relatorio(movimentacoes):

    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
        return

    total_rec = 0
    total_des = 0

    print('\n========== RELATÓRIO ==========\n')

    for movimentacao in movimentacoes:

        if movimentacao['tipo'] == 'receita':
            total_rec += movimentacao['valor']

        elif movimentacao['tipo'] == 'despesa':
            total_des += movimentacao['valor']

    saldo = total_rec - total_des

    print(f'Total de receitas: R$ {total_rec:.2f}')
    print(f'Total de despesas: R$ {total_des:.2f}')
    print(f'Saldo final: R$ {saldo:.2f}')
