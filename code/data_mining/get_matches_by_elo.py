#!/bin/python3
from chessdotcom import get_player_games_by_month
import json
import csv

players_file = open('by_elo_players.txt','r')
# cada elemento de players é um username
players = players_file.readlines()
players = [x.strip('\n') for x in players]

# essa lista serve pra evitar ter que repegar os dados
ja_contabilizados = []

try:
    file_tmp = open('matches_by_elo.csv', 'r')
    reader = csv.reader(file_tmp)

    for row in reader:
        ja_contabilizados.append(row[0])

    file_tmp.close()
except:
    pass

# criação do arquivo csv
with open('matches_by_elo.csv', 'a') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # criação do header do arquivo csv
    filewriter.writerow(['url', 'white_username', 'black_username', 'end_time', 'time_control', 'time_class', 'rules', 'rated'])

    # lista de anos e meses que eu vou pegar
    years = ['2019', '2020']
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for i in range(len(players)):
        print('\tPegando partidas do jogador',players[i],'!!!')
        for ano in years:
            for mes in months:
                try:
                    ma_atual = get_player_games_by_month(players[i],ano,mes)
                except:
                    continue

                if len(ma_atual.json['games']) == 0:
                    # o player não jogou partidas nesse mes/ano
                    continue

                print(f'\t\tpegando de {mes}/{ano}!!!')

                # partidas é uma lista
                partidas = ma_atual.json['games']

                for j in range(len(partidas)):
                    curr_match = partidas[j]

                    if curr_match['url'] in ja_contabilizados:
                        print('Essa partida',curr_match['url'],'já foi contabilizada, indo para a próxima!')
                        continue

                    match_to_add = []

                    try:
                        match_to_add.append(curr_match['url'])
                        match_to_add.append(curr_match['white']['username'])
                        match_to_add.append(curr_match['black']['username'])
                        match_to_add.append(curr_match['end_time'])
                        match_to_add.append(curr_match['time_control'])
                        match_to_add.append(curr_match['time_class'])
                        match_to_add.append(curr_match['rules'])
                        match_to_add.append(curr_match['rated'])
                    except:
                        print('ERRO NA FORMAÇÂO DE MATCH_TO_ADD')

                    filewriter.writerow(match_to_add)

    print("FINALIZADO\n================================")
    print("Não consegui pegar os dados de ", nao_conseguiram, "  partidas!!! :(", sep='')
