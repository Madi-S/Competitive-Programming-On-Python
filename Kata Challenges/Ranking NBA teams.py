def nba_cup(result_sheet, to_find):
    if not to_find:
        return to_find

    teams = {}
    matches = result_sheet.split(',')
    for match in matches:
        team1 = {'points': None, 'name': []}
        team2 = {'points': None, 'name': []}

        for word in match.strip().split(' '):
            try:
                n = float(word)
                if not word.isdigit():
                    return f'Error(float number):{match}'
            except:
                pass

            if word.isdigit():
                if not team1['points']:
                    team1['points'] = int(word)
                else:
                    team2['points'] = int(word)

            elif not team1['points']:
                team1['name'].append(word)

            elif not team2['points']:
                team2['name'].append(word)

        team1['name'] = ' '.join(team1['name'])
        team2['name'] = ' '.join(team2['name'])

        teams_data = (team1, team2)
        for i, team in enumerate(teams_data):
            team_name = team['name']

            team_points = team['points']
            other_team_points = teams_data[i - 1]['points']

            win, draw, loss = 0, 0, 0

            if team_points > other_team_points:
                win = 1
            elif team_points == other_team_points:
                draw = 1
            else:
                loss = 1

            if teams.get(team_name):
                teams[team_name]['W'] += win
                teams[team_name]['D'] += draw
                teams[team_name]['L'] += loss
                teams[team_name]['Scored'] += team_points
                teams[team_name]['Points'] += win * 3 + draw * 1
                teams[team_name]['Conceded'] += other_team_points
            else:
                teams[team_name] = {}
                teams[team_name]['W'] = win
                teams[team_name]['D'] = draw
                teams[team_name]['L'] = loss
                teams[team_name]['Name'] = team_name
                teams[team_name]['Scored'] = team_points
                teams[team_name]['Points'] = win * 3 + draw * 1
                teams[team_name]['Conceded'] = other_team_points

    res = teams.get(to_find)
    if res:
        return f"{res['Name']}:W={res['W']};D={res['D']};L={res['L']};Scored={res['Scored']};Conceded={res['Conceded']};Points={res['Points']}"
    return f'{to_find}:This team didn\'t play!'
