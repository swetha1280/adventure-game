import random
import time


def print_time(message):
    print(message)
    time.sleep(2)


def won():
    print("you won great choice!")


def lost():
    print("you lost the game")


def game1():
    print_time("you are travelling in a car somewhere in the world")
    print_time("you actually dont have any idea about the palce")
    print_time("your car got troubled in the middle of the forest")
    print_time("you have three chances. so choose a number:")
    trouble = input("1.Leave the car\n"
                    "2.Stay in car\n"
                    "3.Try to repair\n")
    if trouble == "1":
        print_time("u are walking down the road \n"
                   "u found a abonded viallage")
        print_time("u have two choices .choose a number:")
        village = input("1.enter the village\n"
                        "2.pass by\n")
        if village == "1":
            print_time("whole village is dark except two houses")
            print_time("warning: everything u see is not true")
            print_time("choose a number which house u want to enter:")
            k = input("1.bad house\n"
                      "2.good house\n")
            if k == "1":
                print_time("your lucky.This is a house of angles")
                print_time("they help you to reach the house.")
                won()
            elif k == "2":
                print_time("damn!the house is full of ghost.")
                print_time("you had no chance to take any actions!")
                lost()
            else:
                print_time("you have given invalid input")
                print_time("you will be redirected to game 1")
                game1()
        elif village == "2":
            print_time("you have been walking miles...")
            print_time("you reached a village \n"
                       "and people of that village helped u")
            won()
        else:
            print_time("you have given invalid input")
            print_time("you will be redirected to game 1")
            game1()
    elif trouble == "2":
        print_time("you choose to stay in car")
        print_time("You are hearing a loud noice in a distance")
        print_time("you have chance to call only one person")
        print_time(" choose a number:")
        confusion = input("1.police\n"
                          "2.friend\n")
        if "1" == confusion:
            print_time("you have choosen good choice\n")
            print_time("police are near by\n")
            print_time("They will come and fight with the monster\n")
            print_time("you will be safe\n")
            won()
        elif "2" == confusion:
            print_time("you friend come to you to help\n")
            print_time("But monster will come and attack you\n")
            print_time("you and your friend will die")
            lost()
        else:
            print_time("you have given invalid input")
            print_time("you will be redirected to game 1")
            game1()
    elif trouble == "3":
        print_time(" You try Repair the car \n")
        print_time("you check all the tools in the car\n")
        a = input("1.repair success\n"
                  "2.repair fail\n")
        if a == "1":
            print_time("you have succesfully repaired the car\n"
                       "you  reached the house safely\n")
            won()
        elif a == "2":
            print_time("you failed to repair the car\n"
                       "It will become dark\n"
                       "monster will attack the car\n"
                       "you will die\n")
            lost()
        else:
            print_time("you have given invalid input")
            print_time("you will be redirected to game 1")
            game1()
    else:
        print_time("you have given invalid input")
        print_time("you will be redirected to game 1")
        game1()


def game2():
    print_time("this ia a game you can win in one move")
    print_time("you are living in a village.\n"
               "you are special person in village.")
    print_time("oneday a dragon attacked your village")
    attack = input("1.fight alone\n"
                   "2.fight along with people\n"
                   "3.run away\n")
    if attack == "1":
        print_time("with all your magical powers you defeated the dragon.\n"
                   "and u successfully saved the village.\n"
                   "village people praised you alot!!.")
        won()
    elif attack == "2":
        print_time("with your magical powers you defeated dragon\n"
                   "but u lost village people in fight.\n"
                   "you will feel sorry forr them\n"
                   "you won but you lost\n")
        won()
    elif attack == "3":
        print_time("you betrayed the people\n"
                   "dragon will attact the village\n"
                   "all the people in the village are dead")
        lost()
    else:
        print_time("you have given invalid input")
        print_time("you will be redirected to game2")
        game2()


def story():
    print_time("name of the character will choose randomly")
    name = ("vivek", "bunny", "mukul", "shankar", "shiva")
    random.choice(name)
    print_time(random.choice(name) + " welcome to the gaming corner!")
    while True:
        print_time("you have a games to play\n"
                   "choose a number:")
        game = input("1.The abonded village\n"
                     "2.The dragon world\n")
        if "1" == game:
            game1()
            break

        elif "2" == game:
            game2()
            break
        else:
            print_time("you have given invalid input")
            print_time("you will be redirected")
            break
    print_time("Do you want to try again")
    try_again = input("1.yes\n"
                      "2.no\n")
    if "1" == try_again:
        story()
    elif "2" == try_again:
        print_time("hope you enjoyed the game\n"
                   "Thankyou")
    else:
        print_time("you have given invalid input")
        print_time("you will be redirected to story")
        story()


story()
