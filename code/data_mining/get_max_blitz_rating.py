players_file = open('br_players.csv','r')
players = players_file.readlines()
players = [x.strip('\n') for x in players]

max_rapid = 0
max_blitz = 0

print(f'There are {len(players)} players in this file!\n----------------------')

for row in players:
    player_attr = row.split(',')
    if int(player_attr[9]) > max_rapid:
        max_rapid = int(player_attr[9])
        print(f'The new max rapid rating is {max_rapid}')

    if int(player_attr[10]) > max_blitz:
        max_blitz = int(player_attr[10])
        print(f'The new max blitz rating is {max_blitz}')

print('---------------------------------')
print(f'The final max blitz rating is {max_blitz} and the final max rapid rating is {max_rapid}')
