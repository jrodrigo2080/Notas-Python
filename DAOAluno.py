import sqlite3 as sqlite

class DAOAluno:

    def insertAluno(self, nome, turma):
        try:
            con = sqlite.connect("./DADOS/DBALUNOS.db")
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
            con = sqlite.connect("./DADOS/DBALUNOS.db")
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
            con = sqlite.connect("./DADOS/DBALUNOS.db")
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
            conexao = sqlite.connect("./DADOS/DBALUNOS.db")
            cursor = conexao.cursor()
            cursor.execute('''SELECT * FROM ALUNO WHERE NOME="nome";''')

            registro = cursor.fetchone()
            print(registro)
            conexao.commit()
            cursor.close()
            conexao.close()

        except sqlite.DatabaseError as e:
            print("erro ao selecionar aluno ", e)
            conexao.close()


    #ALUNO = insertAluno('','maria','j')

    aluno = selectAluno('', 'maria')


