class Carro:
    def __init__(self, nome, cor, potencia, portas):
        self.nome = nome
        self.cor = cor
        self.potencia = potencia
        self.portas = portas

class CarroNovo(Carro):
    def __str__(self):
        return f"Carro novo\nNome: {self.nome}\nCor: {self.cor}\nPotência: {self.potencia}\nPortas: {self.portas}"

class CarroUsado(Carro):
    def __init__(self, nome, cor, potencia, portas, ano_fabricacao):
        super().__init__(nome, cor, potencia, portas)
        self.ano_fabricacao = ano_fabricacao

    def __str__(self):
        return f"Carro usado\nNome: {self.nome}\nAno de fabricação: {self.ano_fabricacao}\nCor: {self.cor}\nPotência: {self.potencia}\nPortas: {self.portas}"

carro_novo = CarroNovo("Gol", "Azul", "1.6", 4)
carro_usado = CarroUsado("Civic", "Vermelho", "1.8", 2, 2019)

print(carro_novo)
print(carro_usado)
