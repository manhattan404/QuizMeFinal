from json.tool import main
from colorama import Fore, Back, Style


class Questions:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def prompt():
        prompt = Fore.YELLOW + \
            "*****You will be asked to enter a question and an answer to be saved in the file*****" + Style.RESET_ALL
        prompt += Fore.YELLOW + "\n*****Type 'menu' to go back to main menu*****" + Style.RESET_ALL

        print(prompt)

    def enterquestion():
        active = True
        endprogram = "QUIT".lower()
        while active:
            ask_question = input("Enter a question: ")
            if ask_question == "menu":
                active = False
                print("Going back to main menu...")
            else:
                provide_answer = input("Answer: ")
