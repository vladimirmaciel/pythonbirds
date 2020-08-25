class Pessoa:
    def __init__(self, *filhos, nome=None, idade = 42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

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
    print(luciano.__dict__) # confere quais os atributos de instancia do objeto
    print(Vladimir.__dict__)


