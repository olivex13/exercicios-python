
# EXERCICIOS LISTAS - PYTHON  🛸

## Exercicios em python com o objetivo de se aprimorar na linguagem.

 1.	Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
2.	Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
3.	Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
4.	Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
5.	Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
6.	Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
7.	Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
8.	Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
9.	Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
10.	Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
11.	Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
12.	Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
13.	Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
14.	Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
-          a.	"Telefonou para a vítima?"
           b.	"Esteve no local do crime?"
           c.	"Mora perto da vítima?"
           d.	"Devia para a vítima?"
           e.	"Já trabalhou com a vítima?" 
           
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

15.	Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
- a.	Mostre a quantidade de valores que foram lidos;
- b.	Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
- c.	Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
- d.	Calcule e mostre a soma dos valores;
- e.	Calcule e mostre a média dos valores;
- f.	Calcule e mostre a quantidade de valores acima da média calculada;
- g.	Calcule e mostre a quantidade de valores abaixo de sete;
- h.	Encerre o programa com uma mensagem;

16.	Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
- a.	$200 - $299
- b.	$300 - $399
- c.	$400 - $499
- d.	$500 - $599
- e.	$600 - $699
- f.	$700 - $799
- g.	$800 - $899
- h.	$900 - $999
- i.	$1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

17.	Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

| Atleta            | Primeiro Salto | Segundo Salto | Terceiro Salto | Quarto Salto | Quinto Salto |
|-------------------|----------------|---------------|----------------|--------------|--------------|
| Rodrigo Curvêllo  | 6.5 m          | 6.1 m         | 6.2 m          | 5.4 m        | 5.3 m        |

| Resultado Final   |
|-------------------|
| Média: 5.9 m      |

18 - Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
-  total de votos computados;
- Os númeos e respectivos votos de todos os jogadores que receberam votos;
- O percentual de votos de cada um destes jogadores;
- O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.

Enquete: Quem foi o melhor jogador?

-      Número do jogador (0=fim): 9
       Número do jogador (0=fim): 10
       Número do jogador (0=fim): 9
       Número do jogador (0=fim): 10
       Número do jogador (0=fim): 11
       Número do jogador (0=fim): 10
       Número do jogador (0=fim): 50
       Informe um valor entre 1 e 23 ou 0 para sair!
       Número do jogador (0=fim): 9
       Número do jogador (0=fim): 9
       Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

| Jogador | Votos | %     |
|---------|-------|-------|
| 9       | 4     | 50,0% |
| 10      | 3     | 37,5% |
| 11      | 1     | 12,5% |

O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

19 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server

2- Unix

3- Linux

4- Netware

5- Mac OS

6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

| Sistema Operacional   | Votos | %   |
|-----------------------|-------|-----|
| Windows Server        | 1500  | 17% |
| Unix                  | 3500  | 40% |
| Linux                 | 3000  | 34% |
| Netware               | 500   | 5%  |
| Mac OS                | 150   | 2%  |
| Outro                 | 150   | 2%  |
|-----------------------|-------|-----|
| **Total**             | **8800** |     |

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

20 - As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
- O salário de cada funcionário, juntamente com o valor do abono;
- O número total de funcionário processados;
- O valor total a ser gasto com o pagamento do abono;
- O número de funcionário que receberá o valor mínimo de 100 reais;
- O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

-               Projeção de Gastos com Abono
============================ 
 
- Salário: 1000
- Salário: 300
- Salário: 500
- Salário: 100
- Salário: 4500
- Salário: 0
 
| Salário     | Abono     |
|-------------|-----------|
| R$ 1000.00  | R$ 200.00 |
| R$ 300.00   | R$ 100.00 |
| R$ 500.00   | R$ 100.00 |
| R$ 100.00   | R$ 100.00 |
| R$ 4500.00  | R$ 900.00 |

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00


21 - Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
- O modelo do carro mais econômico;
- Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

| Veículo  | Nome      | Km por litro |
|----------|-----------|--------------|
| Veículo 1 | Fusca     | 7            |
| Veículo 2 | Gol       | 10           |
| Veículo 3 | Uno       | 12.5         |
| Veículo 4 | Vectra    | 9            |
| Veículo 5 | Peugeout  | 14.5         |

| Nº | Veículo     | Km por litro | Consumo (litros) | Custo (R$) |
|----|-------------|--------------|-------------------|------------|
| 1  | Fusca       | 7.0          | 142.9             | R$ 321.43  |
| 2  | Gol         | 10.0         | 100.0             | R$ 225.00  |
| 3  | Uno         | 12.5         | 80.0              | R$ 180.00  |
| 4  | Vectra      | 9.0          | 111.1             | R$ 250.00  |
| 5  | Peugeout    | 14.5         | 69.0              | R$ 155.17  |

O menor consumo é do Peugeout.

22 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

-	Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
-	necessita da esfera;
-	necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

| Situação                              | Quantidade | Percentual |
|---------------------------------------|------------|------------|
| 1 - Necessita da esfera               | 40         | 40%        |
| 2 - Necessita de limpeza              | 30         | 30%        |
| 3 - Necessita troca do cabo/conector  | 15         | 15%        |
| 4 - Quebrado ou inutilizado           | 15         | 15%        |
| **Total**                             | **100**    | **100%**   |

23 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

| Nome      | Telefone    |
|-----------|-------------|
| Alexandre | 456123789   |
| Anderson  | 1245698456  |
| Antonio   | 123456456   |
| Carlos    | 91257581    |
| Cesar     | 987458      |
| Rosemary  | 789456125   |

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

# ACME Inc. - Uso do Espaço em Disco pelos Usuários
------------------------------------------------------------------------
| Nr. | Usuário    | Espaço Utilizado | % do Uso  |
|-----|------------|------------------|-----------|
| 1   | Alexandre  | 434,99 MB        | 16,85%    |
| 2   | Anderson   | 1187,99 MB       | 46,02%    |
| 3   | Antonio    | 117,73 MB        | 4,56%     |
| 4   | Carlos     | 87,03 MB         | 3,37%     |
| 5   | Cesar      | 0,94 MB          | 0,04%     |
| 6   | Rosemary   | 752,88 MB        | 29,16%    |

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

24 - Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
