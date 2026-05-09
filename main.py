from jso_utils import salvar, carregar
from financeiro import adicionar_movimentacao, ver_movimentacoes, ver_saldo

def menu(movimentacoes):

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
                adicionar_movimentacao('receita', movimentacoes)
            
            elif opcao == 2:
                adicionar_movimentacao('despesa', movimentacoes)

            elif opcao == 3:
                ver_movimentacoes(movimentacoes)

            elif opcao == 4:
                ver_saldo(movimentacoes)
            
            elif opcao == 5:
                print('Programa encerrado!')
                salvar(movimentacoes)
                break

            else:
                print('Opção inválida!')

        except ValueError:
            print('Você digitou um valor inválido!')

movimentacoes = carregar()
menu()
