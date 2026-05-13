from financeiro import (
    adicionar,
    ver_movimentacoes,
    editar_movimentacoes,
    remover_movimentacoes,
    filtro_categoria,
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
            '\n3 - Editar movimentações' 
            '\n4 - Remover movimentações' \
            '\n5 - Filtrar por categoria' 
            '\n6 - Ver movimentações' 
            '\n7 - Menu estatísticas' 
            '\n8 - Dashboard'
            '\n9 - Ver saldo' 
            '\n10 - Relatório' \
            '\n11 - Sair' 
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
                filtro_categoria(movimentacoes)

            elif opcao == 6:
                ver_movimentacoes(movimentacoes)

            elif opcao == 7:
                menu_estatisticas(movimentacoes)

            elif opcao == 8:
                dashboard(movimentacoes)

            elif opcao == 9:
                ver_saldo(movimentacoes)

            elif opcao == 10:
                relatorio(movimentacoes)

            elif opcao == 11:
                print('Programa encerrado!')
                salvar(movimentacoes)
                break

            else:
                print('Opção inválida!')

        except ValueError:
            print('Você digitou um valor inválido!')


movimentacoes = carregar()
menu(movimentacoes)