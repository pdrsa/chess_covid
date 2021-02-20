#!/bin/python3
from random import sample

# abre o arquivo
players_file = open('br_players.csv','r')
players = players_file.readlines()
players = [x.strip('\n') for x in players]

# listas a serem preenchidas
nomes_total = []
nomes_escolhidos = []

# quantidade aleatória a ser escolhida
qntd = 15000

for row in players:
    p = row.split(',')
    nomes_total.append(p[1])

# usernames escolhidos
nomes_escolhidos = sample(nomes_total,qntd)

f = open('random_players.txt','w')
for name in nomes_escolhidos:
    f.write(name)
    f.write('\n')
