#!/bin/python3
# abre o arquivo
players_file = open('br_players.csv','r')
players = players_file.readlines()
players = [x.strip('\n') for x in players]

# obtido por get_max_blitz_rating.py; é o maior rating de blitz atingido
max_blitz = 3051

# tamanho da população que quero pegar
tam = 15000

# quantidade de pessoas em cada intervalo
qntd = 10

# tamanho do intervalo
# reduzi com o -1 pois sem isso estava tendo uma quantidade muito pequena de resultados
intervalo = (max_blitz * qntd) // tam - 1

# dicionário que mantém conta dos intervalos
d_intervalo = {}

# lista com todos os usernames escolhidos
nomes_escolhidos = []

for row in players:
    p = row.split(',')

    # pega dados do jogador atual
    username = p[1]
    blitz_rating = int(p[10])

    # acha a posicao no dicionario
    posicao = blitz_rating // intervalo

    if posicao in d_intervalo:
        if d_intervalo[posicao] > 10:
            pass
        else:
            d_intervalo[posicao] += 1
            nomes_escolhidos.append(username)
    else:
        d_intervalo[posicao] = 1
        nomes_escolhidos.append(username)

f = open('by_elo_players.txt','w')
for name in nomes_escolhidos:
    f.write(name)
    f.write('\n')
