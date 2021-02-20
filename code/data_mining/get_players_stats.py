#!/bin/python3
from chessdotcom import get_country_details, get_country_players, get_player_game_archives, get_player_profile, get_player_stats
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
print("AGORA SERÁ CRIADO O ARQUIVO CSV PARA CADA USUÁRIO DE CADA PÁIS")

# primeiro quero criar um mecanismo para que caso o programa pare eu possa retomar de onde parei sem maiores problemas
ja_contabilizados = []

try:
    file_tmp = open('players.csv', 'r')
    reader = csv.reader(file_tmp)

    for row in reader:
        ja_contabilizados.append(row[1])

    file_tmp.close()
except:
    pass


# após criar a lista de ja contabilizados eu posso continuar o script
nao_conseguiram = 0

# criação do arquivo csv
with open('players.csv', 'a') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # criação do header do arquivo csv
    filewriter.writerow(['player_id', 'username', 'country', 'followers', 'last_online', 'joined', 'is_streamer', 'status', 'title', 'best_rapid_rating', 'best_blitz_rating', 'best_bullet_rating'])

    # iteração pra cada país
    for country in acceptable_coutries:
        print('COMEÇANDO A PEGAR OS PLAYERS DO PAIS ', country, '!!! (',str(acceptable_coutries.index(country)),str(len(acceptable_coutries)),')')
        # pega todos os players de um país e cria uma lista com todos os usernames
        players = get_country_players(country).json['players']

        # para cada jogador do país
        for i in range(len(players)):
            # caso o player já tenha sido contabilizado, pule para o próximo
            if players[i] in ja_contabilizados:
                print(players[i], "já foi contabilizado! Passando para o próximo!",sep=' ')
                continue

            # o try é necessário pra ignorar problemas de conexão
            try:
                # todos os dados do jogador atual
                player_profile_data = get_player_profile(players[i]).json
                player_stats_data = get_player_stats(players[i]).json

                # dados do jogador atual que vão pro csv
                current_player = []

                # adicionando os dados na ordem correta
                current_player.append(player_profile_data['player_id'])
                current_player.append(player_profile_data['username'])
                current_player.append(player_profile_data['country'][-2:])
                current_player.append(player_profile_data['followers'])
                current_player.append(player_profile_data['last_online'])
                current_player.append(player_profile_data['joined'])
                current_player.append(player_profile_data['is_streamer'])
                current_player.append(player_profile_data['status'])
                # como os próximos campos podem ou não existir, eu usarei try except pra cada um deles
                try:
                    current_player.append(player_profile_data['title'])
                except:
                    current_player.append('None')
                try:
                    current_player.append(player_stats_data['chess_rapid']['best']['rating'])
                except:
                    current_player.append(0)
                try:
                    current_player.append(player_stats_data['chess_blitz']['best']['rating'])
                except:
                    current_player.append(0)
                try:
                    current_player.append(player_stats_data['chess_bullet']['best']['rating'])
                except:
                    current_player.append(0)

                # após a criação da lista de dados que eu quero adicionar, basta escrever no arquivo
                print("Adicionando o jogador",players[i],"!!!")
                filewriter.writerow(current_player)
            except:
                nao_conseguiram += 1
                print("ERRO: Não foi possível adicionar o jogador",players[i],"!!!")

print("FINALIZADO\n================================")
print("Não consegui pegar os dados de ", nao_conseguiram, "  players!!! :(", sep='')
