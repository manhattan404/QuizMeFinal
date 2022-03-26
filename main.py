import json
from multiprocessing.dummy import active_children
import random
from colorama import Fore, Back, Style
import os
from prettytable import PrettyTable
from storedata import Questions
import tqdm as tq
import time

myTable = PrettyTable(['Reviewer'])


def showMenu():
    myTable.add_rows(
        [
            ["[A] Store questions and answers"],
            ["[B] Edit questions and answers"],
            ["[C] Take the quiz "],
            ["[D] See scores and progress"],
            ["[E] Quit"],
        ]
    )
    print(myTable)


def chooseOption():
    choice = input("Choose an option: ").lower()

    if choice == "a":
        Questions.prompt()
        Questions.enterquestion()
    elif choice == "quit":
        print("Goodbye!")


def take_quiz():
    with open('sets.json') as json_file:
        question_dictionary = json.load(json_file)

    score = 0
    items = list(question_dictionary.items())
    random.shuffle(items)

    for q, a in items:
        real_question = q
        quote = ": "
        if input(Fore.YELLOW + real_question + quote + Style.RESET_ALL).lower() == a.lower():
            score += 1
            print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Wrong!" + Style.RESET_ALL)
            print("Sorry, correct answer is \"{}\".".format(a))
    return score
    print("Your total score is {score}")


def play_again():
    prompt = input("Would you like to try again? [Y/N]")
    if prompt == "Y":
        take_quiz()
    else:
        exit()


def enter_user_name():
    user_name = input("Please enter your name: ")
    capitalized_name = user_name.title()
    welcome_message = "Welcome {}!".format(capitalized_name)
    print(welcome_message)


def menuLoop():
    active = True
    while active:
        showMenu()
        chooseOption()
    else:
        active = False
        print("Goodbye")


menuLoop()
