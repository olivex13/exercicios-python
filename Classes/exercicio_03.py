"""
3 - Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
    
    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = int(comprimento)
        self.largura = int(largura)
    
    def alterar_lados(self):
        novo_comprimento = input("Digite o novo comprimento: ")
        self.comprimento = int(novo_comprimento)
        nova_largura = input("Digite a nova largura: ")
        self.largura = int(nova_largura)
        print("Medidas alteradas com sucesso")
    
    def valor_dos_lados(self):
        comprimento = int(self.comprimento)
        largura = int(self.largura)
        print(f"O retangulo tem: \n {comprimento}cm de comprimento \n {largura}cm de largura \n")
    
    def calcular_area(self):
        area_cm = int(self.comprimento) * int(self.largura)
        area = area_cm / 10000
        return area
       

    def calcular_perimetro(self):
        perimetro_cm = 2 * (int(self.comprimento) + int(self.largura))
        perimetro = perimetro_cm / 100
        return perimetro
       


  
print("CRIANDO UM RETANGULO".center(60))
print("=" * 60)

comprimento = input("Digite o comprimento em cm: ")
largura = input("Digite a largura em cm: ")

retangulo = Retangulo(comprimento, largura)

retangulo.valor_dos_lados()

print("=" * 60)

retangulo.alterar_lados()

print("=" * 60)

retangulo.valor_dos_lados()

print("=" * 60)

area_do_retangulo = retangulo.calcular_area()
print(f"A area tem {area_do_retangulo}m²")

perimetro_do_retangulo = retangulo.calcular_perimetro()
print(f"O perimetro é de {perimetro_do_retangulo} metros")
print("=" * 60)

print(f"Você vai precisar comprar {area_do_retangulo}m² de piso e {perimetro_do_retangulo} metros de rodapé.")