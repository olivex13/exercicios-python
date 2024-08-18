"""
2 - Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self, tamanho_do_lado):
       self.tamanho_do_lado = tamanho_do_lado

    def valor_do_lado(self):

        print(f"O valor do lado é {self.tamanho_do_lado}")

    def mudar_valor_do_lado(self, novo_lado):
        self.tamanho_do_lado = novo_lado 
        print(F" O novo valor do lado é {self.tamanho_do_lado}")
    
    def calcular_area(self):
        tamanho_lado = self.tamanho_do_lado
        area = tamanho_lado * tamanho_lado
        print(f"A area do quadrado é {area}")


quadrado = Quadrado(5)
quadrado.valor_do_lado()
quadrado.calcular_area()
quadrado.mudar_valor_do_lado(10)
quadrado.calcular_area()

   