# open input.txt file
with open('input.txt') as input_file:

    possibleSum = 0
    total_power = 0
    
    for line in input_file:

        # line.split(":")[0]
        # "Game 1"
        gameID = int(line.split(":")[0].split()[1])

        min_values = {
            "blue": 0,
            "green": 0,
            "red": 0,
        }
        
        # line.split(":")[1]
        # " 7 blue, 9 red, 1 green; 8 green; 10 green, 5 blue, 3 red; 11 blue, 5 red, 1 green"
        # line.split(":")[1].split(";")
        # " 7 blue, 9 red, 1 green"
        # " 8 green"
        # " 10 green, 5 blue, 3 red"
        # " 11 blue, 5 red, 1 green"
        for game in line.split(":")[1].split(";"):
            
            # game.split()
            # ["7", "blue,", "9", "red,", "1", "green"]
            # ["8", "green"]
            # ["10", "green,", "5", "blue,", "3", "red"]
            # ["11", "blue,", "5", "red,", "1", "green"]
            pulls = game.split()
            for idx, word in enumerate(pulls):
                for color in min_values:
                    if word.find(color) >= 0:
                        # value of the color
                        val = int(pulls[idx-1])
                        if val > min_values[color]:
                            min_values[color] = val
        
        game_power = 1
        for color in min_values:
            game_power *= min_values[color]

        print("Game " + str(gameID) + " power = " + str(game_power))
        total_power += game_power

    print("Sum of powers: " + str(total_power))
