MAX_VALUES = {
    "blue": 14,
    "green": 13,
    "red": 12,
}

# open input.txt file
with open('input.txt') as input_file:

    possibleSum = 0

    for line in input_file:

        is_possible = True
        # line.split(":")[0]
        # "Game 1"
        gameID = int(line.split(":")[0].split()[1])

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
                for color in MAX_VALUES:
                    if word.find(color) >= 0:
                        if int(pulls[idx-1]) > MAX_VALUES[color]:
                            is_possible = False
                            break
                if not is_possible:
                    break

        if is_possible:
            possibleSum += gameID

        print("Game " + str(gameID) + " is "
              + ("possible" if is_possible else "impossible")
              )

    print("Sum: " + str(possibleSum))
