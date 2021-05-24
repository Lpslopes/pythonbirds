class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade= idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return "Ola"
if __name__ == '__main__':
  lamartine = Pessoa(nome="Lamartine", idade=40)
  luciano = Pessoa(lamartine, nome='luciano')
  lamartine.endereço = 'Rua 6'
  lamartine.olhos = 4
  for filho in luciano.filhos:
      print(filho.nome)
del lamartine.olhos
print(lamartine.__dict__)
print(Pessoa.olhos)
print(lamartine.olhos)

