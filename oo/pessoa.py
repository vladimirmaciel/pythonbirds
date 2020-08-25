class Pessoa:
    olhos=2 #atributo default ou atributo de calsse
    def __init__(self, *filhos, nome=None, idade = 42):

        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'
if __name__ == '__main__':
    Vladimir = Pessoa(nome='Vladimir', idade=25)
    luciano = Pessoa(Vladimir, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome,filho.idade)
    luciano.sobrenome = 'Serra' #atributo dinâmico
    del  luciano.filhos #removendo um atributo dinamicamente
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__) # confere quais os atributos de instancia do objeto
    print(Vladimir.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(Vladimir.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(Vladimir.olhos))
    print(Pessoa.metodo_estatico())
    print(luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),luciano.nome_e_atributos_de_classe())

