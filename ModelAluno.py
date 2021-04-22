import  DAOAluno as a
class ModelAluno:

    def __init__(self, nome, turma, id):
        self.id = id
        self.nome = nome
        self.turma = turma

class nota:

    def __init__(self, id, id_aluno, nota_1, nota_2, nota_3, media):
        self.id = id
        self.id_aluno = id_aluno
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.media = media

