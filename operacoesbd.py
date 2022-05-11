import mysql.connector


def abrir_banco_de_dados(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)


def encerrar_banco_de_dados(connection):
    connection.close()


def inserir_no_banco_de_dados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    return id


def listar_banco_de_dados(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results


def atualizar_banco_de_dados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    return linhas_afetadas


def excluir_banco_de_dados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    return linhas_afetadas
