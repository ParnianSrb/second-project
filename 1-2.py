input_list = []
game_list = []
game_1, game_2, game_3, game_4, game_5, game_6 = [dict() for _ in range(6)]

for i in range(0, 6):
    input_list.append(input())
    # input_list = ['2-2', '2-1', '1-2', '2-2', '3-1', '2-1']

for i in range(0, 6):
    game = input_list[i].split('-')  # split('-', 1)
    game_list.append(game)
    # game_list = [['2', '2'], ['2', '1'], ['1', '2'], ['2', '2'], ['3', '1'], ['2', '1']]

game_1['Iran'] = game_list[0][0]
game_1['Spain'] = game_list[0][1]
game_2['Iran'] = game_list[1][0]
game_2['Portugal'] = game_list[1][1]
game_3['Iran'] = game_list[2][0]
game_3['Morocco'] = game_list[2][1]
game_4['Spain'] = game_list[3][0]
game_4['Portugal'] = game_list[3][1]
game_5['Spain'] = game_list[4][0]
game_5['Morocco'] = game_list[4][1]
game_6['Portugal'] = game_list[5][0]
game_6['Morocco'] = game_list[5][1]

game_list_dict = [game_1, game_2, game_3, game_4, game_5, game_6]
# game_list_dict = [{'Iran': '2', 'Spain': '2'}, {'Iran': '2', 'Portugal': '1'}, {'Iran': '1', 'Morocco': '2'},
# {'Spain': '2', 'Portugal': '2'}, {'Spain': '3', 'Morocco': '1'}, {'Portugal': '2', 'Morocco': '1'}]

iran_wins, spain_wins, portugal_wins, morocco_wins = 0, 0, 0, 0
iran_loses, spain_loses, portugal_loses, morocco_loses = 0, 0, 0, 0
iran_draws, spain_draws, portugal_draws, morocco_draws = 0, 0, 0, 0
iran_scored, spain_scored, portugal_scored, morocco_scored = 0, 0, 0, 0
iran_conceded, spain_conceded, portugal_conceded, morocco_conceded = 0, 0, 0, 0

for dict_item in game_list_dict:
    keys_item = list(dict_item.keys())
    values_item = list(dict_item.values())
    # print(keys_item, values_item)

    if keys_item[0] == 'Iran':
        iran_scored += int(values_item[0])
        iran_conceded += int(values_item[1])
        if int(values_item[0]) > int(values_item[1]):
            iran_wins += 1
        elif int(values_item[0]) == int(values_item[1]):
            iran_draws += 1
        else:
            iran_loses += 1

    elif keys_item[0] == 'Spain':
        spain_scored += int(values_item[0])
        spain_conceded += int(values_item[1])
        if int(values_item[0]) > int(values_item[1]):
            spain_wins += 1
        elif int(values_item[0]) == int(values_item[1]):
            spain_draws += 1
        else:
            spain_loses += 1

    elif keys_item[0] == 'Portugal':
        portugal_scored += int(values_item[0])
        portugal_conceded += int(values_item[1])
        if int(values_item[0]) > int(values_item[1]):
            portugal_wins += 1
        elif int(values_item[0]) == int(values_item[1]):
            portugal_draws += 1
        else:
            portugal_loses += 1

    elif keys_item[0] == 'Morocco':
        morocco_scored += int(values_item[0])
        morocco_conceded += int(values_item[1])
        if int(values_item[0]) > int(values_item[1]):
            morocco_wins += 1
        elif int(values_item[0]) == int(values_item[1]):
            morocco_draws += 1
        else:
            morocco_loses += 1

    if keys_item[1] == 'Iran':
        iran_scored += int(values_item[1])
        iran_conceded += int(values_item[0])
        if int(values_item[1]) > int(values_item[0]):
            iran_wins += 1
        elif int(values_item[1]) == int(values_item[0]):
            iran_draws += 1
        else:
            iran_loses += 1

    elif keys_item[1] == 'Spain':
        spain_scored += int(values_item[1])
        spain_conceded += int(values_item[0])
        if int(values_item[1]) > int(values_item[0]):
            spain_wins += 1
        elif int(values_item[1]) == int(values_item[0]):
            spain_draws += 1
        else:
            spain_loses += 1

    elif keys_item[1] == 'Portugal':
        portugal_scored += int(values_item[1])
        portugal_conceded += int(values_item[0])
        if int(values_item[1]) > int(values_item[0]):
            portugal_wins += 1
        elif int(values_item[1]) == int(values_item[0]):
            portugal_draws += 1
        else:
            portugal_loses += 1

    elif keys_item[1] == 'Morocco':
        morocco_scored += int(values_item[1])
        morocco_conceded += int(values_item[0])
        if int(values_item[1]) > int(values_item[0]):
            morocco_wins += 1
        elif int(values_item[1]) == int(values_item[0]):
            morocco_draws += 1
        else:
            morocco_loses += 1

iran_points = (iran_wins * 3) + (iran_draws * 1) + (iran_loses * 0)
spain_points = (spain_wins * 3) + (spain_draws * 1) + (spain_loses * 0)
portugal_points = (portugal_wins * 3) + (portugal_draws * 1) + (portugal_loses * 0)
morocco_points = (morocco_wins * 3) + (morocco_draws * 1) + (morocco_loses * 0)

iran_difference = iran_scored - iran_conceded
spain_difference = spain_scored - spain_conceded
portugal_difference = portugal_scored - portugal_conceded
morocco_difference = morocco_scored - morocco_conceded

spain_list = [spain_wins, spain_loses, spain_draws, spain_difference, spain_points]
iran_list = [iran_wins, iran_loses, iran_draws, iran_difference, iran_points]
portugal_list = [portugal_wins, portugal_loses, portugal_draws, portugal_difference, portugal_points]
morocco_list = [morocco_wins, morocco_loses, morocco_draws, morocco_difference, morocco_points]

print(f'Spain wins:{spain_wins} , loses:{spain_loses} , draws:{spain_draws} , goal difference:{spain_difference} , points:{spain_points}')
print(f'Iran wins:{iran_wins} , loses:{iran_loses} , draws:{iran_draws} , goal difference:{iran_difference} , points:{iran_points}')
print(f'Portugal wins:{portugal_wins} , loses:{portugal_loses} , draws:{portugal_draws} , goal difference:{portugal_difference} , points:{portugal_points}')
print(f'Morocco wins:{morocco_wins} , loses:{morocco_loses} , draws:{morocco_draws} , goal difference:{morocco_difference} , points:{morocco_points}')

