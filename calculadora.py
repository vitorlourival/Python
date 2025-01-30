soma = 0
tabuada = input("Qual deseja? '+' '-' '*'")
inp = int(input("escolha um numero: "))
contador = 0
if tabuada == "+":
    while contador < 10:
        contador +=1
        result = inp + contador
        print(f"{inp} + {contador} = {result}")