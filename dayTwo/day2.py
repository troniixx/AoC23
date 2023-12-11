def id_finder(file_path):
    limits = {"red": 12, "green": 13, "blue:": 14}
    game_limit = {}
    flag = True
    ids = []

    with open(file_path, "r") as f:
        for line in f:
            j = 0
            games = line.split(";")
            pulls = games.split(",")
            splits = pulls.split(" ")
            for i, split in enumerate(splits):
                if split in limits:
                    game_limit[split] = int(splits[i+1])

                for limit in game_limit:
                    if game_limit[limit] < limits[limit]:
                        flag = False
                    else:
                        ids.append(i)
                j+=1
                


if __name__ == '__main__':
    print(id_finder("/Users/merterol/Desktop/AoC23/dayTwo/games_simple.txt"))
    #print(id_finder("/Users/merterol/Desktop/AoC23/dayTwo/games.txt"))