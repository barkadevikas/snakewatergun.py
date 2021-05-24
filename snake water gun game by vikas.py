import random
l1=['s','w','g']

no_of_chance=0
chance=10
human_point=0
computer_point=0

print("\t\t\t snake water gun game ")
print("type s for snake\n w gor water \n g for gun")
while no_of_chance<chance:
    _input=input('snake,water,gun:')
    _random=random.choice(l1)
    if _input==_random:
        print("both choice same game tie\n")
    elif _input=='s' and _random=='w':
        human_point=human_point+1
        print(f"you choice {_input} and comuter choice {_random}\n")
        print("you won this game\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")


    elif _input == 's' and _random == 'g':
        computer_point=computer_point+1
        print(f"you choice {_input} and comuter choice {_random}\n")
        print("computer won this game\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input == 'w' and _random == 's':
        computer_point=computer_point+1
        print(f"you choice {_input} and comuter choice {_random}\n")
        print("computer won this game\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input == 'w' and _random == 'g':
        human_point=human_point+1
        print(f"you choice {_input} and comuter choice {_random}\n")
        print("you won this game\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input == 'g' and _random == 'w':
        computer_point=computer_point+1
        print(f"you choice {_input} and comuter choice {_random}\n")
        print("computer won this game\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input == 'g' and _random == 's':
        human_point = human_point + 1
        print(f"you choice {_input} and comuter choice {_random}\n")
        print("you won this game\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    else:
        print("you enter wrong charecter plz select valid charecter\n")

    no_of_chance=no_of_chance+1
    print(f"chance-{no_of_chance} is left out of {chance}\n")


print("game over")
if computer_point==human_point:
    print("game tie")
elif computer_point>human_point:
    print("computer won the game")
else:
    print("you won the game")
print(f"your point is {human_point} and computr point is{computer_point}")