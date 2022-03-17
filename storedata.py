from tkinter.messagebox import askquestion


class AskAndStore:

    bank={}

    def __init__(self):
        self.askaway

    def askaway(self):

ask_question = input("Enter a question: ")
ask_answer = input("Enter the answer: ")


AskAndStore.askaway("How are you?")
