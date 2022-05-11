lista_de_manifestacoes = []


class Manifestacao:
    """A classe Manifestacao representa uma manifestação de uma ovidoria."""

    def __init__(self, protocolo, nome, tipo, descricao):
        self.protocolo = protocolo
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao

    def adicionar_a_lista(self):
        lista_de_manifestacoes.append([self.protocolo, self.nome, self.tipo, self.descricao])


def procurar_manifestacao(tipo_a_ser_procurado=''):
    for indice, manifestacao in enumerate(lista_de_manifestacoes):
        if tipo_a_ser_procurado != '':
            if lista_de_manifestacoes[indice][2] == tipo_a_ser_procurado:
                print(manifestacao)
        else:
            print(manifestacao)


# A estrutura de repetição abaixo apresenta repetidamente a lista de opções,
# até que seja selecionada a sétima opção, que encerra o programa.

protocolo = 0
tipo = 'AAAAA'
while True:
    print('\n\tOuvidoria - Universidade ABC'
          '\n'
          '\n1) Listar todas as manifestações'
          '\n2) Listar todas as sugestões'
          '\n3) Listar todas as reclamações'
          '\n4) Listar todos os elogios'
          '\n5) Enviar uma nova manifestação'
          '\n6) Pesquisar uma manifestação por protocolo (ID)'
          '\n7) Sair')

    # A estrutura de repetição abaixo será repetida até que o usuário digite
    # um número no intervalo definido.

    while True:
        opcao = input('\nPor favor, digite um número entre 1 e 7 para selecionar uma das opções acima: ').strip()
        if not opcao.isnumeric():

            # Caso o usuário digite qualquer entrada que não seja um
            # número, será impressa uma mensagem de erro.

            print('\nEntrada inválida! Por favor, digite apenas um número inteiro entre 1 e 7!')
        else:

            # Quando o usuário finalmente digitar um número, a
            # variável opcao terá seu tipo alterado para inteiro,
            # quebrando finalmente o while.

            opcao = int(opcao)
            if opcao < 1 or opcao > 7:
                print('\nEntrada inválida! Por favor, digite apenas um número inteiro entre 1 e 7!')
                continue
            break

    if opcao == 1:
        print('\nLista de manifestações:\n')
        procurar_manifestacao()

    elif opcao == 2:
        print('\nLista de sugestões:\n')
        procurar_manifestacao('Sugestão')

    elif opcao == 3:
        print('\nLista de reclamações:\n')
        procurar_manifestacao('Reclamação')

    elif opcao == 4:
        print('\nLista de elogios:\n')
        procurar_manifestacao('Elogio')

    # A quinta opção permite que o usuário crie uma manifestação,
    # que será adicionada à lista manifestacoes.

    elif opcao == 5:
        protocolo = protocolo + 1
        nome = input('\nPor favor, digite o seu nome: ').strip().title()
        while tipo != 'Sugestão' != 'Reclamação' != 'Elogio':
            tipo = input('Por favor, digite o tipo da manifestação (Sugestão, Reclamação ou Elogio): ').strip().title()
            if tipo != 'Sugestão' and tipo != 'Reclamação' and tipo != 'Elogio':
                print('\nEntrada inválida! Digite apenas "Sugestão", "Reclamação" ou "Elogio"!\n')
        descricao = input('Por favor, descreva a sua manifestação: ').strip().capitalize()

        manif = Manifestacao(protocolo, nome, tipo, descricao)
        manif.adicionar_a_lista()

    elif opcao == 6:
        while True:
            procurar_protocolo = input('\nDigite o protocolo da manifestação a ser procurada: ').strip()
            if not procurar_protocolo.isnumeric():
                print('\nEntrada inválida! Por favor, digite apenas um número inteiro!')
            else:
                procurar_protocolo = int(procurar_protocolo)
                if procurar_protocolo < 1 or procurar_protocolo > len(lista_de_manifestacoes):
                    print('\nEntrada inválida! Por favor, digite apenas um número inteiro!')
                    continue
            break

        for indice, manifestacao in enumerate(lista_de_manifestacoes):
            if procurar_protocolo == (indice + 1):
                print(manifestacao)

    elif opcao == 7:
        print('\nSaindo do programa...')
        break
