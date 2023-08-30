class Pessoa:
    def __init__(self):
        self.nome = input("Digite seu nome: ")
        self.altura = float(input("Digite sua altura: ").replace(',', '.'))
        self.peso = float(input("Digite seu peso: ").replace(',', '.'))
        mostrar_dados(self)


def mostrar_dados(self):
    print(f"Nome: {self.nome}")
    print(f"Altura: {self.altura:.2f}")
    print(f"Peso: {self.peso}")
