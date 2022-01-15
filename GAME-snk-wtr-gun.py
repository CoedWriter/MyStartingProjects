import random
lst = {"Snake", "Water", "Gun"}
player = {"Computer": 0, "You": 0}
print("Welcome to Snake-Water-Gun game!\nPress : ")
i = 1
while i <= 10:

    plyr_choice = input()
    cmptr = random.choice(lst)
    # when input is s
    if plyr_choice == "s" and cmptr == "w": print("ghichir-phichir")
    else: print("it's alright!")



    i += 1
