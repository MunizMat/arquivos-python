
def varName(p):
    for k, v in globals().items():
        if id(p) == id(v):
            return k

def openFileAppend(FileName, y ):
    with open(f"/Users/matheusmuniz/Desktop/txt/folyScented/{FileName}.txt", "r") as u:
        globals()[f'{FileName}'] = u.readlines()
        globals()[f'{FileName}'] = list(map(lambda a: a.strip(), globals()[f'{FileName}']))
        globals()[f'{FileName}'].append(y)

def openFile(FileName):
    with open(f"/Users/matheusmuniz/Desktop/txt/folyScented/{FileName}.txt", "r") as u:
        globals()[f'{FileName}'] = u.readlines()
        globals()[f'{FileName}'] = list(map(lambda a: a.strip(), globals()[f'{FileName}']))

def openFile4Writing(Filename, Mode, ToWrite):
    with open(f"/Users/matheusmuniz/Desktop/txt/folyScented/{Filename}.txt", f"{Mode}") as u:
        u.write(f'{ToWrite}\n')

def eraseFiles():
    for x in vars(dif):
        openFile4Writing(x, "w", "")

def deleteProduct(product):
    d = vars(product)
    for x in d:
        openFile(x)
        globals()[f'{x}'].remove(str(d[x]))
        openFile4Writing(x, "w", '')
        for y in globals()[f'{x}']:
            openFile4Writing(x, 'a', y)

def getIndex(List, Item):
    return List.index(Item)


cafe = 160
folyScented = 212
valorBase = 25
valorCera = 40
valorGordura = 11
listaDeProdutos = []

class Produtos:
    margemDeLucro = 2
    def __init__(self, capacidade, valorEssencia, precoRecipiente):
        if valorEssencia == folyScented:
            self.margemDeLucro = 2.5
        self.margemDeLucro = self.margemDeLucro
        self.valoresFixos = self.valoresFixos
        self.porcentagemBase = self.porcentagemBase
        self.porcentagemEssencia = self.porcentagemEssencia
        self.nome = f'{type(self).__name__} {varName(valorEssencia)} {capacidade}mL'
        self.capacidade = capacidade
        self.precoRecipiente = precoRecipiente
        self.quantidadeBase = capacidade * self.porcentagemBase
        self.quantidadeEssencia = capacidade * self.porcentagemEssencia
        self.custoBase = round((self.quantidadeBase * valorBase) / 1000)
        self.custoEssencia = round((self.quantidadeEssencia * valorEssencia) / 1000)
        self.custoLiquido = round(self.custoBase + self.custoEssencia)
        self.custoSemEmbalagens = round(self.custoLiquido + self.precoRecipiente)
        self.custo = round(self.custoBase + self.custoEssencia + self.valoresFixos + self.precoRecipiente)
        self.preco = self.custo * (self.margemDeLucro + 1)
        listaDeProdutos.append(self)
        d = vars(self)
        openFile('nome')
        if self.nome not in nome:
            for x in d:
                openFile4Writing(x, "a", d[x])


class Vela(Produtos):
    valoresFixos = 8.8
    margemDeLucro = 1.5
    def __init__(self, capacidade, valorEssencia):
        self.valoresFixos = self.valoresFixos
        self.margemDeLucro = self.margemDeLucro
        self.nome = f'{type(self).__name__} {varName(valorEssencia)}'
        self.capacidade = capacidade
        self.precoRecipiente = 7
        self.quantidadeEssencia = 20
        self.quantidadeCera = 90
        self.quantidadeGordura = 70
        self.custoEssencia = round((self.quantidadeEssencia * valorEssencia) / 1000)
        self.custoCera = round(self.quantidadeCera * valorCera / 1000)
        self.custoGordura = round(self.quantidadeGordura * valorGordura / 500)
        self.custoSemEmbalagens = round(self.custoEssencia + self.custoCera + self.custoGordura + self.precoRecipiente)
        self.custo = round(self.custoSemEmbalagens + self.valoresFixos)
        self.preco = self.custo * (self.margemDeLucro + 1)

class Difusor(Produtos):
    valoresFixos = 8.76
    porcentagemBase = 0.84
    porcentagemEssencia = 0.16
    def __init__(self, capacidade, valorEssencia, precoRecipiente):
        super().__init__(capacidade, valorEssencia, precoRecipiente)


class HomeSpray(Produtos):
    valoresFixos = 4.8
    porcentagemBase = 0.88
    porcentagemEssencia = 0.12
    def __init__(self, capacidade, valorEssencia, precoRecipiente):
        super().__init__(capacidade, valorEssencia, precoRecipiente)

class AguaDeLencois(Produtos):
    margemDeLucro = 1.5
    valoresFixos = 4.8
    porcentagemBase = 0.90
    porcentagemEssencia = 0.10
    def __init__(self, capacidade, valorEssencia, precoRecipiente):
        super().__init__(capacidade, valorEssencia, precoRecipiente)

class Perfume(Produtos):
    valoresFixos = 4.8
    porcentagemBase = (200/3)/100
    porcentagemEssencia = 1-porcentagemBase
    margemDeLucro = 2
    def __init__(self, capacidade, valorEssencia, precoRecipiente):
        super().__init__(capacidade, valorEssencia, precoRecipiente)


dif = Difusor(250, cafe, 9.5)
dif_FS = Difusor(250, folyScented, 9.5)
agLen = AguaDeLencois(200, cafe, 4)
agLen_FS = AguaDeLencois(200, folyScented, 4)
per = Perfume(30, cafe, 7.5)
per_FS = Perfume(30, folyScented, 7.5)
hm250 = HomeSpray(250, cafe, 8.5)
hm250_FS = HomeSpray(250, folyScented, 8.5)
hm500 = HomeSpray(500, cafe, 10)
hm500_FS = HomeSpray(500, folyScented, 10)
velaa = Vela(500, cafe)
velaafs = Vela(500, folyScented)
print(velaa.custoSemEmbalagens)
print(velaafs.custoSemEmbalagens)



