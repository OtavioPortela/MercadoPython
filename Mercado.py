from typing import List, Dict
from time import sleep

from models import Produto

produtos: List[Produto] = []

carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('====================================================')
    print('=================Bem Vindo(a) ======================')
    print('==================== ao ============================')
    print('================= Mercadinho =======================')

    print("Selecione uma das opçoes abaixo: ")
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - fechar Pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input('Digite a opçao desejada: '))

    if opcao == 1:
        cadastra_produto()

    elif opcao == 2:
        listar_produtos()

    elif opcao == 3:
        comprar_produto()

    elif opcao == 4:
        visualizar_carrinho()

    elif opcao == 5:
        fechar_pedido()

    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)

    else:
        print('Opçao invalida')
        sleep(1)
        menu()


def cadastra_produto() -> None:
    print('Cadastro de Produto')
    print('===========================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sussesso! ')
    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Lista de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('---------------')
            sleep(1)


    else:
        print("ainda nao existe produtos cadastrados ")
        menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o codigo do produto para adicionar ao carrinho')
        print('-----------------------------------------------------------')
        print('====================Produtos disponveis====================')

        for produto in produtos:
            print(produto)
            print('------------------')
            sleep(1)

        codigo: int = int(input("Digite o codigo: "))

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant +1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho ')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()


            else:
                item = {produto : 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(2)
                menu()
        else:
            print(f'O produdo com codigo {codigo} nao foi encontrado')
            sleep(2)
            menu()

    else:
        print('ainda nao existe produto para vender ')
        sleep(2)
        menu()
def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos do carrinho ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-------------------------')
                sleep(1)

    else:
        print("ainda nao existem produtos no carrinho")
        sleep(2)
        menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total = dados[0].preco * dados[1]
                print('---------------------------------')
                sleep(1)
        print(f'Sua fatura é {Formata_float_str_moeda(valor_total)}')
        print('Volte Sempre')
        carrinho.clear()
        sleep(4)

    else:
        print("ainda nao existe produtos no carrinho ")
        sleep(1)
        menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()