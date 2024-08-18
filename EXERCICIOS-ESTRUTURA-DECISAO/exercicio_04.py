# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print("VERIFICANDO SE É VOGAL OU CONSOANTE".center(60))

letra = input("Digite uma letra: ")
letra = letra.lower()

if letra in 'aeiou':
    print(f'A letra "{letra}" é uma vogal.')
else:
    print(f'A letra "{letra}" é uma consoante.')