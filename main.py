from builtins import input

from utils.busca_cotacao import buscar_cotacao

while True:
    print('Bem vindo ao visualizador de ações.')
    print('Escolha uma opção:')
    print('1 - Buscar cotação.')
    print('2 - Sair.')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        acao = input('Informe a ação que deseja pesquisar: ')
        cotacao = buscar_cotacao(acao)

        if cotacao is not None:
            print(f"Informações da última semana para a ação {acao}:")
            print(cotacao)
        else:
            print(f"Não foi possível obter informações para a ação {acao}. Verifique se o símbolo está correto.")
    elif opcao == 2:
        print('Obrigada por usar o buscador de ações.')
        break
    else:
        print('Opção inválida. Digite novamente.')
