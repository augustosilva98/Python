class Aluno:
    def __init__(self, nome, turma, professor):
        self.nome = nome
        self.turma = turma
        self.professor = professor
        self.notas = {}

    def adicionar_nota(self, materia, nota):
        self.notas[materia] = nota

    def calcular_status(self):
        media = sum(self.notas.values()) / len(self.notas)

        if media >= 6:
            return "Aprovado"
        elif 4 <= media < 6:
            return "Recuperação"
        else:
            return "Reprovado"

    def imprimir_informacoes(self):
        print("Nome do aluno:", self.nome)
        print("Turma:", self.turma)
        print("Nome do professor:", self.professor)

        for materia, nota in self.notas.items():
            print("Nota de", materia + ":", nota)

        print("Status:", self.calcular_status())


aluno1 = Aluno("João", "Turma A", "Professora Maria")
aluno1.adicionar_nota("Matemática", 8)
aluno1.adicionar_nota("Português", 7)
aluno1.adicionar_nota("História", 6)
aluno1.imprimir_informacoes()
