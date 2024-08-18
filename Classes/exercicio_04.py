#4 - Classe Pessoa: Crie uma classe que modele uma pessoa:
#    Atributos: nome, idade, peso e altura
#    Métodos: Envelhecer, engordar, emagrecer, crescer. 
#Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
#sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa():

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def envelhecer(self, anos_passados):
        anos_passados = int(anos_passados)
        if self.idade < 21:
            self.altura += (anos_passados * 0.005)
            self.idade += anos_passados
            print(f"A pessoa envelheceu {anos_passados} anos. Sua nova idade é {self.idade} anos e sua nova altura é {self.altura} m.")
        else: 
            self.idade += anos_passados
            print(f"A pessoa envelheceu {anos_passados} anos. Sua nova idade é {self.idade} anos.")
         
    def engordar(self, kgs_engordados):
        kgs_engordados = float(kgs_engordados)
        self.peso += kgs_engordados
        print(f" A pessoa engordou {kgs_engordados} kgs. \n Seu novo peso é: {self.peso} kgs.")

    def emagrecer(self, kgs_perdidos):
        kgs_perdidos = float(kgs_perdidos)
        self.peso -= kgs_perdidos
        print(f" A pessoa perdeu {kgs_perdidos} kgs. \n Seu novo peso é: {self.peso} kgs.")
        

print("DEFININDO PESSOAS".center(60))
print("=" * 60)

nome = input("Digite o nome pessoa: ")
idade = input("Digite a idade da pessoa: ")
peso = input("Digite o peso da pessoa: ")
altura = input ("Digite a altura da pessoa: ")

pessoa = Pessoa(nome, idade, peso, altura)

anos_passados = input("Quantos anos se passaram ? ")
pessoa.envelhecer(anos_passados)

kgs_perdidos = input("Quantos kgs emagreceu? ")
pessoa.emagrecer(kgs_perdidos)

kgs_engordados = input("Quantos kgs ganhou? ")
pessoa.engordar(kgs_engordados)