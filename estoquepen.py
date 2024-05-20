import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="estoquepen"
)

cursor = conexao.cursor()

def inserir_produto():
    nome = input("Digite o nome do produto: ")
    marca_prod = input ("Digite a marca do produto: ")
    fornecedor_prod = input ("Digite o nome do fornecedor: ")
    numero_quant = input ("Digite a quantidade do item: ")
    reposicao = input ("Digite a a data da última reposição: ")
    preco = float(input("Digite o preço do produto: "))

    
    cursor.execute(f"INSERT INTO produtos (nome_prod, marca, fornecedor, quantidade, data_rep, preco_venda) VALUES ('{nome}', '{marca_prod}', '{fornecedor_prod}', '{numero_quant}', '{reposicao}', '{preco}')")
    conexao.commit()
    print("Produto inserido com sucesso!")


def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)

def atualizar_produto():
    id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
    novo_nome = input("Digite o novo nome do produto: ")
    nova_marca = input ("Digite a marca do produto: ")
    novo_fornecedor = input ("Digite o nome do fornecedor: ")
    nova_quant = input ("Digite a nova quantidade: ")
    nova_data = input ("Digite a nova data de reposição: ")
    novo_preco = float(input("Digite o novo preço do produto: "))
    cursor.execute(f"UPDATE produtos SET nome = '{novo_nome}', preco = '{novo_preco}' WHERE id_produto = '{id_produto}'")
    conexao.commit()
    print("Produto atualizado com sucesso!")

def deletar_produto():
    id_produto = int(input("Digite o ID do produto que deseja deletar: "))
    
    cursor.execute(f"SELECT * FROM produtos WHERE id_produto = '{id_produto}'")
    produto = cursor.fetchone()
    if produto:
        
        cursor.execute(f"DELETE FROM produtos WHERE id_produto = '{id_produto}'")
        conexao.commit()
        print("Produto deletado com sucesso!")
    else:
        print("O produto com o ID fornecido não existe.")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Inserir produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Deletar produto")
        print("5. Criar relatório")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")


        if escolha == "1":
            inserir_produto()
        elif escolha == "2":
            listar_produtos()
        elif escolha == "3":
            atualizar_produto()
        elif escolha == "4":
            deletar_produto()
        elif escolha == "5":
            criar_relatorio()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()

conexao.close()