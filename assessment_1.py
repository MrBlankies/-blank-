import random
import datetime

filename = "game_file.txt"

file = open(filename, "a")
file.close()

file = open(filename, "r")
lines = file.readlines()
file.close()

# if file is empty, write the header
if len(lines) == 0:
    file = open(filename, "a")
    file.write("username,datetime,user_score,computer_score\n")
    file.close()

# rock paper scissors:
print(" Welcome to Rock-Paper-Scissors game\n")
choices = ("rock", "paper", "scissors")

# enter username = game start
username = input("Enter your username: ")
print(f"Welcome, {username}! Your username has been saved.\n")

# mode loop
while True:
    mode = input("Choose an option:\n1. Play a game (First to 10 wins)\n2. Check leaderboard\n3. Exit\n").strip()
    
    if mode == "1":

        user_score = 0
        computer_score = 0

        # player pick a choice 
        while user_score < 10 and computer_score < 10:
            user_choice = input("\nPick rock/paper/scissors: ").lower()

            if user_choice not in choices:
                print("Not a valid choice, try again.")
                continue

            # computer pick a random choice
            computer_choice = random.choice(choices)
            print(f"\nComputer picked: {computer_choice}")

            # compare choices, find winner or tie
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                print(f"Winner: {username}")
                user_score += 1
            else:
                print("Winner: Computer")
                computer_score += 1

            # show scores
            print(f"Score - {username}: {user_score}, Computer: {computer_score}")


        # score of 10 = game over, store their data
        print("\nGAME OVER")
        if user_score > computer_score:
            print(f"Congratulations, {username}! You are the winner!\n")
            file = open(filename, "a")
            file.write(f"{username},{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')},{user_score},{computer_score}\n")
        else:
            print("YOU LOSE!")
            file = open(filename, "a")
            file.write(f"{username},{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')},{user_score},{computer_score}\n")
            file.close()

    elif mode == "2":

        # create option to display top 5 players with most wins
        players_wins = {}

        file = open(filename, "r")
        lines = file.readlines()
        for line in lines[1:]:
            parts = line.strip().split(",")
            player = parts[0]
            wins = int(parts[2]) 
            if player in players_wins:
                players_wins[player] += wins
            else:
                players_wins[player] = wins

        sorted_players = sorted(players_wins.items(), key=lambda x: x[1], reverse=True)

        # display the top 5 players
        print("\nLeaderboard (Top 5 players with most wins):")
        for i, (player, win_count) in enumerate(sorted_players[:5]):
            print(f"{i+1}. {player} - Wins: {win_count//10}")
        
        user_wins = players_wins.get(username, 0)
        print("\nYour wins: ",user_wins//10,"\n")

    elif mode == "3":
        print(f"Goodbye {username}!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.\n")
