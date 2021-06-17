def main():
    num_of_players = input("Welcome to Ahler Bowlorama! How many players do you have? ")
    if int(num_of_players) > 6:
        num_of_players = input("Please enter 6 players or less: ")
    player_scores = {}
    i = 0
    while i in range(int(num_of_players)):
        player_name = raw_input("Enter player name: ")
        player_scores[player_name] = 0
        i += 1
    for player_name in player_scores:
        print(player_name + ": " + str(player_scores[player_name]))
    frame = 1
    for frame in range(10):
        frame += 1 
        if frame == 10:
            print("LAST FRAME")
        print
        print("FRAME " + str(frame))
        for player_name in player_scores:
            score = int(input(player_name + " - first round score: "))
            player_scores[player_name] += score
            if score == 10:
                print("STRIKE!")
            elif (score < 10) and (score >= 0):
                score = int(input("Second round score: "))
                player_scores[player_name] += score
        print
        if frame == 10:
            print("FINAL SCORES")
        for player_name in player_scores:
            print(player_name + ": " + str(player_scores[player_name]))
    print
    print("Game over. Thanks for playing!")

if __name__ == "__main__":
    main()