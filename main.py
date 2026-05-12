from financeiro import (
    adicionar,
    ver_movimentacoes,
    editar_movimentacoes,
    remover_movimentacoes,
    dashboard,
    menu_estatisticas,
    ver_saldo,
    relatorio
)
from json_utils import salvar, carregar


def menu(movimentacoes):
    while True:
        print('\n========== MENU ==========\n')

        print(
            '1 - Adicionar receita'
            '\n2 - Adicionar despesa'
            '\n3 - Editar movimentações' \
            '\n4 - Remover movimentações' \
            '\n5 - Ver movimentações' \
            '\n6 - Menu estatísticas' \
            '\n7 - Dashboard'
            '\n8 - Ver saldo' \
            '\n9 - Relatório' \
            '\n10 - Sair\n'
        )

        try:
            opcao = int(input('Qual opção deseja: '))

            if opcao == 1:
                adicionar('receita', movimentacoes)
                salvar(movimentacoes)

            elif opcao == 2:
                adicionar('despesa', movimentacoes)
                salvar(movimentacoes)

            elif opcao == 3:
                editar_movimentacoes(movimentacoes)
                salvar(movimentacoes)

            elif opcao == 4:
                remover_movimentacoes(movimentacoes)
                salvar(movimentacoes)

            elif opcao == 5:
                ver_movimentacoes(movimentacoes)

            elif opcao == 6:
                menu_estatisticas(movimentacoes)

            elif opcao == 7:
                dashboard(movimentacoes)

            elif opcao == 8:
                ver_saldo(movimentacoes)

            elif opcao == 9:
                relatorio(movimentacoes)

            elif opcao == 10:
                print('Programa encerrado!')
                salvar(movimentacoes)
                break

            else:
                print('Opção inválida!')

        except ValueError:
            print('Você digitou um valor inválido!')


movimentacoes = carregar()
menu(movimentacoes)