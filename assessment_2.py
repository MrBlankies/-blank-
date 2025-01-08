# Quiz game

import requests
import random


# Create file part

file_login = "login.txt"
file_score = "score.txt"

file = open(file_login, "a")
file.close()
file = open(file_score, "a")
file.close()

file = open(file_login, "r")
lines = file.readlines()
file.close()

if len(lines) == 0:
    file = open(file_login, "w")
    file.write("Username,PIN\n")
    file.close()

file = open(file_score, "r")
lines = file.readlines()
file.close()

if len(lines) == 0:
    file = open(file_score, "w")
    file.write("question,correct_answer,wrong_ans1,wrong_ans2,wrong_ans3\n")
    file.close()


# Account login part

answer = input("Do you have an account (yes/no): ").lower().strip()
found = False

if answer == "yes":
    username = input("Enter username: ").strip()
    PIN = input("Enter PIN: ").strip()

    file = open(file_login) 
    found = False

    for line in file:
        stored_username, stored_PIN = line.strip().split(",")
        if stored_username == username and stored_PIN == PIN:
            found = True
            break  

    if found:
        print(f"Welcome {stored_username}!")
    else:
        print("Invalid username or PIN.")

elif answer == "no":
    print("No worries! Create one now.")
    username = input("Enter a username: ").strip()
    PIN = input("Enter a PIN: ").strip()

    while not (PIN.isdigit() and len(PIN) == 4):
        print("Not a 4 digit PIN")
        PIN = input("Enter a PIN: ").strip()

    file = open(file_login)
    for line in file:
        stored_username, stored_PIN = line.strip().split(",")
        if stored_username == username:
            print("Username already exists. Please try again.")
            exit()

    file = open(file_login, "a")  
    file.write(f"{username},{PIN}\n")  
    print(f"Account created successfully! Welcome, {username}.")
    found = True

else:
    print("Invalid answer.")


# Quiz part

if found:
    again = "yes"
    while again == "yes":
        url = "https://opentdb.com/api.php?amount=10"
        response = requests.get(url)
        data = response.json()

        question_data = data["results"][0]
        question = question_data["question"]
        incorrect = question_data["incorrect_answers"]
        correct = question_data["correct_answer"]

        options = [correct] + incorrect
        random.shuffle(options)

        option_map = {"A": options[0], "B": options[1], "C": options[2], "D": options[3]}

        print(question)
        print("A:", options[0])
        print("B:", options[1])
        print("C:", options[2])
        print("D:", options[3])

        answer = input("Enter your answer (A, B, C, D): ").strip().upper()
        if answer in option_map:
            if option_map[answer] == correct:
                print("Correct!")
            else:
                print("Wrong! The correct answer is:", correct)
        else:
            print("Invalid choice. Please enter A, B, C, or D.")

        file = open(file_score, "a")

        file.write(f"{question},")
        file.write(f"{correct},")
        file.write(f"{incorrect},")
        file.write("\n")
        
        file.close()

        again = input("Want to play again? (yes/no): ")
