import random
life = 50
life_enemy = 50
dano = 50
turnos = 1

habilidades = [
    "corte",
    "flecha" ,
    "magia",
    "defesa",
    "cura"     
]
monstros = [
    "ogro",
    "mumia",
    "alien"
]

player = input("Digite Seu Nome: ")
print(f"Bem Vindo(a) {player}")
enemy = random.choice(monstros)
print(f"Seu Oponente {enemy}")
print(f"Turno {turnos}")
while life and life_enemy > 0:
    print(f"Turno: {turnos}")
    print(f"Player Life: {life}  Enemy Life: {life_enemy}")

    for atk in habilidades:
        #atkEnm = random.choice(habilidades)
        print(f"Life {life}")
        print("Corte,Flecha,Magia,defesa,cura")

        atk = input("Selecione um Ataque: ")
        if atk == "corte" or "flecha" or "magia":
          if enemy == "defesa":
             print(f"{enemy} Defendeu Seu Ataque")
          else:
             life_enemy -10
             print(f"{enemy} Sofreu 10 de dano")
        elif atk == "defesa":
           print(f"Player usou {atk}")
    
    for atkEnm in habilidades:
        atkEnm = random.choice(habilidades)
        print(f"Life {life}")
        print("Corte,Flecha,Magia,defesa,cura")

        if atkEnm == "corte" or "flecha" or "magia":
          if player == "defesa":
             print(f"{player} Defendeu Seu Ataque")
          else:
             life -10
             print(f"{player} Sofreu 10 de dano")
        elif atkEnm == "defesa":
           print(f"Player usou {atk}")
    
    
    

    

