import sqlite3 as sqlite

class DAOAluno:
    def criarConexao(self):
        try:
        #abre a conexao
            conexao = sqlite.connect("C:\Faculdade\Python\AtividadeNotas\DADOS\DBALUNOS.db")
            #aquisição do cusror
            cursor = conexao.cursor()
            #execucao do comando
            cursor.execute("SELECT * FROM ALUNO")
            cursor.fetchall()
            #efetiva o comand
            conexao.commit()
            print("#Conectado ao banco de dados... ")
        except sqlite.DatabaseError as e:
            print("erro ao conectar ao banco de dados -> ",e)
            conexao.close()
        finally:
            conexao.close()
            print("#Conexao Fechada...")

    def insertAluno(self, nome, turma):
        try:
            con = sqlite.connect("C:\Faculdade\Python\AtividadeNotas\DADOS\DBALUNOS.db")
            cursor = con.cursor()
            comando = '''INSERT INTO ALUNO(NOME, TURMA)VALUES(:NOME,:TURMA);'''
            cursor.execute(comando, {"NOME": nome, "TURMA": turma})
            con.commit()
            con.close()
            print("Aluno salvo com sucesso!")

        except sqlite.DatabaseError as e:
            print('Erro ao adicionar aluno ->', e)
            con.close()
        finally:
            con.close()

    def updateAluno(self, nome, turma, id):
        try:
            con = sqlite.connect("C:\Faculdade\Python\AtividadeNotas\DADOS\DBALUNOS.db")
            cursor = con.cursor()
            comando = '''UPDATE ALUNO SET NOME = :NOME, TURMA = :TURMA  WHERE ID = :ID;'''
            cursor.execute(comando, {"NOME": nome, "TURMA": turma, "ID": id})
            con.commit()
            con.close()
            print("Aluno alterado com sucesso!")

        except sqlite.DatabaseError as e:
            print('Erro ao Alterar aluno ->', e)
            con.close()
        finally:
            con.close()

    def deleteAluno(self, id):
        try:
            con = sqlite.connect("C:\Faculdade\Python\AtividadeNotas\DADOS\DBALUNOS.db")
            cursor = con.cursor()
            comando = '''DELETE FROM ALUNO WHERE ID=:ID;'''
            cursor.execute(comando, {"ID": id})
            con.commit()
            con.close()
            print("Aluno deletado com sucesso!")

        except sqlite.DatabaseError as e:
            print('Erro ao deletar aluno ->', e)
            con.close()
        finally:
            con.close()

    def selectAluno(self, nome):
        try:
            conexao = sqlite.connect("C:\Faculdade\Python\AtividadeNotas\DADOS\DBALUNOS.db")
            cursor = conexao.cursor()
            cursor.execute('''SELECT * FROM ALUNO WHERE NOME="nome";''')

            registro = cursor.fetchone()
            print(registro)
            conexao.commit()
            cursor.close()
            conexao.close()

        except sqlite.DatabaseError as e:
            print("erro ao selecionar aluno ",e)
            conexao.close()


