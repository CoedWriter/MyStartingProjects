def gettime():
    import datetime
    return datetime.datetime.now()

def log():
    print("Choose the client. Press")
    client = int(input("1 for Harry\n2 for Rohan\n3 for Hammad\n: "))
    ykh = 1

    if client == 1:
        while ykh == 1:
            print("What do you want to log?\n")
            wht = int(input("Press\n1 for food\n2 for exercise\n: "))
            if wht == 1:
                f = open("HarryDiet.txt", "a")
                food = input("What Harry has eaten?\n: ")
                f.write(str([str(gettime())]) + food + "\n")
                f.close()
            else:
                f = open("HarryExercise.txt","a")
                exercise = input("What exercises has Harry done?\n: ")
                f.write(str([str(gettime())]) + exercise + "\n")
                f.close()
            ykh = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))

    elif client == 2:
        while ykh == 1:
            print("What do you want to log? Press")
            wht = int(input("1 for Food\n2 for Exercise\n:"))
            if wht == 1:
                f = open("RohanDiet.txt", "a")
                food = input("What Rohan has eaten?\n: ")
                f.write(str([str(gettime())]) + food + "\n")
                f.close()

            else:
                f = open("RohanExercise.txt", "a")
                exercise = input("Exercises of Rohan\n: ")
                f.write(str([str(gettime())]) + exercise + "\n")
                f.close()
            ykh = int(input("Do you want to log more for Rohan? \n1. Yes \n2. No"))

    elif client == 3:
        while ykh == 1:

            print("What do you want to log? Press")

            wht = int(input("1 for Food\n2 for Exercise\n:"))

            if wht == 1:

                f = open("HammadDiet.txt", "a")

                food = input("What Hammad has eaten?\n: ")

                f.write(str([str(gettime())]) + food + "\n")

                f.close()


            else:

                f = open("HammadExercise.txt", "a")

                exercise = input("Exercises of Hammad\n: ")

                f.write(str([str(gettime())]) + exercise + "\n")

                f.close()
            ykh = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No"))
    else:
        print("wrong input! please try again!1")



def retrieve():

    print("Choose the client. Press")
    client = int(input("1 for Harry\n2 for Rohan\n3 for Hammad\n: "))
    ykh = 1
    if client == 1:
        while ykh == 1:
            print("What do you want to retrieve?\nPress")
            wht = int(input("1 for Food\n2 for Exercise\n: "))
            if wht == 1:
                f = open("HarryDiet.txt", "rt")
                a = f.read()
                print(a)
                f.close()
            else:
                f = open("HarryExercise.txt", "rt")
                a = f.read()
                print(a)
                f.close()
            ykh = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))

    elif client == 2:
        while ykh == 1:
            print("What do you want to retrieve? Press")
            wht = int(input("1 for Food\n2 for Exercise:"))
            if wht == 1:
                f = open("RohanDiet.txt", "rt")
                print(f.readlines())
                f.close()

            else:
                f = open("RohanExercise.txt", "rt")
                print(f.readlines())
                f.close()
            ykh = int(input("Do you want to retrieve more for Rohan? \n1. Yes \n2. No"))

    elif client == 3:
        while ykh == 1 :
            print("What do you want to retrieve?\nPress")
            wht = input("1 for Food\n2 for Exercise\n: ")
            if wht == 3:
                f = open("HammadDiet.txt","rt")
                a = f.read()
                print(a)
                f.close()
            else:
                f = open("HammadExercise.txt", "rt")
                a = f.read()
                print(a)
                f.close()
            ykh = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))
    else:
        print("wrong input! please try again!2")
    ykh = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))

print("Welcome to Health Management System\nWhat would you like to do?")
act = int(input("Press\n1 to log\n2 to retrieve\n: "))
if act == 1:
    log()
elif act == 2:
    retrieve()
else:
    print("Wrong input! Please try again!0")


