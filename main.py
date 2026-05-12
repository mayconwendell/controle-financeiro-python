from financeiro import (
    adicionar,
    ver_movimentacoes,
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
            '\n3 - Ver Movimentações'
            '\n4 - Ver Saldo'
            '\n5 - Ver Relatório'
            '\n6 - Sair\n'
        )

        try:
            opcao = int(input('Qual opção deseja: '))

            if opcao == 1:
                adicionar('receita', movimentacoes)

            elif opcao == 2:
                adicionar('despesa', movimentacoes)

            elif opcao == 3:
                ver_movimentacoes(movimentacoes)

            elif opcao == 4:
                ver_saldo(movimentacoes)

            elif opcao == 5:
                relatorio(movimentacoes)

            elif opcao == 6:
                print('Programa encerrado!')
                salvar(movimentacoes)
                break

            else:
                print('Opção inválida!')

        except ValueError:
            print('Você digitou um valor inválido!')


movimentacoes = carregar()
menu(movimentacoes)