answer = "yes"
while answer == "yes":
    year = input("Give year: ")
    year = int(year)
    if year % 4 == 0 and year % 100 != 0:
        print("Leap")
    elif year % 100 == 0 and year % 400 == 0:
        print("Leap")
    else:
        print("Not Leap")
    answer = input("Continue? ")