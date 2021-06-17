def main():
    team_one = raw_input("Welcome to cornhole! What is the first team's name? ")
    team_two = raw_input("What is the second team's name? ")
    team_scores = {}
    team_scores[team_one] = 0
    team_scores[team_two] = 0 
    round = 1 
    while (team_scores[team_one] != 21) and (team_scores[team_two] != 21):
        print
        print("Round " + str(round))
        team_one_score = int(raw_input("Team " + team_one + " how many points did you score? "))
        if (team_one_score > 12) or (team_one_score < 0):
            team_one_score = int(raw_input("Please enter a number 0 through 12."))
        team_two_score = int(raw_input("Team " + team_two + " how many points did you score? "))
        if (team_two_score > 12) or (team_two_score < 0):
            team_two_score = int(raw_input("Please enter a number 0 through 12."))
        if team_one_score > team_two_score:
            team_scores[team_one] += (team_one_score - team_two_score)
        elif team_two_score > team_one_score:
            team_scores[team_two] += (team_two_score - team_one_score)
        if team_scores[team_one] > 21:
            print
            print("Bust!")
            team_scores[team_one] = 15
        if team_scores[team_two] > 21:
            print("Bust!")
            team_scores[team_two] = 15
        print
        print(team_one + ": " + str(team_scores[team_one]))
        print(team_two + ": " + str(team_scores[team_two]))
        round += 1 
    print
    print("Good game!")
    if team_scores[team_one] > team_scores[team_two]:
        print("Winner: Team " + team_one + "!")
    else:
        print("Winner: Team " + team_two + "!")
main() 