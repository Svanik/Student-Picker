"""Random picker that may be modified for use in classes made for my bio class."""
import random


def pickonestudent():
    """Pick one studnet when called."""
    pick = random.choice(students)
    print(pick)


def pickxstudents():
    """Pick x studnet when called."""
    numofstud = input("Enter Num of Students to Pick: ")
    if numofstud <= len(students) and numofstud > 0:
        if numofstud.isnumeric():
            numofstud = int(numofstud)
            choicenum = 1
            while choicenum < (numofstud + 1):
                pick = random.choice(students)
                students.remove(pick)
                pickedstudents.append(pick)
                print(f'#{choicenum} {pick}')
                choicenum = choicenum + 1
        else:
            print("You did not enter a number try again. ")
            pickxstudents()
    else:
        print("The number you entered is too large ")
        pickxstudents()


def pickallstudents():
    """Pick all studnets one at a time when called."""
    studlen = len(students)
    choicenum = 1
    while choicenum < (studlen + 1):
        pick = random.choice(students)
        students.remove(pick)
        pickedstudents.append(pick)
        print(f'#{choicenum} {pick}')
        choicenum = choicenum + 1


def goagain():
    """Pick wheter to go again."""
    while True:
        goagain = input("Would you like to pick again. (y/n)")
        if goagain == 'y' or goagain == 'Y':
            x = 1
            break
        elif goagain == 'n' or goagain == 'N':
            x = 0
            break
        else:
            print('Invalid Input, Please retry')
    return x


def pickthistodo():
    """Pick what needs to be done next."""
    dothis = input('''Please enter the number that correseponds with the option
                    1) Pick 1 students
                    2) Pick a given number of students
                    3) Pick all studnets
                    Enter Choice: ''')
    if dothis == '1' or dothis == '2' or dothis == '3':
        dothis = int(dothis)
        return dothis
    else:
        print("Your input is not valid pleace input 1, 2, or 3")
        pickthistodo()


students = ["Halle Conaghan", 'Svanik Dani', 'Daniella Donohue',
            'Christian Fusco', 'Marilise DeBuck', 'Lennox Lamar',
            'Christopher Mayo', 'Jacob Naddelman', 'Isabel Piantini',
            'Youcef Soltani', 'Rebeca Vargas', 'Tyler Wasilewski']
pickedstudents = []

x = 1
while x == 1:
    donow = pickthistodo()
    if donow == 1:
        pickonestudent()
        students = ["Halle Conaghan", 'Svanik Dani', 'Daniella Donohue',
                    'Christian Fusco', 'Marilise DeBuck', 'Lennox Lamar',
                    'Christopher Mayo', 'Jacob Naddelman', 'Isabel Piantini',
                    'Youcef Soltani', 'Rebeca Vargas', 'Tyler Wasilewski']
        pickedstudents = []
        x = goagain()
    elif donow == 2:
        pickxstudents()
        students = ["Halle Conaghan", 'Svanik Dani', 'Daniella Donohue',
                    'Christian Fusco', 'Marilise DeBuck', 'Lennox Lamar',
                    'Christopher Mayo', 'Jacob Naddelman', 'Isabel Piantini',
                    'Youcef Soltani', 'Rebeca Vargas', 'Tyler Wasilewski']
        pickedstudents = []
        x = goagain()
    elif donow == 3:
        pickallstudents()
        students = ["Halle Conaghan", 'Svanik Dani', 'Daniella Donohue',
                    'Christian Fusco', 'Marilise DeBuck', 'Lennox Lamar',
                    'Christopher Mayo', 'Jacob Naddelman', 'Isabel Piantini',
                    'Youcef Soltani', 'Rebeca Vargas', 'Tyler Wasilewski']
        pickedstudents = []
        x = goagain()
    else:
        x = 1
