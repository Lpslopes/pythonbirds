class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade= idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return "Ola"
if __name__ == '__main__':
  lamartine = Pessoa(nome="Lamartine",idade=40)
  luciano = Pessoa(lamartine, nome='luciano')
  for filho in luciano.filhos:
      print(filho.nome)

