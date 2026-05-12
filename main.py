from financeiro import (
    adicionar,
    ver_movimentacoes,
    editar_movimentacoes,
    estatisticas_gerais,
    menu_estatisticas,
    ver_saldo,
    relatorio
)

from json_utils import salvar, carregar


def menu(movimentacoes):
    while True:
        print('\n========== MENU ==========\n')

        print(
            '1 - Adicionar Receita'
            '\n2 - Adicionar Despesa'
            '\n3 - Editar movimentações' \
            '\n4 - Ver movimentações' \
            '\n5 - Menu Estatísticas' \
            '\n6 - Estatísticas gerais'
            '\n7 - Ver Saldo' \
            '\n8 - Relatório' \
            '\n9 - Sair\n'
        )

        try:
            opcao = int(input('Qual opção deseja: '))

            if opcao == 1:
                adicionar('receita', movimentacoes)

            elif opcao == 2:
                adicionar('despesa', movimentacoes)

            elif opcao == 3:
                editar_movimentacoes(movimentacoes)

            elif opcao == 4:
                ver_movimentacoes(movimentacoes)

            elif opcao == 5:
                menu_estatisticas(movimentacoes)

            elif opcao == 6:
                estatisticas_gerais(movimentacoes)

            elif opcao == 7:
                ver_saldo(movimentacoes)

            elif opcao == 8:
                relatorio(movimentacoes)

            elif opcao == 9:
                print('Programa encerrado!')
                salvar(movimentacoes)
                break

            else:
                print('Opção inválida!')

        except ValueError:
            print('Você digitou um valor inválido!')


movimentacoes = carregar()
menu(movimentacoes)