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

    categorias = {
        1: 'alimentação',
        2: 'transporte',
        3: 'lazer',
        4: 'salário',
        5: 'estudos'
    }

    for chave, valor in categorias.items():
        print(f'{chave} - {valor}')

    print('6 - Outro')

    try:

        categoria = int(input('Qual categoria: '))

        if categoria in categorias:
            return categorias[categoria]
        
        elif categoria == 6:
            categoria = input('Digite a categoria: ').lower()
            return categoria

        else:
            print('Categoria inválida!')
            return None

    except ValueError:
        print('Você digitou um valor inválido!')    

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

def remover_movimentacoes(movimentacoes):
    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
        return
    else:
        continuar = 's'
        
        while continuar == 's':
                
            listar_movimentacoes(movimentacoes)
            try:

                pergunta = int(input('Qual opção deseja remover: '))
                indice = pergunta - 1
                
                if pergunta >= 1 and pergunta <= len(movimentacoes):
                    confirmacao = input(f'Tem certeza de que deseja deletar a movimentação {pergunta}? (s / n) ').lower().strip()

                    if confirmacao == 's':
                        movimentacoes.pop(indice)
                    
                    else:
                        break

                else:
                    print('Movimentação não localizada!')

            except ValueError:
                print('Valor digitado inválido!')

            continuar = input('Quer remover outra movimentação (s / n) ').lower().strip()

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

def dashboard(movimentacoes):
    valor_receita = 0
    valor_despesa = 0
    valor_final = 0
    maior_valor = 0
    gastos_categoria = {}
    maior_categoria = None
    maior_gasto = None
    

    print('========== DASHBOARD ==========')

    for movimentacao in movimentacoes:
        
        if movimentacao['tipo'] == 'receita':
            valor_receita += movimentacao['valor']

        elif movimentacao['tipo'] == 'despesa':
            
            valor_despesa += movimentacao['valor']
            
            if maior_gasto is None:
                maior_gasto = movimentacao
            
            elif maior_gasto['valor'] < movimentacao['valor']:
                maior_gasto = movimentacao

            categoria = movimentacao['categoria']
            valor = movimentacao['valor']

            if categoria in gastos_categoria:
                gastos_categoria[categoria] += valor
            
            else:
                gastos_categoria[categoria] = valor

    for chave, valor in gastos_categoria.items():
        if maior_categoria is None:
            maior_categoria = chave
            maior_valor = valor
        
        elif maior_valor < valor:
            maior_categoria = chave
            maior_valor = valor

    valor_final = valor_receita - valor_despesa
    status = 'positivo' if valor_final > 0 else 'negativo'
    if valor_final == 0:
        status = 'nulo'

    print(f'\nSaldo atual: R$ {valor_final}')
    print(f'Total de receitas: R$ {valor_receita}')
    print(f'Total de despesas: R$ {valor_despesa}\n')
    
    if maior_gasto is not None:
        print(f"Maior gasto: {maior_gasto['nome']} - R$ {maior_gasto['valor']:.2f}")
    
    else:
        print("Maior gasto: Nenhuma despesa cadastrada")

    if maior_categoria is not None:
        print(f'Categoria com maior gasto: {maior_categoria} - R$ {maior_valor:.2f}')

    else:
        print("Categoria com maior gasto: Nenhuma despesa cadastrada")

    print(f'\nQuantidade de movimentações: {len(movimentacoes)}\n')

    print(f'Status financeiro: {status}\n')
    print('=' *31)

def menu_estatisticas(movimentacoes):

    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
    
    else:
        continuar = 's'
        while continuar == 's':
            try:
                print('1 - Maior despesa' \
                '\n2 - Média de gastos' \
                '\n3 - Categoria com mais despesas' \
                '\n4 - Quantidade de movimentações' \
                '\n5 - Total por categoria' \
                '\n6 - Sair')

                opcao = int(input('Qual opção deseja: '))

                if opcao == 1:
                    maior_despesa = None

                    for movimentacao in movimentacoes:

                        if movimentacao['tipo'] == 'despesa':
                            if maior_despesa is None:
                                maior_despesa = movimentacao
                            elif movimentacao['valor'] > maior_despesa['valor']:
                                maior_despesa = movimentacao
                    
                    if maior_despesa:
                        print(f"Maior despesa: {maior_despesa['nome']} - R$ {maior_despesa['valor']:.2f}")

                elif opcao == 2:
                    
                    total_gastos = 0
                    quantidade = 0
                    
                    for movimentacao in movimentacoes:

                        if movimentacao['tipo'] == 'despesa':
                            total_gastos += movimentacao['valor']
                            quantidade += 1

                    if quantidade > 0:

                        media = total_gastos / quantidade
                        print(f"A média de despesas é R$ {media:.2f}")
                    
                    else:
                        print('Não existem despesas.')

                elif opcao == 3:
                    gastos_categoria = {}
                    maior_categoria = None
                    maior_valor = 0

                    for movimentacao in movimentacoes:

                        if movimentacao['tipo'] == 'despesa':
                                            
                            categoria = movimentacao['categoria']
                            valor = movimentacao['valor']

                            if movimentacao['categoria'] in gastos_categoria:
                                gastos_categoria[categoria] += valor

                            else:
                                gastos_categoria[categoria] = valor

                    for chave, qtd in gastos_categoria.items():
                        
                        if maior_categoria is None:
                            maior_categoria = chave
                            maior_valor = qtd

                        elif qtd > maior_valor:
                            maior_valor = qtd
                            maior_categoria = chave

                    if maior_categoria:
                        print(f"Categoria com mais despesas: {maior_categoria} - R$ {maior_valor:.2f}")
                    else:
                        print("Não existem despesas cadastradas.")

                elif opcao == 4:
                    dashboard(movimentacoes)

                elif opcao == 5:
                    totais = {}

                    for movimentacao in movimentacoes:
                        categoria = movimentacao['categoria']
                        valor = movimentacao['valor']
                        
                        if categoria in totais:
                            totais[categoria] += valor
                        
                        else:
                            totais[categoria] = valor
                    
                    for chave, qtd in totais.items():
                        categorias = chave
                        valor_final = qtd

                        print(f'{categorias}: R$ {valor_final:.2f}')
                
                elif opcao == 6:
                    break
                
                else:
                    print('Opção digitada inválida!')

            except ValueError:
                print('Você digitou um valor inválido!')

            continuar = input('Deseja ver outra estatística? (s / n) ').lower().strip()

def filtro_categoria(movimentacoes):
    if not movimentacoes:
        print('Não tem movimentações cadastradas!')
    
    else:
        continuar = 's'
        
        while continuar == 's':
            categoria_escolhida = escolher_categoria()
            total_categoria = 0
            encontrou = False

            print(f'Categoria: {categoria_escolhida}\n')

            for i, movimentacao in enumerate(movimentacoes):
                
                if movimentacao['categoria'] == categoria_escolhida:
                    total_categoria += movimentacao['valor']
                    encontrou = True
                    print(f"{i + 1} - {movimentacao['nome']} | {movimentacao['tipo']} | {movimentacao['valor']:.2f}")

            if encontrou == False:
                print('Categoria não localizada!')
            
            continuar = input('Deseja filtrar outra categoria? (s / n): ').lower().strip()