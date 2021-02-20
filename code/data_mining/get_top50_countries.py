#!/bin/python3
from chessdotcom import get_country_details, get_country_players, get_player_game_archives, get_player_profile, get_player_stats
import requests
import csv

def loading_bar(atual, maximo):
    qntd = atual * 100 // maximo
    print('[',end='')
    for _ in range(qntd):
        print('|',end='')
    for _ in range(100-qntd):
        print(' ',end='')
    print(']')

# lê as siglas dos países
file_country = open('country_codes.txt', 'r')
codes = file_country.readlines()

# retira o \n no final
codes = [x.strip('\n') for x in codes]

# lista com os países aceitos
acceptable_coutries = []

iterador = 0
for code in codes:
    # pra eu não ficar perdido, implementei essa barra de carregamento
    # pois houve alguns problemas de conexão e eu não sabia se tava pegando os dados
    # ou não estava fazendo nada xD
    loading_bar(iterador,len(codes))
    iterador += 1

    # lógica pra pegar os dados que eu quero
    flag = 0
    try:
        data = get_country_details(code)
    except:
        flag = -1

    # caso tudo tenha dado certo, adiciona o páis na lista
    if flag != -1:
        acceptable_coutries.append(code)

# anúncios
print("TODOS OS PAÍSES ACEITOS FORAM ACHADOS")

d = {}

iterador = 0
for code in acceptable_coutries:
    loading_bar(iterador,len(acceptable_coutries))
    iterador += 1
    try:
        tamanho = len(get_country_players(code).json['players'])
        d[tamanho] = code
    except:
        pass

l = list(d.items())
l.sort()
x = l[-50:]
print(x)
