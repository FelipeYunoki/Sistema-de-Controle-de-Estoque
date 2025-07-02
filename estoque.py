from colorama import Fore, init
init(autoreset=True)

produtos = []

def menu():
    print(Fore.LIGHTBLACK_EX + "===============================")
    print(Fore.WHITE + "Sistema de Controle de Estoque")
    print(Fore.LIGHTBLACK_EX + "===============================")
    print(Fore.YELLOW + "1. Cadastrar Produto")
    print(Fore.YELLOW + "2. Listar Produtos")
    print(Fore.YELLOW + "3. Buscar Produto")
    print(Fore.YELLOW + "4. Atualizar Produto")
    print(Fore.YELLOW + "5. Excluir Produto")
    print(Fore.YELLOW + "0. Sair")

def cadastrar_produto():
    while True:
        print(Fore.LIGHTBLACK_EX + "===============================")
        nome = input(Fore.CYAN + "Nome do produto: ")
        preco = float(input(Fore.CYAN + "Preço do produto: "))
        estoque = int(input(Fore.CYAN + "Quantidade em estoque: "))

        produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque}

        produtos.append(produto)

        continua = input(Fore.CYAN + "Deseja cadastrar outro produto(s/n): ")

        if continua.lower() != 's':
            break 

def lista_produtos():
    if produtos == []:
        print(Fore.RED + "Nenhum produto cadastrado")
    else:
        for produto in produtos:
            print(Fore.GREEN + f"{produto['nome']} - R${produto['preco']} - {produto['estoque']} unidade")

def buscar_produto():
    nome_busca = input("Digite o nome do produto: ") 

    encontrado = False
    for produto in produtos:
        if produto["nome"].lower() == nome_busca.lower():
            print(Fore.GREEN + "Produto encontrado")
            print(Fore.YELLOW + f"{produto['nome']} - R${produto['preco']} - {produto['estoque']} unidade")
            encontrado = True
            break

        if not encontrado:
            print(Fore.RED + "Produto não encontrado.")

def autualizar_produto():
    nome_atualizar = input("Digite o nome do produto para atualizar: ")

    for produto in produtos:
        if produto["nome"].lower() == nome_atualizar.lower():
            print(Fore.GREEN + "Produuto encontrado")
            novo_preco = float(input("Novo preço: "))
            novo_estoque = int(input("Novo estoque: "))
            produto["preco"] = novo_preco
            produto["estoque"] = novo_estoque
            break
    else:
        print(Fore.RED + "Produto não encontrado.")
menu()

opcao = input(Fore.CYAN + "\nEscoha uma opção(1, 2, 3, 4, 5 ou 0 para sair): ")

while True:
    match opcao:
        case "1":
            cadastrar_produto()
        case "2":
            lista_produtos()
        case "3":
            buscar_produto()
        case "4":
            autualizar_produto()

    opcao = input(Fore.CYAN + "\nEscoha uma opção(1, 2, 3, 4, 5 ou 0 para sair): ")
#py -m pip install colorama