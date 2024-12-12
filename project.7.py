# part 1


students = {
	10: {'name': 'Russell Lopez', 'grades': [45, 34, 67, 45, 0, 34]},
    11: {'name': 'Theresa Campbell', 'grades': [40, 34, 20, 44, 56, 18, 34, 35]},
    12: {'name': 'Martin Roy', 'grades': [46, 55, 71, 67, 55, 64]},
    13: {'name': 'Nicole Young', 'grades': [40, 38, 42, 42, 51]},
    14: {'name': 'Elizabeth Diaz', 'grades': [44]},
    15: {'name': 'Susan Coleman', 'grades': [56, 19, 55, 34, 30, 18]},

}

for i in students:
    grades = students[i]['grades']
    if students[i]['name'] == 'Elizabeth Diaz':
        total = sum(grades)
    else:
        total = sum(grades) // 6
    if total < 40:
        print(students[i]['name']+':',total)


# part 2


import requests
import json

url = 'https://bored-api.appbrewery.com/random'

response = requests.get(url)
data = json.loads(response.text)

activity = data['activity']
print(activity)
