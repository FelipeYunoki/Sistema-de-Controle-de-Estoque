from colorama import Fore, init
init(autoreset=True)

def menu():
    print(Fore.LIGHTBLACK_EX + "===============================")
    print(Fore.WHITE + "Sistema de Controle de Estoque")
    print(Fore.LIGHTBLACK_EX + "===============================")
    print(Fore.YELLOW + "1. Cadastrar Produto")
    print(Fore.YELLOW + "2. Listar Produtos")
    print(Fore.YELLOW + "3. Buscar Produto")
    print(Fore.YELLOW + "4. Atualizar Produto")
    print(Fore.YELLOW + "5. Excluir Produto")
    print(Fore.YELLOW + "6. Sair")

def cadastrar_produto():
    nome = input(Fore.CYAN + "Digite o nome do produto: ")
    preco = float(input(Fore.CYAN + "Digite o preço do produto: "))
    quantidade = int(input(Fore.CYAN + "Digite a quantidade do produto: "))
    
    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    
    produtos.append(produto)
    print(Fore.GREEN + "Produto cadastrado com sucesso!")
    
menu()

#py -m pip install colorama