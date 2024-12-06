class Turma:
    def __init__(self):
        self.turma = []
        self.menorNota = None
        self.maiorNota = None

    def cadastrarAlunos(self, alunos):
        for aluno in alunos:
            if aluno.nota < 0 or aluno.nota > 10:
                raise ValueError(f"Nota inválida: {aluno.nota}. Deve estar entre 0 e 10.")
            self.turma.append(aluno)
            if self.menorNota is None or aluno.nota < self.menorNota.nota:
                self.menorNota = aluno
            if self.maiorNota is None or aluno.nota > self.maiorNota.nota:
                self.maiorNota = aluno

    def mostrarAlunos(self):
        print('Quantidade de alunos:', len(self.turma))
        for aluno in self.turma:
            print(aluno.mostrarAluno())
