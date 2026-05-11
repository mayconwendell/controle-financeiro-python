<<<<<<< HEAD
from jso_utils import salvar, carregar
from financeiro import adicionar_movimentacao, ver_movimentacoes, ver_saldo

def menu(movimentacoes):
=======
from financeiro import (
    adicionar_movimentacao,
    ver_movimentacoes,
    ver_saldo,
    relatorio
)

from json_utils import salvar, carregar


def menu():
>>>>>>> 91677ab (feat: adiciona relatório financeiro)

    while True:

        print('\n========== MENU ==========\n')

        print(
            '1 - Adicionar Receita'
            '\n2 - Adicionar Despesa'
            '\n3 - Ver Movimentações'
            '\n4 - Ver Saldo' 
            '\n5 - Ver Relatório'
            '\n5 - Sair\n'
        )

        try:

            opcao = int(input('Qual opção deseja: '))

            if opcao == 1:
                adicionar_movimentacao('receita', movimentacoes)
<<<<<<< HEAD
            
=======

>>>>>>> 91677ab (feat: adiciona relatório financeiro)
            elif opcao == 2:
                adicionar_movimentacao('despesa', movimentacoes)

            elif opcao == 3:
                ver_movimentacoes(movimentacoes)

            elif opcao == 4:
                ver_saldo(movimentacoes)
<<<<<<< HEAD
            
=======

>>>>>>> 91677ab (feat: adiciona relatório financeiro)
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

<<<<<<< HEAD
movimentacoes = carregar()
menu()
=======

movimentacoes = carregar()

menu()
>>>>>>> 91677ab (feat: adiciona relatório financeiro)
