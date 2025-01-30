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

enemy = random.choice(monstros)
player = input("Digite Seu Nome: ")
print(f"Bem Vindo(a) {player}")
print(f"Turno {turnos}")
while True:
    print(f"Seu Oponente {enemy}")
    for atk in habilidades:
        atkEnm = random.choice(habilidades)
        print(f"Life {life}")
        print("Corte,Flecha,Magia,defesa,cura")
        atk = input("Selecione um Ataque: ")
        if atk == "corte" or "flecha" or "magia":
          if enemy == "defesa":
             print(f"{enemy} Defendeu Seu Ataque")
          else:
             life_enemy -10
             print(f"{enemy} Sofreu 10 de dano")
    
    
    

    

