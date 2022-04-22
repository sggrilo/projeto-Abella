sugestoes = [['1', 'Luigi', 'Sugestão', 'A quadra de tênis precisa de uma capa protetora, todos ficam queimados '
                                        'quando vão lá, iria ajudar bastante.'],
             ['2', 'Pedro', 'Sugestão', 'Cuidem das lâmpadas do quinto andar, todas já estão prestes a queimar, '
                                        'então por favor cuidem disso.']]

reclamacoes = [['3', 'José', 'Reclamação', 'Alguém jogou todo o papel higiênico no vaso sanitário.'],
               ['4', 'Roger', 'Reclamação', 'A comida daqui não tem gosto nenhum.']]

elogios = [['5', 'Juliana', 'Elogio', 'Os métodos de ensino prático usados pelos professores de Física e Química é '
                                      'incrível!'],
           ['6', 'Paulo', 'Elogio', 'Gosto muito da atribuição de papel duplo para os papeis higiênicos do banheiro '
                                    'do segundo andar!']]

# A lista 'manifestacoes' é uma combinação de todas as outras listas acima.
# Portanto, os elementos das listas 'sugestoes', 'reclamacoes' e 'elogios'
# serão adicionados a ela.

manifestacoes = []
manifestacoes.extend(sugestoes)
manifestacoes.extend(reclamacoes)
manifestacoes.extend(elogios)

# A estrutura de repetição abaixo apresenta repetidamente a lista de opções,
# até que seja selecionada a sétima opção, que quebra a repetição e encerra
# o programa.

while True:
    print('Ouvidoria — Universidade ABC')
    print('')
    print('1) Listar todas as manifestações')
    print('2) Listar todas as sugestões')
    print('3) Listar todas as reclamações')
    print('4) Listar todos os elogios')
    print('5) Enviar uma manifestação (criar uma nova)')
    print('6) Pesquisar protocolo por número (ID)')
    print('7) Sair')
    print('')

    # A estrutura de repetição abaixo será repetida até que o usuário digite
    # um número no intervalo definido.

    while True:
        opcao = int(input('Por favor, digite um número entre 1 e 7 para selecionar uma das opções acima: '))
        if opcao < 1 or opcao > 7:
            print('Entrada inválida! Por favor, digite apenas um número entre 1 e 7!')
            print('')
        else:
            print('')
            break

    # As quatro primeiras opções abaixo mostram cada elemento das listas
    # 'manifestacoes', 'sugestoes', 'reclamacoes' e 'elogios', respectivamente.

    # Foram utilizados dois for para listar cada elemento da manifestação
    # separado por um travessão.

    if opcao == 1:
        print('Lista de manifestações:')
        print('')
        for manif in manifestacoes:
            for indice, item in enumerate(manif):
                if indice != len(manif) - 1:
                    print(f'{item} ', end='— ')
                else:
                    print(item)
        print('')

    elif opcao == 2:
        print('Lista de sugestões:')
        print('')
        for sugestao in sugestoes:
            for indice, item in enumerate(sugestao):
                if indice != len(sugestao) - 1:
                    print(f'{item} ', end='— ')
                else:
                    print(item)
        print('')

    elif opcao == 3:
        print('Lista de reclamações:')
        print('')
        for reclamacao in reclamacoes:
            for indice, item in enumerate(reclamacao):
                if indice != len(reclamacao) - 1:
                    print(f'{item} ', end='— ')
                else:
                    print(item)
        print('')

    elif opcao == 4:
        print('lista de elogios:')
        print('')
        for elogio in elogios:
            for indice, item in enumerate(elogio):
                if indice != len(elogio) - 1:
                    print(f'{item} ', end='— ')
                else:
                    print(item)
        print('')

    # A quinta opção permite que o usuário crie uma nova manifestação,
    # que será adicionada à lista manifestacoes e à lista do seu
    # respectivo tipo.

    elif opcao == 5:

        # O comprimento de 'manifestacoes' é adicionado a 1 para que o ID da
        # manifestação seja de 1 a mais que o total de manifestações.

        protocolo = len(manifestacoes) + 1

        nome = input('Digite o nome do requisitante: ').strip()

        while True:

            # A variável 'numeroTipo' será utilizada para determinar o
            # tipo da manifestação (reclamação, sugestão ou elogio).

            numeroTipo = int(input('Digite o tipo da manifestação, sendo 1 = Sugestão, 2 = Reclamação e 3 = Elogio: '))

            if numeroTipo < 1 or numeroTipo > 3:
                print('Entrada inválida! Por favor, digite apenas um número entre 1 e 3!')
                print('')
            else:
                if numeroTipo == 1:
                    tipo = 'Sugestão'
                elif numeroTipo == 2:
                    tipo = 'Reclamação'
                else:
                    tipo = 'Elogio'
                break

        descricao = input('Descreva sua manifestação: ').strip()
        print('')

        # Cada um dos elementos da manifestação serão adicionados a uma
        # variável, chamada 'manifestacao'.

        manifestacao = str(protocolo) + '#' + nome + '#' + tipo + '#' + descricao

        # Em seguida, é gerada uma lista com cada um dos elementos,
        # denominada manifestacaoSeparada, que é adicionada à lista
        # 'manifestacoes' e à lista correspondente ao seu tipo.

        manifestacaoSeparada = manifestacao.split('#')

        if tipo == 'Sugestão':
            sugestoes.append(manifestacaoSeparada)
        elif tipo == 'Reclamação':
            reclamacoes.append(manifestacaoSeparada)
        else:
            elogios.append(manifestacaoSeparada)
        manifestacoes.append(manifestacaoSeparada)

        # Depois, é mostrada ao usuário a manifestação que ele criou.

        print('Protocolo: ' + manifestacaoSeparada[0])
        print('Nome: ' + manifestacaoSeparada[1])
        print('Tipo: ' + manifestacaoSeparada[2])
        print('Problema: ' + manifestacaoSeparada[3])
        print('')

    elif opcao == 6:
        print('Pesquisa de protocolo (ID):')
        print('')

        while True:

            # Enquanto não for digitado um ID correspondente a uma
            # manifestação existente, essa estrutura de repetição
            # é executada.

            procura = int(input('Por favor, digite o ID da manifestação para procurá-la: '))
            procura = procura - 1
            if procura < 0 or procura > len(manifestacoes) - 1:
                print('Entrada inválida! Por favor, digite apenas um ID existente.')
                print('')
            else:
                print('')
                break

        # Após ser digitado um ID válido, é procurada na lista
        # 'manifestacoes' a manifestação correspondente ao ID
        # lido pelo programa e ela é impressa, mostrando cada
        # elemento separadamente, assim como na tela de criação
        # da manifestação.

        print('Protocolo: ' + manifestacoes[procura][0])
        print('Nome: ' + manifestacoes[procura][1])
        print('Tipo: ' + manifestacoes[procura][2])
        print('Problema: ' + manifestacoes[procura][3])
        print('')

    elif opcao == 7:

        # Caso o usuário digite esse número, a estrutura de repetição
        # é quebrada, encerrando o programa.

        print('Saindo do programa...')
        break
