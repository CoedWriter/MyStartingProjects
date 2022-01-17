import random
lst = ["S", "W", "G"]
computer = 0
player = 0
print("Welcome to Snake-Water-Gun game!")
i = 1
time_limit = int(input("Rounds you want(add number): "))
print("Press")
while i <= time_limit:

    plyr_choice = input("S for snake\nW for water\nG for gun\n: ").capitalize()
    cmptr = random.choice(lst)
    # when input is s
    if plyr_choice == cmptr: print("Tie!")

    elif plyr_choice == "S":
        if cmptr == "W":
            print("You got it!")
            player += 1
        elif cmptr == "G":
            print("to Computer!")
            computer += 1
        print(f"Chances left: {time_limit - i}")
        i += 1

    #when input is w
    elif plyr_choice == "W":
        if cmptr == "S":
            print("to Computer!")
            computer += 1
        elif cmptr == "G":
            print("You got it!")
            player += 1
        print(f"Chances left: {time_limit - i}")
        i += 1

    #when input is g
    elif plyr_choice == "G":
        if cmptr == "S":
            print("You got it!")
            player += 1
        elif cmptr == "W":
            print("to Computer!")
            computer += 1
        print(f"Chances left: {time_limit - i}")
        i += 1
    else: print("Wrong input. Please try again!"); i += 1; print(f"Chances left: {time_limit - i}")


print(f"Scoreboard\nYou: {player}\nComputer: {computer}")
if player > computer: print("Insaniyat ki jeet hui\nYou won!")
elif computer > player: print("Roger report: machines took over the humankind\nYou lose!")
else: print("Draw!\nAnd that's how machines and humans started living with harmony and peace!")
