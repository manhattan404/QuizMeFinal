#Welcome Menu function --- [DONE]
#Log in menu --- Postponed
#Ability to create a topic
#Store questions and answers function --- [DONE]
#Take the quiz function --- [DONE]
#Play again function
#Json files function
#Ability to edit questions and answers function
#Ability to create topic. Then list topics 
#Need to make a new function that displays file names and let users be able to open the file (topic)
# Create a variable for save path of the topics users create

# UPDATE TRIAL

#from directory import CreateNewTopic
import json
import random
from colorama import Fore, Back, Style
import os
from main import main_menu
from menu import mainMenu
from question_model import Question

#Maybe open the json file then close it back?

question_dictionary = {}

# Need to be able to save new json file based on created topic by user
# Ability to edit title of created topic just in case user put wrong title 
# Be able to structure subtopics 
def save_the_info():
    file_name = 'sets.json'
    with open(file_name, 'a',) as f:
        json.dump(question_dictionary, f, indent=2)
        print(Fore.GREEN + "***All done! Questions and answers have been stored!***" + Style.RESET_ALL)
        

## def display_topics():

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

        #store responses to a dictionary
        #make an 'quit' string as an exception
        question_dictionary[ask_question] = provide_answer

def take_quiz():
    with open('sets.json') as json_file:
        question_dictionary = json.load(json_file)

    #read_json = open('sets.json')
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
    
def mainChoice():

    choice = input("Choose a letter: ")
    if choice == "A":
        store_questions_answers()
    if choice == "B":
        print("Module under construction")
    if choice == "C":
        take_quiz()
    if choice == "D":
        print("Module under construction")
    if choice == "E":
        print("Good bye! See you later!")
        exit()
    if choice == 'F':
        CreateNewTopic()

## Need to loop through main menu

mainMenu()
play_again()

