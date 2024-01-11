'''15.	Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
 Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
-	Dicas:
-	Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
-	Triângulo Equilátero: três lados iguais;
-	Triângulo Isósceles: quaisquer dois lados iguais;
-	Triângulo Escaleno: três lados diferentes; '''

print("==========TRIANGULOS==========".center(60))

def triangulo(lado_1, lado_2, lado_3):
    if ((lado_1 + lado_2) > lado_3):
        return "é triangulo"
    elif((lado_1 + lado_3) > lado_2):
        return "é triangulo"
    elif ((lado_2 + lado_3) > lado_1):
        return "é triangulo"
    else:
        return "não é triangulo"
    
def tipo_triangulo(lado_1, lado_2, lado_3):
    if (lado_1 == lado_2 and lado_2 == lado_3):
        return "Triângulo Equilátero"
    elif (lado_1 == lado_2 or lado_2 == lado_3 or lado_3 == lado_1):
        return "Triângulo Isósceles"
    elif (lado_1 != lado_2 and lado_2 != lado_3):
        return "Triângulo Escaleno"
    
lado_a = int(input('Digite o lado A: '))
lado_b = int(input('Digite o lado B: '))
lado_c = int(input('Digite o lado C: '))  

eh_triangulo = triangulo(lado_a, lado_b, lado_c)
tipo_do_tringulo = tipo_triangulo(lado_a, lado_b, lado_c)

main = (f"""
De acordo com a medidas passadas, {eh_triangulo} e é do tipo {tipo_do_tringulo}
""")

print(main)