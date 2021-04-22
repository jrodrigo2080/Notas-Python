import sqlite3 as sqlite

class DAONotas:
    def insertNotas(self, id_aluno, nota_1, nota_2, nota_3, media):


        try:
            con = sqlite.connect("C:\Faculdade\Python\AtividadeNotas\DADOS\DBALUNOS.db")
            cursor = con.cursor()
            comando = '''INSERT INTO NOTAS(ID_ALUNO,NOTA_1,NOTA_2,NOTA_3,MEDIA)VALUES(:ID_ALUNO,:NOTA_1,:NOTA_2,:NOTA_3,:MEDIA);'''
            cursor.execute(comando, {"ID_ALUNO": id_aluno,
                                     "NOTA_1": nota_1,
                                     "NOTA_2": nota_2,
                                     "NOTA_3": nota_3,
                                     "MEDIA": media})
            con.commit()
            con.close()
            print("Nota salva com sucesso!")

        except sqlite.DatabaseError as e:
            print('Erro ao adicionar nota ->', e)
            con.close()
        finally:
            con.close()

    def updateNotas(self, id_aluno, nota_1, nota_2, nota_3, media,id):
        try:
            con = sqlite.connect("C:\Faculdade\Python\AtividadeNotas\DADOS\DBALUNOS.db")
            cursor = con.cursor()
            comando = '''UPDATE NOTAS SET ID_ALUNO:ID_ALUNO,NOTA_1:NOTA_1,NOTA_2:NOTA_2,NOTA_3:NOTA_3,MEDIA:MEDIA WHERE ID:ID ;'''
            cursor.execute(comando, {"ID_ALUNO": id_aluno,
                                     "NOTA_1": nota_1,
                                     "NOTA_2": nota_2,
                                     "NOTA_3": nota_3,
                                     "MEDIA": media,
                                     "ID": id})
            con.commit()
            con.close()
            print("Notas alterada com sucesso!")

        except sqlite.DatabaseError as e:
            print('Erro ao alterar notas ->', e)
            con.close()
        finally:
            con.close()

    def deleteNota(self, id):
        try:
            con = sqlite.connect("C:\Faculdade\Python\AtividadeNotas\DADOS\DBALUNOS.db")
            cursor = con.cursor()
            comando = '''DELETE FROM NOTAS WHERE ID=:ID;'''
            cursor.execute(comando, {"ID": id})
            con.commit()
            con.close()
            print("Aluno deletado com sucesso!")

        except sqlite.DatabaseError as e:
            print('Erro ao deletar aluno ->', e)
            con.close()
        finally:
            con.close()

    def selectNota(self, id_aluno):
        try:
            conexao = sqlite.connect("C:\Faculdade\Python\AtividadeNotas\DADOS\DBALUNOS.db")
            cursor = conexao.cursor()
            cursor.execute('''SELECT * FROM NOTAS WHERE ID_ALUNO:"id_aluno";''')
            registro = cursor.fetchone()
            print(registro)
            conexao.commit()
            cursor.close()
            conexao.close()

        except sqlite.DatabaseError as e:
            print("erro ao selecionar aluno ",e)
            conexao.close()


DAONotas.insertNotas('', 4, 10, 9, 10, 9.66)
