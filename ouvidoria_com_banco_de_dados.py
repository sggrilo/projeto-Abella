from operacoesbd import *

conexao = abrir_banco_de_dados('localhost', 'root', '', 'ouvidoria')


def testar_entrada_inteira(texto_de_entrada, maior_que=0, menor_que=0):
    """
    Testa se o que o usuário digitou é ou não um número inteiro, apenas aceitando valores numéricos.
    :param texto_de_entrada: O que será exibido no input que o usuário verá.
    :param maior_que: Só será aceito um número maior que esse.
    :param menor_que: Só será aceito um número menor que esse.
    :return um número inteiro no intervalo definido.
    """

    while True:
        num = input(texto_de_entrada)
        if not num.isnumeric():

            """
            Caso o usuário não digite um número inteiro,
            não acontecerá nada.
            """

            pass
        else:
            num = int(num)

            """
            O if só será executado se forem especificados
            os valores maior_que e menor_que.
            """

            if maior_que or menor_que:
                if maior_que < num < menor_que:
                    return num
            else:
                return num


def listar_manifestacoes(tipo=''):
    """
    Lista todas as manifestações de acordo com um determinado tipo.
    Se não houver um tipo especificado, todas as manifestações
    serão listadas.
    :param tipo: O tipo da manifestação, podendo ser Sugestão, Reclamação ou Elogio.
    """
    if tipo:
        sql = f"SELECT * FROM manifestacoes WHERE tipo = '{tipo}'"
    else:
        sql = f"SELECT * FROM manifestacoes"
    manifestacoes = listar_banco_de_dados(conexao, sql)
    for manifestacao in manifestacoes:

        """Serão imprimidas as manifestações de maneira formatada."""

        if tipo:
            print(f"{manifestacao[0]} — {manifestacao[1]} — {manifestacao[3]}")
        else:
            print(f"{manifestacao[0]} — {manifestacao[1]} — {manifestacao[2]} — {manifestacao[3]}")
    print('')


while True:
    """Abaixo, está o menu da ouvidoria."""

    print('Ouvidoria - Universidade ABC\n')
    print('1) Listar todas as manifestações')
    print('2) Listar todas as sugestões')
    print('3) Listar todas as reclamações')
    print('4) Listar todos os elogios')
    print('5) Criar uma nova manifestação')
    print('6) Procurar uma manifestação por protocolo (ID)')
    print('7) Sair\n')

    opcao = testar_entrada_inteira('Digite um número inteiro para selecionar uma opção: ', 0, 8)
    print()

    if opcao == 1:
        listar_manifestacoes()

    elif opcao == 2:
        listar_manifestacoes('Sugestão')

    elif opcao == 3:
        listar_manifestacoes('Reclamação')

    elif opcao == 4:
        listar_manifestacoes('Elogio')

    elif opcao == 5:
        nome = input('Digite o seu nome: ').strip().title()

        """A variável tipo só aceita 3 valores:
        Sugestão, Reclamação ou Elogio."""

        tipo = ''
        while tipo != 'Sugestão' and tipo != 'Reclamação' and tipo != 'Elogio':
            tipo = input('Digite o tipo da manifestação (Sugestão, Reclamação ou Elogio): ').strip().title()
        descricao = input('Digite a descrição da manifestação: ').strip().capitalize()

        sql = "INSERT INTO manifestacoes(nome, tipo, descricao) VALUES (%s, %s, %s)"
        dados = (nome, tipo, descricao)
        inserir_no_banco_de_dados(conexao, sql, dados)

    elif opcao == 6:
        protocolo = testar_entrada_inteira('Digite um número para selecionar o protocolo (ID) da manifestação: ')
        sql = f"SELECT * FROM manifestacoes WHERE id = {str(protocolo)}"
        manifestacoes = listar_banco_de_dados(conexao, sql)
        for manifestacao in manifestacoes:
            print(f"\n{manifestacao[0]} - {manifestacao[1]} - {manifestacao[2]} - {manifestacao[3]}")
        print('')

    elif opcao == 7:
        break
