# 3.	Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print("VERIFICANDO SEU SEXO".center(60))
print('')

print("""
      [F] = Feminino
      [M] = Masculino
      """)
sexo = input(" Digite a opção desejada:  ")

if (sexo == "M" or sexo == "m"):
    print('O sexo selecionado é Masculino.')
elif (sexo == "F" or sexo == "f"):
    print('O sexo selecionado é feminino.')
else:
    print("Sexo selecionado inválido.")


