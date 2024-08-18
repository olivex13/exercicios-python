"""
1 - Classe Bola: Crie uma classe que modele uma bola:
    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
"""

class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material
    
    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        print("Cor Alterada com sucesso")

    def mostraCor(self, cor):
        self.cor = cor
        print(f" A cor da bola é {cor}")

bola = Bola("Amarela", "10cm", "Plastico")

print(bola.cor)

bola.trocaCor("Vermelha")

bola.mostraCor(bola.cor)