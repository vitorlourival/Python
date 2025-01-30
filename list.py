lista_Produtos = ["pc","fone","notebook"]
print(f"Produtos: {lista_Produtos}")


while True:
    inpu = input("Adicionar Produto(1)  Remover Produto(2)  Sair(3): ")
    if inpu == "1":
        inpu = input("Digite O nome do Produto para adicionar: ").lower()
        lista_Produtos.append(inpu)
        print(f"{inpu} Foi Adicionado")
        print(f"{lista_Produtos} Lista Atualizada")
    elif inpu == "2":
        inpu = input("Digite O nome do Produto para Remover: ")
        lista_Produtos.remove(inpu)
        print(f"{inpu} Foi Removido")
        print(f"{lista_Produtos} Lista Atualizada")
    elif inpu == "3":
        print("Encerrou")
        break
    else:
        print("COMANDO INVALIDO!!!")
        print("Tente Novamente")
