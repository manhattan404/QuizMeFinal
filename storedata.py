from colorama import Fore, Back, Style
import main

class Questions:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def prompt():
        prompt = Fore.YELLOW + "*****You will be asked to enter a question and an answer to be saved in the file*****" + Style.RESET_ALL
        prompt += Fore.YELLOW + "\n*****Type 'quit' to stop program*****" + Style.RESET_ALL

        print(prompt)

    def enterquestion():
        active = True
        endprogram = "QUIT".lower()
        while active:
            ask_question = input("Enter a question: ")
            if ask_question == "quit":
                active = False
                print("DONE")
            else:
                provide_answer = input("Answer: ")
