# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print("VERIFICANDO SE É VOGAL OU CONSOANTE".center(60))

while True:
    letra = input("Digite uma letra: ")
    letra = letra.lower()

    if len(letra) == 1 and letra.isalpha():
        break
    else:
        print(' \n Digite uma letra válida')
        print('======================== \n')

if letra in 'aeiou':
    print(f'A letra "{letra}" é uma vogal.')
else:
    print(f'A letra "{letra}" é uma consoante.')