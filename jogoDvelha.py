import random
import time
pontos = 0
opcoes = ["pedra","papel","tesoura"]

while True:
    
    player = input("Escolha Pedra Papel Tesoura: ").lower()
    cpu = random.choice(opcoes)
    if player not in opcoes:
        print("Comando Invalido!!!")
        continue
    if player == cpu:
        print(f"Jogador escolheu {player} e cpu escolheu {cpu}")
        time.sleep(2.5)
        print("Empate")    
    elif player == "pedra" and cpu == "tesoura" or \
         player == "tesoura" and cpu == "papel" or \
         player == "papel"  and cpu == "pedra":
         
         print(f"Jogador escolheu {player} e cpu escolheu {cpu}")
         time.sleep(2.5)
         print("Jogador vençeu")
         pontos +=1
         print("Vc Ganhou 1 Ponto")
         print(f"{pontos} Pontos")      
    else:
        
        print(f"Jogador escolheu {player} e cpu escolheu {cpu}")
        print("cpu ganhou")
        time.sleep(2.5)
        pontos -=1
        print("Vc perdeu 1 Ponto")
        print(f"{pontos} Pontos")
        