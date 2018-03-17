def find_winner(file_name):
    file = open(file=file_name, encoding="utf-8")
    results = []
    for row in file.readlines():
        results.append(row.strip()
                        .replace("\"", "")
                        .replace("Игр-", "")
                        .replace("Очков", "")
                        .split(","))

    max_result = 0
    team_name = []
    plays = int(results[0][1])
    different_plays = 0

    for team in results:
        if int(team[2]) > int(max_result):
            max_result = team[2]
            team_name.clear()
            team_name.append(team[0])
            continue
        elif int(team[2]) == int(max_result):
            team_name.append(team[0])
            continue
        elif int(team[1]) != plays:
            different_plays = 1
            continue

    print(("WINNER" if different_plays == 0 else "LIDER"), "IS", *team_name)


find_winner("teams.txt")
find_winner("teams2.txt")





