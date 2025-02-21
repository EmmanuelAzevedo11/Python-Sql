import mysql.connector

# conectado ao banco de dados
try:
    cn = mysql.connector.connect(
        host='localhost', database='novo_projeto', user='root', password='11042006')

    if cn.is_connected():
        print("conectado")
        db_info = cn.get_server_info()

        cursor = cn.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()

except mysql.connector.Error as erro:
    print("Erro: {}", erro)

# criando a tabela do Bc
try:
    new_table = """CREATE TABLE IF NOT EXISTS register_user
    (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        primeiro_nome VARCHAR(50) NOT NULL,
        sobrenome VARCHAR(50) NOT NULL,
        renda_mensal DECIMAL(10,2)
    );"""

    cursor.execute(new_table)
    cn.commit()
    print("Tabela criada")
except mysql.connector.Error as erro:
    print("Erro: {}", erro)

# inserindo dados no banco de dados
try:
    i = 0
    while (i < 1):
        primeiro_nome = input("Primeiro nome: ")
        if primeiro_nome == " ":
            str(input("Coloque o primeiro seu primeiro nome Ex: Gustavo"))
            break
        sobrenome = input("sobrenome: ")
        if sobrenome == " ":
            str(input("Coloque apenas seu sobrenome nome Ex: Silva"))
            break
        renda_mensal = float(input(
            "Sua renda mensal: (sem contar familiares ou moradores da casa)"))
        i += 1

        primeiro_nome = primeiro_nome.lower().strip()
        sobrenome = sobrenome.lower().strip()

        print("primeiros dados inseridos")

        sql = """INSERT INTO register_user (primeiro_nome, sobrenome, renda_mensal) 
            VALUES (%s, %s, %s)"""

        values = (primeiro_nome,
                  sobrenome, renda_mensal)

        cursor.execute(sql, values)
        print("Dados inseridos!")

        usuarios = [
            {"primeiro_nome": "Jõao",
                "sobrenome": "Oliveira", "renda_mensal": 2500},
            {"primeiro_nome": "Pedro",
                "sobrenome": "Cardoso", "renda_mensal": 7500},
            {"primeiro_nome": "Maria",
                "sobrenome": "Arruda", "renda_mensal": 4200},
            {"primeiro_nome": "Rafael",
                "sobrenome": "Santos", "renda_mensal": 5320},
        ]
        for i in usuarios:

            new_values = (
                i["primeiro_nome"].strip().lower(),
                i["sobrenome"].strip().lower(),
                i["renda_mensal"]
            )

            sql = """INSERT INTO register_user (primeiro_nome, sobrenome, renda_mensal) 
            VALUES (%s, %s, %s)"""

            cursor.execute(sql, new_values)

        cn.commit()
        print("Segundos dados adcionados")

except mysql.connector.Error as erro:
    print("Erro: {}", erro)


# encerrando a conexão do banco de dados
    if cn.is_connected():
        cursor.close()
        cn.close()
        print("Conexão com banco de dados encerrada.")
    else:
        print("erro não esperado.")
