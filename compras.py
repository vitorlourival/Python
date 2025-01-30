saldo = 100 
produtos = {
"mouse" :30,
"teclado" : 50,
"monitor" : 100
}

print(f"Bem Vindo(a)")

while True:
    
    print(f"Catalogo: {produtos}")
    cliente = input("Qual Produto Deseja Comprar? ou (sair), veja seu saldo(saldo)")
    if cliente == "saldo":
        print(f"Saldo: {saldo}")
        continue
    if cliente == "sair":
        print("Obrigado volte Sempre")
        break
    if cliente == "mouse" and saldo >= 30:
        print("Compra Realizado")
        saldo -= 30
        print(f"Saldo: {saldo}")
    elif    cliente == "teclado" and saldo >=50:
        print("Compra Realizado")
        saldo -= 50
        print(f"Saldo: {saldo}")
    elif    cliente == "monitor" and saldo >=100:
        print("Compra Realizado")
        saldo -= 100
        print(f"Saldo: {saldo}")
    else:
        print("Saldo Insuficiente!!!")
    