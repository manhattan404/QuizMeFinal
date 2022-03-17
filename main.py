import json
import random
from re import A
from colorama import Fore, Back, Style
import os
from menu import Menu


question_dictionary = {}

def save_the_info():
    file_name = 'sets.json'
    with open(file_name, 'a',) as f:
        json.dump(question_dictionary, f, indent=2)
        print(Fore.GREEN + "***All done! Questions and answers have been stored!***" + Style.RESET_ALL)
        
def store_questions_answers():
    
    prompt = Fore.YELLOW + "*****You will be asked to enter a question and an answer to be saved in the file*****" + Style.RESET_ALL
    prompt += Fore.YELLOW + "\n*****Type 'quit' to stop program*****" + Style.RESET_ALL

    print(prompt)

    active = True

    while active:
        ask_question = input("Enter a question: ")
        if ask_question == "quit":
            save_the_info()
            active = False  
            main_menu()
        else:
            provide_answer = input("Answer: ")

        question_dictionary[ask_question] = provide_answer

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
    
Menu.mainMenu()
play_again()

