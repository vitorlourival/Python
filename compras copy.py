saldo = 1000
#valor = 0
produtos = {
"mouse" :50,
"teclado" : 70,
"monitor" : 150
}


print(f"Bem Vindo(a)")
for produto,preco in produtos.items():
                print(f"{produto}: {preco}")
while True:
        cliente = input("Qual Produto Deseja Comprar? ou (sair), veja seu saldo(saldo)").lower()
#valor = int(input("Qual o valor do produto?"))

        if cliente in produtos and saldo >= preco:
         print("Comprado")
        else:
          print("Compra Negada")

        if cliente == "saldo":
                print(f"Saldo: {saldo}")
        elif cliente == "sair":
                print("Obrigado!Volte sempre")
                break


