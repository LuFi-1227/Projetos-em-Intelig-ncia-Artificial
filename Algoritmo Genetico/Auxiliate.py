import random


class Cromossomo:
  '''Classe que define um cromossomo para o algoritmo Genético'''

  def __init__(self, valor, possibilidades, nP, flag, Cromossomo1,
               Cromossomo2) -> None:
    if (flag == 0):
      i = 0
      self.nItens = valor
      self.nTrues = 0
      self.fitness = 0
      self.genes = []
      while i < int(valor):
        self.genes.append(0)
        i = i + 1
    else:
      self.nItens = Cromossomo1.GetNitens()
      self.nTrues = 0
      self.fitness = 0
      self.genes = []
      i = 0
      while i < int(self.nItens):
        if (i < int(self.nItens)/2):
          self.genes.append(Cromossomo1.genes[i])
        else:
          self.genes.append(Cromossomo2.genes[i])
        i = i + 1
  def fitnessC(self, valores):
    i = 0
    while i < int(self.nItens):
      self.fitness = self.fitness + (int(self.genes[i]) * float(valores[i]))
      self.nTrues += int(self.genes[i])
      i = i+1
      
    return self.fitness
    
  def GetFitness(self):
    return self.fitness

  def GetNitens(self):
    return self.nItens

  def mutacao(self, possibilidades):
    g = random.randint(0, len(possibilidades)-1)
    h = random.randint(0, int(self.nItens)-1)
    self.genes.insert(h + 1, possibilidades[g])


def Roleta(Populacao):
  roleta = 0
  i = 0
  while i < len(Populacao)-1:
    roleta = roleta + float(Populacao[i].GetFitness())
    i = i + 1
  sorteio = random.uniform(0, roleta)
  acumulado = 0
  j = 0
  while j < len(Populacao)-1:
    acumulado = acumulado + float(Populacao[i].GetFitness())
    if (sorteio < acumulado):
      return j
    j = j + 1
  return -1


def JaFoi(Pop, n, p):
  i = 0
  while i < len(Pop)-1:
    if (n == Pop[i]):
      return 2
    if (p == Pop[i]):
      return 1
    i = i + 1
  return -1


def Substituicao(POP, FIL):
  i = 0
  posmen = 999
  posmai = 999
  while i < len(POP)-1:
    valmai = -999
    valmen = 999
    j = 0
    while j < len(POP)-1:
      if (POP[j].GetFitness() < valmen):
        posmen = j
        valmen = POP[j].GetFitness()
      j = j+1
      
    k = 0
    while k < len(FIL)-1:
      if (FIL[k].GetFitness() > valmai):
        posmai = k
        valmai = FIL[k].GetFitness()
      k = k + 1
    if valmen < valmai or (valmen == valmai and FIL[posmai].nTrues > POP[posmen].nTrues):
      POP[posmen] = FIL[posmai]
      FIL.pop(posmai)
    i = i + 1
