import random
import time

import matplotlib.pyplot as plt

import Auxiliate as a

melhor2 = []
'''print("Quantos valores haverão para trabalhar?")
valor = input()
print("Quantas possibilidades de variável haverão para trabalhar?")
nP = input()
possibilidades = []
print("Digite as possibilidades uma por uma e em ordem:")
i = 0
while i < int(nP):
  possibilidades.append(input())
  i = i + 1
valores = []
print("Digite os pesos de cada valor para fitness em ordem e um por um:")
i = 0
while i < int(valor):
  valores.append(input())
  i = i + 1
Aqui criamos a matriz e iniciamos o projeto
print("Digite o tamanho maximo da população:")
Npop = input()'''

valor = 5
nP = 3
possibilidades = [0, 1, 2]
valores = [1, 2, 4, 1, 12]
PesoMax = 15
Npop = 10

i = 0
Populacao = []
nTrues = 0
posicao = 999
Geracao = 0
var = 1

maior = a.Cromossomo(valor, possibilidades, nP, 0, None, None)
maior.nTrues = 0

while i < int(Npop):
  Populacao.append(a.Cromossomo(valor, possibilidades, nP, 0, None, None))
  Populacao[i].fitnessC(valores)
  if (Populacao[i].fitness > PesoMax):
    Populacao[i].fitness = 0.1

  if (Populacao[i].nTrues > maior.nTrues and Populacao[i].fitness != 0.1):
    maior = Populacao[i]
    posicao = i
  i = i + 1

var = 0
MaxGer = 300
vet = []
ger = []
melhor2.append(0)
while var <= MaxGer:
  ger.append(var)
  Filhos = []
  Reproduzidos = []
  i = 0
  aux = Populacao.copy()

  while i < int(Npop):
    Cromo1 = a.Roleta(aux)
    Cromo2 = a.Roleta(aux)

    if (Cromo1 == Cromo2 or a.JaFoi(Reproduzidos, Cromo1, Cromo2) > 0):
      if (Cromo1 == Cromo2 or a.JaFoi(Reproduzidos, Cromo1, Cromo2) == 1):
        Cromo2 = a.Roleta(aux)
      else:
        Cromo1 = a.Roleta(aux)
    Reproduzidos.append(Cromo1)
    Reproduzidos.append(Cromo2)
    aux.pop(Cromo1)
    aux.pop(Cromo2)

    Filhos.append(
        a.Cromossomo(None, None, None, 1, Populacao[Cromo1],
                     Populacao[Cromo2]))
    Filhos.append(
        a.Cromossomo(None, None, None, 1, Populacao[Cromo2],
                     Populacao[Cromo1]))
    i = i + 2

  k = random.randint(0, int(Npop) - 1)
  Filhos[k].mutacao(possibilidades)
  i = 0
  Geracao = Geracao + 1

  while i < int(Npop):
    Filhos[i].fitnessC(valores)
    if (Filhos[i].fitness > PesoMax):
      Filhos[i].fitness = 0.1
    i = i + 1

  a.Substituicao(Populacao, Filhos)
  j = 0
  soma = 0
  while j < int(Npop):
    soma += Populacao[j].GetFitness()
    j +=1

  vet.append(soma/Npop)
  i = 0
  while i < int(Npop):
    if (float(Populacao[i].GetFitness()) >= float(maior.GetFitness())):
      if(float(Populacao[i].GetFitness()) > float(maior.GetFitness())):
        maior = Populacao[i]
        posicao = i
      else:
        if(int(Populacao[i].nTrues > maior.nTrues)):
          maior = Populacao[i]
          posicao = i
    i = i + 1

  melhor2.append(maior.fitness)

  if (Geracao == MaxGer):
    print("O valor desejado na população se encontra na posição", posicao,
          "Com o vetor:")
    print(maior.genes)
    print("E com o Fitness:")
    print(maior.GetFitness())
    print(Geracao, "Gerações")
  var += 1
  
ger.append(var)
plt.plot(ger, melhor2)
plt.grid()
plt.show()
print("Finni")