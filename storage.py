from colorama import Fore, Back, Style
import json

class Storage:

    question_dictionary = {}

    def __init__(self) -> None:
        pass

    def save_the_info():
        file_name = 'sets.json'
        with open(file_name, 'a',) as f:
            json.dump(question_dictionary, f, indent=2)
            print(Fore.GREEN + "***All done! Questions and answers have been stored!***" + Style.RESET_ALL)

    def promptQuestion():

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

            #question_dictionary[ask_question] = provide_answer