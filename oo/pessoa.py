class Pessoa:
    olhos=2 #atributo default ou atributo de calsse
    def __init__(self, *filhos, nome=None, idade = 42):

        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    @property
    def comprimentar(self):
        return f'Olá meu nome é  {self.nome}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'


class Homem(Pessoa):
    def comprimentar(self):
        # comprimentar_da_classe=super().comprimentar
        return f'{super().comprimentar}. Aperto de Mão'



class Mutante(Pessoa):
     olhos = 3 #sobrescrevendo a Classe Pessoa modificando o atributo olhos para 3

if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')
    luciano = Homem(renzo, nome='Luciano')
    print(Pessoa.comprimentar)
    print(id(luciano))
    print(luciano.comprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome,filho.idade)
    luciano.sobrenome = 'Ramalho' #atributo dinâmico
    del  luciano.filhos #removendo um atributo dinamicamente
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__) # confere quais os atributos de instancia do objeto
    print(renzo.__dict__)
    # Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico())
    print(luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(renzo.comprimentar)
    print(luciano.comprimentar())

