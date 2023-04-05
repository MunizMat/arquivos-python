def listarEstoque():
    for produto in listaDeProdutos:
        print(f'{produto.codigo} - {produto.produto} - {produto.estoque}')

def verificarEstoque():
    for produto in listaDeProdutos:
        if produto.estoque <= produto.limite:
            print(f'{produto.produto} - ESTOQUE BAIXO, ADQUIRIR PRODUTOS')
        else:
            print(f'{produto.produto} - ESTOQUE NORMAL')

def venderProduto():
    prod_a_vender = input("Insira o código do produto a vender: ")
    for produto in listaDeProdutos:
        if produto.codigo == prod_a_vender:
            qtd_a_vender = int(input("Insira a quantidade a ser vendida: "))
            if qtd_a_vender > produto.estoque:
                print("QUANTIDADE EM ESTOQUE INSUFICIENTE")
            else:
                produto.estoque = produto.estoque - qtd_a_vender
                if produto.estoque <= produto.limite:
                    print(f'{produto.codigo} - ESTOQUE BAIXO, ADQUIRIR PRODUTOS')
                with open("/Users/matheusmuniz/Desktop/txt/estoque.txt", "w") as e:
                    estoques = e.write(f'{pendrive.estoque}\n{hd.estoque}\n{monitor.estoque}\n{teclado.estoque}\n{mouse.estoque}\n{impressora.estoque}')

def comprarProduto():
    prod_a_comprar = input("Insira o código do produto a comprar: ")
    for produto in listaDeProdutos:
        if produto.codigo == prod_a_comprar:
            qtd_a_comprar = int(input("Insira a quantidade a ser comprada: "))
            produto.estoque = produto.estoque + qtd_a_comprar
            if produto.estoque <= produto.limite:
                print(f'{produto.codigo} - ESTOQUE BAIXO, ADQUIRIR PRODUTOS')
            with open("/Users/matheusmuniz/Desktop/txt/estoque.txt", "w") as e:
                estoques = e.write(f'{pendrive.estoque}\n{hd.estoque}\n{monitor.estoque}\n{teclado.estoque}\n{mouse.estoque}\n{impressora.estoque}')



class Produtos:
    def __init__(self, codigo, produto, limite, esotoque):
        self.codigo = codigo
        self.produto = produto
        self.limite = limite
        self.estoque = esotoque

class Arquivos:
    def __init__(self, arquivo):
        with open(f"/Users/matheusmuniz/Desktop/txt/{arquivo}.txt", "r") as w:
            self.arquivo = w.readlines()
            self.arquivo = list(map(lambda a: a.strip(), self.arquivo))

codigos = Arquivos("codigos")
produtos = Arquivos("produtos")
limites = Arquivos("limites")
estoques = Arquivos("estoques")


pendrive = Produtos(codigos.arquivo[0], produtos.arquivo[0], int(limites.arquivo[0]), int(estoques.arquivo[0]))
hd = Produtos(codigos.arquivo[1],  produtos.arquivo[1], int(limites.arquivo[1]), int(estoques.arquivo[1]))
monitor = Produtos(codigos.arquivo[2],  produtos.arquivo[2], int(limites.arquivo[2]), int(estoques.arquivo[2]))
teclado = Produtos(codigos.arquivo[3],  produtos.arquivo[3], int(limites.arquivo[3]), int(estoques.arquivo[3]))
mouse = Produtos(codigos.arquivo[4],  produtos.arquivo[4], int(limites.arquivo[4]), int(estoques.arquivo[4]))
impressora = Produtos(codigos.arquivo[5],  produtos.arquivo[5], int(limites.arquivo[5]), int(estoques.arquivo[5]))
listaDeProdutos = [pendrive, hd, monitor, teclado, mouse, impressora]

print('1 - Listar estoque')
print('2 - Verificar estoque')
print('3 - Vender produto')
print('4 - Comprar produto\n')

while True:
    x = int(input('\nInsira a ação desejada: '))
    if x == 1:
        listarEstoque()
    elif x == 2:
        verificarEstoque()
    elif x == 3:
        venderProduto()
    elif x == 4:
        comprarProduto()


