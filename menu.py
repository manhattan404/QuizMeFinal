from prettytable import PrettyTable

myTable = PrettyTable(['Reviewer'])

class Menu:


    def __init__(self, A, B, C, D, E):
        self.choiceA = A
        self.choiceB = B
        self.choiceC = C
        self.choiceD = D
        self.choiceE = E

    def mainMenu():
        myTable.add_rows(
            [
                ["[A] Store questions and answers"],
                ["[B] Edit questions and answers" ],
                ["[C] Take the quiz " ],
                ["[D] See scores and progress" ],
                ["[E] Quit" ],
            ]
        )

        print(myTable)
