# part 1

students = []
usernames = []

while True:
    name = input("Type full name of student (or type 'stop' to finish): ")
    if name.lower() == 'stop':  
        break
    students.append(name)

print("Current list of students: ", students)

for i in range(len(students)):
    full_name = students[i]
    name_parts = full_name.split()
    first_initial = name_parts[0][0].lower()
    last_name = name_parts[-1].lower()

    base_username = first_initial + last_name
    username = base_username
    counter = 1

    while username in usernames:
        username = base_username + str(counter)
        counter += 1

    usernames.append(username)
    print(username)

# part 2

import random 

special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lower_case_letters = ["a", "b", "c", "d", "e" ,"f" ,"g", "h","i" ,"j" ,"k" ,"l" ,"m" ,"n", "o" ,"p" ,"q","r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x", "y" ,"z"]
upper_case_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

password = ""
password += random.choice(lower_case_letters)  
password += random.choice(upper_case_letters)  
password += random.choice(digits)              
password += random.choice(special_characters)  
all_lists = [lower_case_letters, upper_case_letters, digits, special_characters]

for i in range(6):
    selected_list = random.choice(all_lists)
    random_character = random.choice(selected_list)
    password += random_character
print("Random Generated password: ", password)