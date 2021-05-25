class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade= idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return "Ola"

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} olhos {cls.olhos}'


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
print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
print(Pessoa.nome_e_atributo_de_classe(), luciano.nome_e_atributo_de_classe())

