# part 1

# open file
file = open("story.txt")
# read lines 
lines = file.readlines()
# initialize a counter 
counter = 0
# ask user for a word
word = input("Type a word to see how many times it exists in the story: ").lower()
# Punctuation characters to remove
punctuation = ",.?!;:"

# for each line
for line in lines:
    # Convert line to lowercase and split into words
    words = line.lower().split()
    # Loop through each word in the line
    for w in words:
        # Remove punctuation around the word
        clean_word = w.strip(punctuation)
        # Check if the cleaned word matches the input word
        if clean_word == word:
            counter += 1

# check if the word was found
if counter > 0:
    # print the word and the counter
    print(word + ":", counter)
else:
    print("Selected word is not in the story. Try again.")


# part 2


filename = "users.csv"

file = open(filename, "a")
file.close()

file = open(filename, "r")
lines = file.readlines()
file.close()

# if file is empty, write the header
if len(lines) == 0:
    file = open(filename, "a")
    file.write("Username,PIN,First name,Last name\n")
    file.close()


# Ask user if they have an account
answer = input("Do you have an account (yes/no): ").lower().strip()

if answer == "yes":
    # Log in with username and PIN
    username = input("Enter username: ").strip()
    PIN = input("Enter PIN: ").strip()

    # Read the file and check for username and PIN
    file = open(filename) 
    found = False

    # Read each line in the file
    for line in file:
        # Split each line by comma to get the username and PIN
        stored_username, stored_PIN, stored_first_name, stored_last_name  = line.strip().split(",")
        if stored_username == username and stored_PIN == PIN:
            found = True
            break  # Exit the loop if a match is found

    if found:
        print(f"Welcome {stored_first_name}!")
    else:
        print("Invalid username or PIN.")

elif answer == "no":
    # Create a new account
    print("No worries! Create one now.")
    username = input("Enter a username: ").strip()
    PIN = input("Enter a PIN: ").strip()
    while not (PIN.isdigit() and len(PIN) == 4):
        print("Not a 4 digit PIN")
        PIN = input("Enter a PIN: ").strip()
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    
   
        # Check if username already exists
    file = open(filename)
    for line in file:
        stored_username, stored_PIN, stored_first_name, stored_last_name  = line.strip().split(",")
        if stored_username == username:
            print("Username already exists. Please try again.")
            exit()
            # Add the new user to the file using write
    file = open(filename, "a")  
    file.write(f"{username},{PIN},{first_name},{last_name}\n")  
    print(f"Account created successfully! Welcome, {first_name}.")
else:
    print("Invalid Answer.")
