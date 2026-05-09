def menu():

    while True:
        print('\n========== MENU ==========\n')
        print('1 - Adicionar Receita' \
        '\n2 - Adicionar despesa' \
        '\n3 - Ver movimentações' \
        '\n4 - Ver saldo' \
        '\n5 - Sair\n')
        try:

            opcao = int(input('Qual opção deseja: '))

            if opcao == 1:
                adicionar_movimentacao('receita')
            
            elif opcao == 2:
                adicionar_movimentacao('despesa')

            elif opcao == 3:
                pass

            elif opcao == 4:
                pass
            
            elif opcao == 5:
                print('Programa encerrado!')
                break

            else:
                print('Opção inválida!')

        except ValueError:
            print('Você digitou um valor inválido!')