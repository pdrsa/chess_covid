#!/bin/python3
# esse script foi feito para decidir se o rating do blitz ou do rapid
# é melhor espaçado entre os ratings
import matplotlib
import matplotlib.pyplot as plt

players_file = open('br_players.csv','r')
players = players_file.readlines()
players = [x.strip('\n') for x in players]

# o maximo de ambas as categorias, achado pelo get_max_blitz_rating.py
max_blitz = 3051
max_rapid = 2759

# tamanho da população que quero pegar
tam = 15000

# tamanho dos intervalos
i_blitz = tam // max_blitz
i_rapid = tam // max_rapid

# caso os intervalos acabem por excluir um pouco do topo, aumente eles
if tam > max_blitz * i_blitz:
    i_blitz+=1
if tam > max_rapid * i_rapid:
    i_rapid+=1

# cria listas para receber cada valor individual
l_blitz = []
l_rapid = []

for row in players:
    player_attr = row.split(',')
    # rating para rapid e blitz de um player qualquer atual
    l_rapid.append(int(player_attr[9]))
    l_blitz.append(int(player_attr[10]))

# por fim, plota-se os histogramas
# os limites no eixo y se trata pelo limite escolhido para get_matches_by_elo.py
axes = plt.gca()
axes.set_ylim([0,10])
plt.title('BLITZ')
plt.hist(l_blitz, edgecolor='k', bins=(max_blitz//i_blitz)+1)
plt.show()
axes = plt.gca()
axes.set_ylim([0,10])
plt.title('RAPID')
plt.hist(l_rapid, edgecolor='k', bins=(max_rapid//i_rapid)+1)
plt.show()
