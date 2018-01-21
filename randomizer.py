"""Random picker thaat may be used in classes made for my bio class."""

import random


students = ["Halle Conaghan", 'Svanik Dani', 'Daniella Donohue',
            'Christian Fusco', 'Marilise DeBuck', 'Lennox Lamar',
            'Christopher Mayo', 'Jacob Naddelman', 'Isabel Piantini',
            'Youcef Soltani', 'Rebeca Vargas', 'Tyler Wasilewski']
pickedstudents = []

studlen = len(students)
print(studlen)
# just to pick one student
pick = random.choice(students)
print(pick)
# for test seating
choicenum = 1
while choicenum < (studlen + 1):
    pick = random.choice(students)
    students.remove(pick)
    pickedstudents.append(pick)
    print(f'#{choicenum} {pick}')
    choicenum = choicenum + 1
